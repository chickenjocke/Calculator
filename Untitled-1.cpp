
#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <limits>
#include <stdexcept>
#include <tuple>
#include <complex>

struct Residuals {
    double first;
    double second;
};

struct Point {
    double x;
    double y;
    bool is_shaded = false;
    bool is_boundary = false;
    bool solid_boundary = false;
    int layer = 0;
    bool is_point = false;
};

int variable_count = 0;
std::string algebra_variable = "x";
bool has_equals = false;
std::string equation;
std::vector<std::pair<std::string, std::string>> math_input;
std::vector<std::pair<std::string, int>> variables;
double graph_size_x = 10;
double graph_size_y = 10;
std::string relational_operator = "=";
std::vector<std::pair<double, double>> given_points;
bool is_automatic = false;
double pi = 3.141592653589793;
double radians;
bool needs_vertical = false;
bool prints_angles = true;
bool has_polar = false;
double theta_count = 1;
double fibonacci_number = 0.3063489;
bool has_fib = false;
double decimal_precision = 12;
bool print_square_roots = false;
bool analyze_function = false;
bool calculate_limit = false;
bool calculate_derivative = false;
bool calculate_definite_integral = false;
bool calculate_sigma = false;
double limit_target = 0.0;
double derivative_target = 0.0;
double integral_lower_bound = 0.0;
double integral_upper_bound = 0.0;
std::string sigma_variable;
long long sigma_lower_bound = 0;
long long sigma_upper_bound = 0;
double analysis_range = 10.0;
double root_search_limit = 10000.0;

struct DrawingPrimitive {
    std::string type;
    std::pair<double, double> first;
    std::pair<double, double> second;
};
struct SegmentAnnotation {
    double x;
    double y;
    double length;
};
std::vector<DrawingPrimitive> drawing_primitives;

bool check_inequality(double left, double right, std::string op);
double evaluate_expression(
    const std::vector<std::pair<std::string, std::string>>& side_tokens,
    double x_guess, double y_guess);


int find_variables(std::string chosen_var) {
    int count = 0;
    for (auto entry : variables) {
        if (chosen_var == entry.first) {
            count++;
        }
    }
    return count;
}

int get_precedence(std::string op) {
    if (op == "plus" || op == "minus") return 1;
    if (op == "multiply" || op == "divide") return 2;
    if (op == "unary_minus") return 3;
    if (op == "exponent") return 4;
    if (op == "square_root") return 6;
    if (op == "vertical") return 5;
    if (op == "sin" || op == "cos" || op == "tan" || op == "asin" || op == "acos" || op == "atan" || op.rfind("log", 0) == 0) return 6; 
    return 0;
}

bool split_function_arguments(const std::string& text, std::vector<std::string>& arguments) {
    int depth = 0;
    std::size_t start = 0;
    for (std::size_t i = 0; i < text.size(); ++i) {
        if (text[i] == '(') {
            ++depth;
        } else if (text[i] == ')') {
            if (--depth < 0) return false;
        } else if (text[i] == ',' && depth == 0) {
            arguments.push_back(text.substr(start, i - start));
            start = i + 1;
        }
    }
    if (depth != 0) return false;
    arguments.push_back(text.substr(start));
    return true;
}

bool parse_finite_number(const std::string& text, double& value) {
    try {
        std::size_t parsed = 0;
        value = std::stod(text, &parsed);
        return parsed == text.size() && std::isfinite(value);
    } catch (const std::exception&) {
        return false;
    }
}

double apply_operator(double a, double b, std::string op) {
    if (op == "plus") return a + b;
    if (op == "minus") return a - b;
    if (op == "multiply") return a * b;
    if (op == "divide") {
        if (b == 0) return std::numeric_limits<double>::quiet_NaN();
        return a / b;
    }
    if (op == "exponent") return std::pow(a, b);
    return 0;
}

double calculate_integral(
    const std::vector<std::pair<std::string, std::string>>& function,
    double lower_bound,
    double upper_bound) {
    if (lower_bound == upper_bound) return 0.0;

    // Composite Simpson's rule with an even number of intervals.
    constexpr int intervals = 10000;
    const double step = (upper_bound - lower_bound) / intervals;
    auto evaluate_at = [&](double x) {
        return algebra_variable == "y"
            ? evaluate_expression(function, 0.0, x)
            : evaluate_expression(function, x, 0.0);
    };

    double sum = evaluate_at(lower_bound) + evaluate_at(upper_bound);
    if (!std::isfinite(sum)) return std::numeric_limits<double>::quiet_NaN();
    for (int i = 1; i < intervals; ++i) {
        const double value = evaluate_at(lower_bound + i * step);
        if (!std::isfinite(value)) return std::numeric_limits<double>::quiet_NaN();
        sum += (i % 2 == 0 ? 2.0 : 4.0) * value;
    }
    return sum * step / 3.0;
}


void evaluate_stack_top(std::vector<double>& values, std::vector<std::string>& operators) {
    if (operators.empty()) return;
    std::string op = operators.back();
    operators.pop_back();
    if (op == "unary_minus") {
        if (!values.empty()) values.back() = -values.back();
        return;
    }
    if (op == "square_root") {
        if (!values.empty()) values.back() = values.back() >= 0.0
            ? std::sqrt(values.back()) : std::numeric_limits<double>::quiet_NaN();
        return;
    }
    if (op == "sin" || op == "cos" || op == "tan" || op == "asin" || op == "acos" || op == "atan" || op == "log" || op == "ln") {
        if (values.empty()) return;
        const double value = values.back();
        if (op == "sin") values.back() = std::sin(value);
        else if (op == "cos") values.back() = std::cos(value);
        else if (op == "tan") values.back() = std::tan(value);
        else if (op == "asin") values.back() = std::asin(value);
        else if (op == "acos") values.back() = std::acos(value);
        else if (op == "atan") values.back() = std::atan(value);
        else if (op == "log") values.back() = value > 0.0 ? std::log10(value) : std::numeric_limits<double>::quiet_NaN();
        else values.back() = value > 0.0 ? std::log(value) : std::numeric_limits<double>::quiet_NaN();
        return;
    }
    if (values.size() < 2) return;
    double val2 = values.back(); values.pop_back();
    double val1 = values.back(); values.pop_back();
    values.push_back(apply_operator(val1, val2, op));
}

std::complex<double> evaluate_complex_expression(
    const std::vector<std::pair<std::string, std::string>>& tokens,
    std::complex<double> x_guess, std::complex<double> y_guess) {
    using Complex = std::complex<double>;
    std::vector<Complex> values;
    std::vector<std::string> operators;
    bool expecting_operand = true;

    auto apply_top = [&]() {
        if (operators.empty()) return;
        const std::string op = operators.back();
        operators.pop_back();
        if (op == "unary_minus" || op == "square_root" || op == "sin" || op == "cos" || op == "tan" || op == "asin" || op == "acos" || op == "atan" || op == "log" || op == "ln") {
            if (values.empty()) return;
            Complex& value = values.back();
            if (op == "unary_minus") value = -value;
            else if (op == "square_root") value = std::sqrt(value);
            else if (op == "sin") value = std::sin(value);
            else if (op == "cos") value = std::cos(value);
            else if (op == "tan") value = std::tan(value);
            else if (op == "asin") value = std::asin(value);
            else if (op == "acos") value = std::acos(value);
            else if (op == "atan") value = std::atan(value);
            else if (op == "log") value = std::log(value) / std::log(Complex(10.0, 0.0));
            else value = std::log(value);
            return;
        }
        if (values.size() < 2) return;
        const Complex right = values.back(); values.pop_back();
        const Complex left = values.back(); values.pop_back();
        if (op == "plus") values.push_back(left + right);
        else if (op == "minus") values.push_back(left - right);
        else if (op == "multiply") values.push_back(left * right);
        else if (op == "divide") values.push_back(left / right);
        else if (op == "exponent") values.push_back(std::pow(left, right));
    };

    for (const auto& token : tokens) {
        const std::string& type = token.first;
        if (type == "number" || type == "variable" || type == "imaginary") {
            if (!expecting_operand) {
                while (!operators.empty() && operators.back() != "open_parentheses" &&
                       operators.back() != "open_vertical" &&
                       get_precedence(operators.back()) >= get_precedence("multiply")) apply_top();
                operators.push_back("multiply");
            }
            if (type == "number") values.emplace_back(std::stod(token.second), 0.0);
            else if (type == "imaginary") values.emplace_back(0.0, 1.0);
            else if (token.second == "y") values.push_back(y_guess);
            else if (token.second == "theta") values.push_back(x_guess);
            else values.push_back(x_guess);
            expecting_operand = false;
        } else if (type == "open_parentheses" || type == "open_vertical") {
            if (!expecting_operand) {
                while (!operators.empty() && operators.back() != "open_parentheses" &&
                       operators.back() != "open_vertical" &&
                       get_precedence(operators.back()) >= get_precedence("multiply")) apply_top();
                operators.push_back("multiply");
            }
            operators.push_back(type);
            expecting_operand = true;
        } else if (type == "close_parentheses" || type == "close_vertical") {
            const std::string opening = type == "close_vertical" ? "open_vertical" : "open_parentheses";
            while (!operators.empty() && operators.back() != opening) {
                if (operators.back() == "open_parentheses" || operators.back() == "open_vertical") break;
                apply_top();
            }
            if (!operators.empty() && operators.back() == opening) operators.pop_back();
            if (type == "close_vertical" && !values.empty()) values.back() = std::abs(values.back());
            else if (type == "close_parentheses" && !operators.empty() &&
                     (operators.back() == "square_root" || operators.back() == "sin" || operators.back() == "cos" || operators.back() == "tan" ||
                      operators.back() == "asin" || operators.back() == "acos" || operators.back() == "atan" ||
                      operators.back() == "log" || operators.back() == "ln")) apply_top();
            expecting_operand = false;
        } else if (type == "function") {
            operators.push_back(token.second);
            expecting_operand = true;
        } else if (type == "minus" && expecting_operand) {
            operators.push_back("unary_minus");
        } else if (type == "square_root") {
            operators.push_back("square_root");
        } else {
            while (!operators.empty() && operators.back() != "open_parentheses" &&
                   operators.back() != "open_vertical" &&
                   get_precedence(operators.back()) >= get_precedence(type) && type != "exponent") apply_top();
            operators.push_back(type);
            expecting_operand = true;
        }
    }
    while (!operators.empty()) {
        if (operators.back() == "open_parentheses" || operators.back() == "open_vertical") operators.pop_back();
        else if (operators.back() == "square_root") {
            operators.pop_back();
            if (!values.empty()) values.back() = std::sqrt(values.back());
        } else apply_top();
    }
    return values.empty() ? Complex(0.0, 0.0) : values.back();
}

std::string format_complex(const std::complex<double>& value) {
    const double real = std::abs(value.real()) < 1e-12 ? 0.0 : value.real();
    const double imag = std::abs(value.imag()) < 1e-12 ? 0.0 : value.imag();
    std::ostringstream out;
    out << std::setprecision(decimal_precision);
    if (imag == 0.0) out << real;
    else if (real == 0.0) out << imag << "i";
    else out << real << (imag < 0.0 ? " - " : " + ") << std::abs(imag) << "i";
    return out.str();
}

double evaluate_expression(const std::vector<std::pair<std::string, std::string>>& side_tokens, double x_guess, double y_guess) {
    if (std::any_of(side_tokens.begin(), side_tokens.end(),
                    [](const auto& token) { return token.first == "imaginary"; })) {
        const std::complex<double> result = evaluate_complex_expression(side_tokens, x_guess, y_guess);
        if (std::abs(result.imag()) > 1e-10) return std::numeric_limits<double>::quiet_NaN();
        return result.real();
    }
    std::vector<double> values;
    std::vector<std::string> operators;
    bool expecting_operand = true;

    for (const auto& entry : side_tokens) {

        if (entry.first == "number" || entry.first == "variable" || entry.first == "imaginary") {
            if (!expecting_operand) {
                while (!operators.empty() && operators.back() != "open_parentheses" &&
                       operators.back() != "open_vertical" &&
                       get_precedence(operators.back()) >= get_precedence("multiply")) {
                    evaluate_stack_top(values, operators);
                }
                operators.push_back("multiply");
            }
            if (entry.first == "number") {
                values.push_back(std::stod(entry.second));
            } else if (entry.first == "imaginary") {
                values.push_back(std::numeric_limits<double>::quiet_NaN());
            } else if (entry.second == "y") {
                values.push_back(y_guess);
            } else {
                values.push_back(x_guess);
            }
            expecting_operand = false;
        }
        else if (entry.first == "open_parentheses" || entry.first == "open_vertical") {
            if (!expecting_operand) {
                while (!operators.empty() && operators.back() != "open_parentheses" &&
                       operators.back() != "open_vertical" &&
                       get_precedence(operators.back()) >= get_precedence("multiply")) {
                    evaluate_stack_top(values, operators);
                }
                operators.push_back("multiply");
            }
            operators.push_back(entry.first);
            expecting_operand = true;
        }
        else if (entry.first == "close_parentheses" || entry.first == "close_vertical") {
            const std::string opening = entry.first == "close_vertical" ? "open_vertical" : "open_parentheses";
            while (!operators.empty() && operators.back() != opening) {
                if (operators.back() == "open_parentheses" || operators.back() == "open_vertical") break;
                evaluate_stack_top(values, operators);
            }
            if (!operators.empty() && operators.back() == opening) operators.pop_back();
            if (entry.first == "close_vertical" && !values.empty())
                values.back() = std::abs(values.back());
            else if (entry.first == "close_parentheses" && !operators.empty() &&
                     (operators.back() == "square_root" || operators.back() == "sin" || operators.back() == "cos" || operators.back() == "tan" ||
                      operators.back() == "asin" || operators.back() == "acos" || operators.back() == "atan" ||
                      operators.back() == "log" || operators.back() == "ln")) {
                evaluate_stack_top(values, operators);
            }
            expecting_operand = false;
        }
        else if (entry.first == "function") {
            if (!expecting_operand) {
                while (!operators.empty() && operators.back() != "open_parentheses" &&
                       operators.back() != "open_vertical" &&
                       get_precedence(operators.back()) >= get_precedence("multiply")) {
                    evaluate_stack_top(values, operators);
                }
                operators.push_back("multiply");
            }
            operators.push_back(entry.second);
            expecting_operand = true;
        }
        else if (entry.first == "minus" && expecting_operand) {
            operators.push_back("unary_minus");
        }
        else {
            while (!operators.empty() && operators.back() != "open_parentheses" &&
                   operators.back() != "open_vertical" &&
                   get_precedence(operators.back()) >= get_precedence(entry.first) &&
                   entry.first != "exponent") {
                evaluate_stack_top(values, operators);
            }
            operators.push_back(entry.first);
            expecting_operand = true;
        }
    }

    while (!operators.empty()) {
        if (operators.back() == "open_parentheses" || operators.back() == "open_vertical") {
            operators.pop_back();
        } else {
            evaluate_stack_top(values, operators);
        }
    }
    return values.empty() ? 0.0 : values.back();
}

void graph(
    const std::vector<std::vector<std::pair<std::string, std::string>>>& expressions,
    double range_x,
    double range_y,
    double step = 0.1,
    bool print_console = true,
    bool export_html = true) {
    std::vector<Point> points;
    std::vector<SegmentAnnotation> segment_annotations;
    struct PolygonAngleAnnotation {
        double x;
        double y;
        double angle;
        size_t vertex;
    };
    std::vector<PolygonAngleAnnotation> polygon_angle_annotations;
    int layer = 0;

    auto coordinates = [](int index, int count, double range) {
        return -range + (2.0 * range * index / count);
    };

    if (is_automatic && given_points.size() >= 2) {
        for (size_t i = 0; i + 1 < given_points.size(); ++i) {
            drawing_primitives.push_back({"seg", given_points[i], given_points[i + 1]});
        }
        if (given_points.size() >= 3)
            drawing_primitives.push_back({"seg", given_points.back(), given_points.front()});
    }
    if (is_automatic && given_points.size() >= 3) {
        double twice_area = 0.0;
        for (size_t i = 0; i < given_points.size(); ++i) {
            const auto& current = given_points[i];
            const auto& next = given_points[(i + 1) % given_points.size()];
            twice_area += current.first * next.second - next.first * current.second;
        }
        const double orientation = twice_area >= 0.0 ? 1.0 : -1.0;
        for (size_t i = 0; i < given_points.size(); ++i) {
            const auto& previous = given_points[(i + given_points.size() - 1) % given_points.size()];
            const auto& current = given_points[i];
            const auto& next = given_points[(i + 1) % given_points.size()];
            const double in_x = current.first - previous.first;
            const double in_y = current.second - previous.second;
            const double out_x = next.first - current.first;
            const double out_y = next.second - current.second;
            const double turn = std::atan2(in_x * out_y - in_y * out_x, in_x * out_x + in_y * out_y);
            const double interior = std::acos(-1.0) - orientation * turn;
            polygon_angle_annotations.push_back({current.first, current.second,
                interior * 180.0 / std::acos(-1.0), i});
        }
    }

    std::vector<std::vector<std::pair<double, double>>> segment_points;

    for (const DrawingPrimitive& primitive : drawing_primitives) {
        double origin_x = primitive.first.first;
        double origin_y = primitive.first.second;
        double dx = primitive.second.first - origin_x;
        double dy = primitive.second.second - origin_y;

        const double length = std::hypot(dx, dy);
        if (primitive.type == "seg") {
            segment_annotations.push_back({
                (primitive.first.first + primitive.second.first) / 2.0,
                (primitive.first.second + primitive.second.second) / 2.0,
                length
            });
        }
        if (length == 0.0) {
            if (origin_x >= -range_x && origin_x <= range_x &&
                origin_y >= -range_y && origin_y <= range_y)
                points.push_back({origin_x, origin_y, false, true, true, layer});
            continue;
        }

        // Clip the segment or ray to the visible rectangle before sampling it.
        const double unit_x = dx / length, unit_y = dy / length;
        double first_distance = 0.0;
        double last_distance = primitive.type == "seg"
            ? length : std::numeric_limits<double>::infinity();
        auto clip_axis = [&](double origin, double direction, double minimum, double maximum) {
            if (std::abs(direction) < 1e-12)
                return origin >= minimum && origin <= maximum;
            const double first = (minimum - origin) / direction;
            const double second = (maximum - origin) / direction;
            first_distance = std::max(first_distance, std::min(first, second));
            last_distance = std::min(last_distance, std::max(first, second));
            return first_distance <= last_distance;
        };
        if (!clip_axis(origin_x, unit_x, -range_x, range_x) ||
            !clip_axis(origin_y, unit_y, -range_y, range_y) ||
            last_distance < first_distance) continue;

        const double distance_step = std::max(step / 2.0, 0.01);
        const int samples = std::max(1, static_cast<int>(std::ceil(
            (last_distance - first_distance) / distance_step)));
        for (int sample = 0; sample <= samples; ++sample) {
            const double distance = first_distance +
                (last_distance - first_distance) * sample / samples;
            points.push_back({origin_x + unit_x * distance,
                              origin_y + unit_y * distance,
                              false, true, true, layer});
        }
    }

    if (has_polar) {
        const double max_theta = theta_count * 2.0 * pi;
        const int samples = std::max(1, static_cast<int>(std::ceil(720.0 * theta_count)));

        for (const auto& expression : expressions) {
            auto polar_marker = std::find_if(expression.begin(), expression.end(),
                [](const auto& token) { return token.first == "polar"; });
            if (polar_marker == expression.end()) continue;

            std::vector<std::pair<std::string, std::string>> radius_expression(
                polar_marker + 1, expression.end());
            for (int sample = 0; sample <= samples; ++sample) {
                const double theta = max_theta * sample / samples;
                const double radius = evaluate_expression(radius_expression, theta, 0.0);
                if (!std::isfinite(radius)) continue;
                const double x = radius * std::cos(theta);
                const double y = radius * std::sin(theta);
                if (std::isfinite(x) && std::isfinite(y))
                    points.push_back({x, y, false, true, true, layer});
            }
            ++layer;
        }
    }

    if (has_fib) {
        struct FibonacciSquare {
            double x;
            double y;
            double size;
        };
        std::vector<FibonacciSquare> squares;
        double first = 1.0, second = 1.0;
        double min_x = 0.0, min_y = 0.0, max_x = 1.0, max_y = 1.0;
        squares.push_back({0.0, 0.0, 1.0});

        for (int index = 1; index < 40; ++index) {
            const double size = index == 1 ? 1.0 : first + second;
            if (index > 1) {
                first = second;
                second = size;
            }
            double x = 0.0, y = 0.0;
            switch ((index - 1) % 4) {
                case 0: x = max_x; y = min_y; break;
                case 1: x = min_x; y = max_y; break;
                case 2: x = min_x - size; y = min_y; break;
                default: x = min_x; y = min_y - size; break;
            }
            const double next_min_x = std::min(min_x, x);
            const double next_min_y = std::min(min_y, y);
            const double next_max_x = std::max(max_x, x + size);
            const double next_max_y = std::max(max_y, y + size);
            if (next_max_x - next_min_x > 2.0 * range_x ||
                next_max_y - next_min_y > 2.0 * range_y) break;
            squares.push_back({x, y, size});
            min_x = next_min_x; min_y = next_min_y;
            max_x = next_max_x; max_y = next_max_y;
        }

        const double center_x = (min_x + max_x) / 2.0;
        const double center_y = (min_y + max_y) / 2.0;
        for (size_t index = 0; index < squares.size(); ++index) {
            const FibonacciSquare& square = squares[index];
            const double left = square.x - center_x;
            const double bottom = square.y - center_y;
            const double size = square.size;
            double center_arc_x = left, center_arc_y = bottom;
            double start_angle = 0.0;
            switch (index % 4) {
                case 0: center_arc_x = left;        center_arc_y = bottom;        start_angle = 0.0; break;
                case 1: center_arc_x = left + size;  center_arc_y = bottom;        start_angle = 90.0; break;
                case 2: center_arc_x = left + size;  center_arc_y = bottom + size; start_angle = 180.0; break;
                default:center_arc_x = left;        center_arc_y = bottom + size; start_angle = 270.0; break;
            }
            const int arc_samples = std::max(12, static_cast<int>(std::ceil(90.0 * size / std::max(step, 0.01))));
            for (int sample = 0; sample <= arc_samples; ++sample) {
                const double angle = (start_angle + 90.0 * sample / arc_samples) * pi / 180.0;
                const double x = center_arc_x + size * std::cos(angle);
                const double y = center_arc_y + size * std::sin(angle);
                points.push_back({x, y, false, true, true, layer});
            }
        }

        range_x = std::max(1.0, (max_x - min_x) * 0.55);
        range_y = std::max(1.0, (max_y - min_y) * 0.55);
    }

    for (const auto& expression : expressions) {
        if (std::any_of(expression.begin(), expression.end(),
                [](const auto& token) { return token.first == "polar"; })) continue;
        relational_operator = "equals";
        std::vector<std::pair<std::string, std::string>> left_side;
        std::vector<std::pair<std::string, std::string>> right_side;
        bool found_relation = false;
        for (const auto& token : expression) {
            if (token.first == "equals" || token.first == "less_than" ||
                token.first == "greater_than" || token.first == "less_equal" ||
                token.first == "greater_equal") {
                relational_operator = token.first;
                found_relation = true;
            } else if (found_relation) {
                right_side.push_back(token);
            } else {
                left_side.push_back(token);
            }
        }

        const bool left_is_y = left_side.size() == 1 && left_side[0].first == "variable" && left_side[0].second == "y";
        const bool right_is_y = right_side.size() == 1 && right_side[0].first == "variable" && right_side[0].second == "y";
        if (!found_relation || left_is_y || right_is_y) {
            auto function = !found_relation ? expression : (left_is_y ? right_side : left_side);
            if (right_is_y) {
                if (relational_operator == "less_than") relational_operator = "greater_than";
                else if (relational_operator == "greater_than") relational_operator = "less_than";
                else if (relational_operator == "less_equal") relational_operator = "greater_equal";
                else if (relational_operator == "greater_equal") relational_operator = "less_equal";
            }
            const bool inequality = relational_operator == "less_than" || relational_operator == "greater_than" ||
                relational_operator == "less_equal" || relational_operator == "greater_equal";
            const bool solid = !inequality || relational_operator == "less_equal" || relational_operator == "greater_equal";
            for (double x = -range_x; x <= range_x + step / 2; x += step) {
                const double boundary_y = evaluate_expression(function, x, 0.0);
                if (!std::isfinite(boundary_y)) continue;
                if (!inequality) {
                    if (boundary_y >= -range_y && boundary_y <= range_y)
                        points.push_back({x, boundary_y, false, true, true, layer});
                } else {
                    for (double y = -range_y; y <= range_y + step / 2; y += step) {
                        const bool shaded = check_inequality(y, boundary_y, relational_operator);
                        const bool boundary = std::abs(y - boundary_y) <= step / 2;
                        if (shaded || boundary)
                            points.push_back({x, y, shaded, boundary, solid, layer});
                    }
                }
            }
        } else {
            const int columns = static_cast<int>(std::ceil(2.0 * range_x / step));
            const int rows = static_cast<int>(std::ceil(2.0 * range_y / step));
            const bool inequality = relational_operator == "less_than" || relational_operator == "greater_than" ||
                relational_operator == "less_equal" || relational_operator == "greater_equal";
            const bool solid = relational_operator == "equals" || relational_operator == "less_equal" ||
                relational_operator == "greater_equal";
            std::vector<std::vector<double>> residuals(rows + 1, std::vector<double>(columns + 1));
            std::vector<std::vector<bool>> valid(rows + 1, std::vector<bool>(columns + 1, false));
            auto residual = [&](double x, double y) {
                return evaluate_expression(left_side, x, y) - evaluate_expression(right_side, x, y);
            };
            for (int row = 0; row <= rows; ++row) {
                const double y = coordinates(row, rows, range_y);
                for (int column = 0; column <= columns; ++column) {
                    const double x = coordinates(column, columns, range_x);
                    const double value = residual(x, y);
                    if (!std::isfinite(value)) continue;
                    residuals[row][column] = value;
                    valid[row][column] = true;
                    if (inequality && check_inequality(value, 0.0, relational_operator))
                        points.push_back({x, y, true, false, solid, layer});
                    if (std::abs(value) < 1e-10){
                        points.push_back({x, y, false, true, solid, layer});
                    }
                        }
            }
            auto add_crossing = [&](int r1, int c1, int r2, int c2) {
                if (!valid[r1][c1] || !valid[r2][c2]) return;
                
                const double first = residuals[r1][c1], second = residuals[r2][c2];
                if ((first < 0 && second > 0) || (first > 0 && second < 0)) {
                    const double fraction = first / (first - second);
                    const double x1 = coordinates(c1, columns, range_x), x2 = coordinates(c2, columns, range_x);
                    const double y1 = coordinates(r1, rows, range_y), y2 = coordinates(r2, rows, range_y);
                    points.push_back({x1 + fraction * (x2 - x1), y1 + fraction * (y2 - y1), false, true, solid, layer});
                }
            };

            for (int row = 0; row < rows; ++row)
                for (int column = 0; column < columns; ++column) {
                    add_crossing(row, column, row, column + 1);
                    add_crossing(row, column, row + 1, column);
                }
            for (int column = 0; column < columns; ++column) add_crossing(rows, column, rows, column + 1);
            for (int row = 0; row < rows; ++row) add_crossing(row, columns, row + 1, columns);
        }
        ++layer;
    }

    for (const auto& point : given_points) {
        points.push_back({point.first, point.second, false, true, true, layer, true});
    }

    struct CurveEquation {
        std::vector<std::pair<std::string, std::string>> left;
        std::vector<std::pair<std::string, std::string>> right;
        bool explicit_y = false;
    };
    std::vector<CurveEquation> curves;
    for (const auto& expression : expressions) {
        if (std::any_of(expression.begin(), expression.end(),
                [](const auto& token) { return token.first == "polar"; })) continue;
        CurveEquation curve;
        bool found_relation = false;
        bool equality = false;
        for (const auto& token : expression) {
            if (token.first == "equals" || token.first == "less_than" ||
                token.first == "greater_than" || token.first == "less_equal" ||
                token.first == "greater_equal") {
                found_relation = true;
                equality = token.first == "equals";
            } else if (found_relation) {
                curve.right.push_back(token);
            } else {
                curve.left.push_back(token);
            }
        }
        if (found_relation && !equality) continue;
        if (!found_relation) {
            curve.right = curve.left;
            curve.left.clear();
            curve.explicit_y = true;
        } else if (curve.left.size() == 1 && curve.left[0].first == "variable" && curve.left[0].second == "y") {
            curve.explicit_y = true;
        } else if (curve.right.size() == 1 && curve.right[0].first == "variable" && curve.right[0].second == "y") {
            curve.left.swap(curve.right);
            curve.explicit_y = true;
        }
        curves.push_back(std::move(curve));
    }

    auto curve_value = [](const CurveEquation& curve, double x, double y) {
        if (curve.explicit_y) return y - evaluate_expression(curve.right, x, y);
        return evaluate_expression(curve.left, x, y) - evaluate_expression(curve.right, x, y);
    };
    std::vector<std::tuple<double, double, double, int, int>> intersection_angles;
    const double seed_step = std::max(1.0, step * 10.0);
    for (size_t first_curve = 0; first_curve < curves.size(); ++first_curve) {
        for (size_t second_curve = first_curve + 1; second_curve < curves.size(); ++second_curve) {
            auto f = [&](double x, double y) { return curve_value(curves[first_curve], x, y); };
            auto g = [&](double x, double y) { return curve_value(curves[second_curve], x, y); };
            for (double start_y = -range_y; start_y <= range_y + seed_step / 2; start_y += seed_step) {
                for (double start_x = -range_x; start_x <= range_x + seed_step / 2; start_x += seed_step) {
                    double x = start_x, y = start_y;
                    for (int iteration = 0; iteration < 40; ++iteration) {
                        const double fv = f(x, y), gv = g(x, y);
                        if (!std::isfinite(fv) || !std::isfinite(gv)) break;
                        if (std::max(std::abs(fv), std::abs(gv)) < 1e-8) break;
                        const double hx = 1e-5 * (1.0 + std::abs(x));
                        const double hy = 1e-5 * (1.0 + std::abs(y));
                        const double fx = (f(x + hx, y) - f(x - hx, y)) / (2.0 * hx);
                        const double fy = (f(x, y + hy) - f(x, y - hy)) / (2.0 * hy);
                        const double gx = (g(x + hx, y) - g(x - hx, y)) / (2.0 * hx);
                        const double gy = (g(x, y + hy) - g(x, y - hy)) / (2.0 * hy);
                        const double determinant = fx * gy - fy * gx;
                        if (!std::isfinite(determinant) || std::abs(determinant) < 1e-12) break;
                        const double dx = (-fv * gy + fy * gv) / determinant;
                        const double dy = (-fx * gv + fv * gx) / determinant;
                        const double old_error = std::abs(fv) + std::abs(gv);
                        bool improved = false;
                        for (double scale = 1.0; scale >= 1.0 / 64.0; scale /= 2.0) {
                            const double next_x = x + scale * dx;
                            const double next_y = y + scale * dy;
                            if (!std::isfinite(next_x) || !std::isfinite(next_y) ||
                                std::abs(next_x) > range_x || std::abs(next_y) > range_y) continue;
                            const double next_error = std::abs(f(next_x, next_y)) + std::abs(g(next_x, next_y));
                            if (std::isfinite(next_error) && next_error < old_error) {
                                x = next_x;
                                y = next_y;
                                improved = true;
                                break;
                            }
                        }
                        if (!improved) break;
                    }
                    const double fv = f(x, y), gv = g(x, y);
                    if (!std::isfinite(fv) || !std::isfinite(gv) ||
                        std::max(std::abs(fv), std::abs(gv)) >= 1e-7) continue;
                    bool duplicate = false;
                    for (const auto& intersection : intersection_angles) {
                        if (std::get<3>(intersection) == static_cast<int>(first_curve) &&
                            std::get<4>(intersection) == static_cast<int>(second_curve) &&
                            std::hypot(std::get<0>(intersection) - x, std::get<1>(intersection) - y) < 1e-4) {
                            duplicate = true;
                            break;
                        }
                    }
                    if (duplicate) continue;
                    const double hx = 1e-5 * (1.0 + std::abs(x));
                    const double hy = 1e-5 * (1.0 + std::abs(y));
                    const double fx = (f(x + hx, y) - f(x - hx, y)) / (2.0 * hx);
                    const double fy = (f(x, y + hy) - f(x, y - hy)) / (2.0 * hy);
                    const double gx = (g(x + hx, y) - g(x - hx, y)) / (2.0 * hx);
                    const double gy = (g(x, y + hy) - g(x, y - hy)) / (2.0 * hy);
                    const double angle = std::atan2(std::abs(fx * gy - fy * gx), std::abs(fx * gx + fy * gy)) * 180.0 / std::acos(-1.0);
                    if (std::isfinite(angle))
                        intersection_angles.push_back({x, y, angle, static_cast<int>(first_curve), static_cast<int>(second_curve)});
                }
            }
        }
    }

    // Also measure intersections between equality curves and finite segments.
    for (size_t curve_index = 0; curve_index < curves.size(); ++curve_index) {
        auto curve = [&](double x, double y) { return curve_value(curves[curve_index], x, y); };
        for (size_t segment_index = 0; segment_index < drawing_primitives.size(); ++segment_index) {
            const DrawingPrimitive& primitive = drawing_primitives[segment_index];
            if (primitive.type != "seg") continue;
            const double x1 = primitive.first.first, y1 = primitive.first.second;
            const double dx = primitive.second.first - x1, dy = primitive.second.second - y1;
            const double length = std::hypot(dx, dy);
            if (length == 0.0) continue;
            const int samples = std::max(1, static_cast<int>(std::ceil(length / std::max(step, 0.01))));
            double previous_t = 0.0;
            double previous_value = curve(x1, y1);
            for (int sample = 1; sample <= samples; ++sample) {
                const double t = static_cast<double>(sample) / samples;
                const double current_value = curve(x1 + t * dx, y1 + t * dy);
                if (std::isfinite(previous_value) && std::isfinite(current_value) &&
                    (previous_value == 0.0 || current_value == 0.0 ||
                     ((previous_value < 0.0) != (current_value < 0.0)))) {
                    double low = previous_t, high = t;
                    double low_value = previous_value;
                    if (previous_value == 0.0) {
                        low = high = previous_t;
                    } else if (current_value == 0.0) {
                        low = high = t;
                    } else {
                        for (int iteration = 0; iteration < 50; ++iteration) {
                            const double middle = (low + high) / 2.0;
                            const double middle_value = curve(x1 + middle * dx, y1 + middle * dy);
                            if (!std::isfinite(middle_value)) break;
                            if (std::abs(middle_value) < 1e-10) {
                                low = high = middle;
                                break;
                            }
                            if ((low_value < 0.0) != (middle_value < 0.0)) {
                                high = middle;
                            } else {
                                low = middle;
                                low_value = middle_value;
                            }
                        }
                    }
                    const double root_t = (low + high) / 2.0;
                    const double x = x1 + root_t * dx, y = y1 + root_t * dy;
                    const double hx = 1e-5 * (1.0 + std::abs(x));
                    const double hy = 1e-5 * (1.0 + std::abs(y));
                    const double fx = (curve(x + hx, y) - curve(x - hx, y)) / (2.0 * hx);
                    const double fy = (curve(x, y + hy) - curve(x, y - hy)) / (2.0 * hy);
                    const double angle = std::atan2(std::abs(fx * dx + fy * dy),
                                                    std::abs(fx * dy - fy * dx)) * 180.0 / std::acos(-1.0);
                    const int encoded_segment = static_cast<int>(curves.size() + segment_index);
                    bool duplicate = false;
                    for (const auto& intersection : intersection_angles) {
                        if (std::get<3>(intersection) == static_cast<int>(curve_index) &&
                            std::get<4>(intersection) == encoded_segment &&
                            std::hypot(std::get<0>(intersection) - x, std::get<1>(intersection) - y) < 1e-4) {
                            duplicate = true;
                            break;
                        }
                    }
                    if (!duplicate && std::isfinite(angle))
                        intersection_angles.push_back({x, y, angle, static_cast<int>(curve_index), encoded_segment});
                }
                previous_t = t;
                previous_value = current_value;
            }
        }
    }

    if (print_console) {
        const int width = 61, height = 21;
        std::vector<std::string> grid(height, std::string(width, ' '));
        std::vector<std::vector<std::vector<int>>> shade_layers(height, std::vector<std::vector<int>>(width));
        struct ConsoleLabel { int row; int column; int width; std::string text; };
        std::vector<ConsoleLabel> console_labels;
        std::vector<std::vector<bool>> label_cells(height, std::vector<bool>(width, false));
        auto add_console_label = [&](double x, double y, const std::string& text) {
            int display_width = 0;
            for (unsigned char character : text)
                if ((character & 0xC0) != 0x80) ++display_width;
            const int center_column = static_cast<int>(std::lround(
                (x + range_x) * (width - 1) / (2.0 * range_x)));
            const int center_row = static_cast<int>(std::lround(
                (range_y - y) * (height - 1) / (2.0 * range_y)));

            int best_row = -1, best_column = -1;
            double best_score = std::numeric_limits<double>::infinity();
            for (int row = 0; row < height; ++row) {
                const int vertical_distance = std::abs(row - center_row);
                for (int start_column = 1; start_column + display_width < width; ++start_column) {
                    bool available = true;
                    for (int column = start_column - 1; column <= start_column + display_width; ++column) {
                        if (grid[row][column] != ' ' || label_cells[row][column]) {
                            available = false;
                            break;
                        }
                    }
                    if (!available) continue;

                    int labels_on_row = 0;
                    for (const ConsoleLabel& label : console_labels)
                        if (label.row == row) ++labels_on_row;
                    const double horizontal_distance = std::abs(
                        start_column + display_width / 2.0 - center_column);
                    const double score = vertical_distance * 2.0 + horizontal_distance * 0.1 +
                                         labels_on_row * 5.0;
                    if (score < best_score) {
                        best_score = score;
                        best_row = row;
                        best_column = start_column;
                    }
                }
            }
            if (best_row < 0) return;

            console_labels.push_back({best_row, best_column, display_width, text});
            for (int column = best_column - 1; column <= best_column + display_width; ++column)
                label_cells[best_row][column] = true;
        };
        auto add_console_label_at = [&](int target_row, int target_column, const std::string& text) {
            int display_width = 0;
            for (unsigned char character : text)
                if ((character & 0xC0) != 0x80) ++display_width;

            for (int row_offset : {0, -1, 1}) {
                const int row = target_row + row_offset;
                if (row < 0 || row >= height) continue;
                for (int distance = 0; distance <= 8; ++distance) {
                    for (int direction : {0, -1, 1}) {
                        if (distance == 0 && direction != 0) continue;
                        const int start_column = target_column - display_width / 2 + direction * distance;
                        if (start_column < 1 || start_column + display_width >= width) continue;
                        bool available = true;
                        for (int column = start_column - 1; column <= start_column + display_width; ++column) {
                            if (grid[row][column] != ' ' || label_cells[row][column]) {
                                available = false;
                                break;
                            }
                        }
                        if (!available) continue;
                        console_labels.push_back({row, start_column, display_width, text});
                        for (int column = start_column - 1; column <= start_column + display_width; ++column)
                            label_cells[row][column] = true;
                        return;
                    }
                }
            }
            add_console_label(target_column * (2.0 * range_x) / (width - 1) - range_x,
                              range_y - target_row * (2.0 * range_y) / (height - 1), text);
        };
        const int x_axis = width / 2, y_axis = height / 2;
        for (int row = 0; row < height; ++row) grid[row][x_axis] = '|';
        for (int column = 0; column < width; ++column) grid[y_axis][column] = '-';
        grid[y_axis][x_axis] = '+';
        auto add_axis_label = [&](int row, int center_column, const std::string& text) {
            const int start_column = center_column - static_cast<int>(text.size()) / 2;
            if (row < 0 || row >= height || start_column < 0 ||
                start_column + static_cast<int>(text.size()) > width) return;
            console_labels.push_back({row, start_column, static_cast<int>(text.size()), text});
            for (int column = start_column; column < start_column + static_cast<int>(text.size()); ++column)
                label_cells[row][column] = true;
        };
        const int tick_step_x = std::max(1, static_cast<int>(std::ceil(range_x / 5.0)));
        const int tick_step_y = std::max(1, static_cast<int>(std::ceil(range_y / 5.0)));
        for (int tick = -static_cast<int>(range_x); tick <= static_cast<int>(range_x); ++tick) {
            if (tick % tick_step_x != 0 || tick == 0 || std::abs(tick) > range_x) continue;
            const int column = static_cast<int>(std::lround((tick + range_x) * (width - 1) / (2.0 * range_x)));
            add_axis_label(y_axis + 1, column, std::to_string(tick));
        }
        for (int tick = -static_cast<int>(range_y); tick <= static_cast<int>(range_y); ++tick) {
            if (tick % tick_step_y != 0 || std::abs(tick) > range_y) continue;
            const int row = static_cast<int>(std::lround((range_y - tick) * (height - 1) / (2.0 * range_y)));
            add_axis_label(row, x_axis - 4, std::to_string(tick));
        }
        for (const Point& point : points) {
            if (!std::isfinite(point.x) || !std::isfinite(point.y) || point.x < -range_x || point.x > range_x ||
                point.y < -range_y || point.y > range_y) continue;
            const int column = static_cast<int>(std::lround((point.x + range_x) * (width - 1) / (2.0 * range_x)));
            const int row = static_cast<int>(std::lround((range_y - point.y) * (height - 1) / (2.0 * range_y)));
            if (row < 0 || row >= height || column < 0 || column >= width) continue;
            if (point.is_point) {
                grid[row][column] = 'P';
            } else if (point.is_boundary) {
                if (point.solid_boundary) grid[row][column] = '*';
                else if ((column + row) % 2 == 0) grid[row][column] = '.';
            } else if (point.is_shaded) {
                auto& shades = shade_layers[row][column];
                if (std::find(shades.begin(), shades.end(), point.layer) == shades.end()) shades.push_back(point.layer);
            }
        }
        for (int row = 0; row < height; ++row)
            for (int column = 0; column < width; ++column)
                if (grid[row][column] == ' ' && !shade_layers[row][column].empty()) {
                    const size_t count = shade_layers[row][column].size();
                    grid[row][column] = count == 1 ? '#' : count == 2 ? '@' : '%';
                }
        if (prints_angles) {
            for (const auto& intersection : intersection_angles) {
                const double acute_angle = std::get<2>(intersection);
                const double obtuse_angle = 180.0 - acute_angle;
                std::ostringstream acute_label, obtuse_label;
                acute_label << std::fixed << std::setprecision(0) << acute_angle << "°";
                obtuse_label << std::fixed << std::setprecision(0) << obtuse_angle << "°";

                const int center_column = static_cast<int>(std::lround(
                    (std::get<0>(intersection) + range_x) * (width - 1) / (2.0 * range_x)));
                const int center_row = static_cast<int>(std::lround(
                    (range_y - std::get<1>(intersection)) * (height - 1) / (2.0 * range_y)));
                // Spread the four angle measures into a compact 2-by-2 layout around the crossing.
                add_console_label_at(center_row - 2, center_column - 5, acute_label.str());
                add_console_label_at(center_row - 2, center_column + 5, obtuse_label.str());
                add_console_label_at(center_row + 2, center_column - 5, acute_label.str());
                add_console_label_at(center_row + 2, center_column + 5, obtuse_label.str());
            }
            for (const PolygonAngleAnnotation& annotation : polygon_angle_annotations) {
                if (annotation.x < -range_x || annotation.x > range_x ||
                    annotation.y < -range_y || annotation.y > range_y) continue;
                std::ostringstream label;
                label << std::fixed << std::setprecision(0) << annotation.angle << "°";
                add_console_label(annotation.x, annotation.y, label.str());
            }
            for (const SegmentAnnotation& annotation : segment_annotations) {
                if (annotation.x < -range_x || annotation.x > range_x ||
                    annotation.y < -range_y || annotation.y > range_y) continue;
                std::ostringstream label;
                label << std::fixed << std::setprecision(2) << annotation.length;
                add_console_label(annotation.x, annotation.y, label.str());
            }
        }
        std::cout << "\nGraph (x: -" << range_x << " to " << range_x << ", y: -" << range_y << " to " << range_y << ")\n";
        for (int row = 0; row < height; ++row) {
            for (int column = 0; column < width;) {
                auto label = std::find_if(console_labels.begin(), console_labels.end(),
                    [&](const ConsoleLabel& item) { return item.row == row && item.column == column; });
                if (label != console_labels.end()) {
                    std::cout << label->text;
                    column += label->width;
                } else {
                    std::cout << grid[row][column++];
                }
            }
            std::cout << '\n';
        }
        std::cout << "* marks equation curves, P marks input points, and #, @, % show increasing overlap in inequalities.\n";
        if (is_automatic && given_points.size() >= 3 && prints_angles) {
            std::cout << "Auto polygon measurements (interior angles):\n";
            for (size_t i = 0; i < given_points.size(); ++i) {
                const size_t next = (i + 1) % given_points.size();
                const double side_length = std::hypot(given_points[next].first - given_points[i].first,
                                                      given_points[next].second - given_points[i].second);
                if (prints_angles == true) {
                   std::cout << "Side P" << i + 1 << "-P" << next + 1 << ": "
                              << std::fixed << std::setprecision(2) << side_length
                              << " | Angle at P" << i + 1 << ": "
                              << std::setprecision(2) << polygon_angle_annotations[i].angle << " degrees\n";
                }
            }
        }
        if (!intersection_angles.empty()) {
            if (prints_angles == true) {
                std::cout << "Intersection angles (four around each crossing):\n";
                for (const auto& intersection : intersection_angles) {
                    const int first_curve = std::get<3>(intersection);
                    const int second_item = std::get<4>(intersection);
                    std::cout << "Curve " << first_curve + 1 << " and ";
                    if (second_item >= static_cast<int>(curves.size()))
                        std::cout << "segment " << second_item - static_cast<int>(curves.size()) + 1;
                    else
                        std::cout << "curve " << second_item + 1;
                    const double acute_angle = std::get<2>(intersection);
                    const double obtuse_angle = 180.0 - acute_angle;
                    std::cout << " at (" << std::get<0>(intersection) << ", " << std::get<1>(intersection)
                            << "): " << std::fixed << std::setprecision(2)
                            << acute_angle << "°, " << obtuse_angle << "°, "
                            << acute_angle << "°, " << obtuse_angle << "°\n";
                }
            }
        } else if (curves.size() > 1) {
            std::cout << "No curve intersections found in the displayed range.\n";
        }
    }

    if (export_html) {
        std::ofstream file("graph.html");
        if (!file.is_open()) {
            std::cout << "Error: Could not generate graphing file.\n";
            return;
        }
        file << "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Graph</title>\n"
             << "<style>body{font-family:sans-serif;background:#f5f6f8;display:flex;justify-content:center;padding:30px}"
                ".container{width:760px;background:#fff;padding:20px;border-radius:12px;box-shadow:0 4px 12px #0002}"
                "canvas{width:100%;height:500px;border:1px solid #ddd}</style></head><body>\n"
             << "<div class='container'><h2>Algebra Graph</h2><canvas id='graph' width='720' height='500'></canvas>"
                "<p>Overlapping inequality regions blend into darker shades.</p></div><script>\nconst points=[\n";
        for (size_t i = 0; i < points.size(); ++i) {
            const Point& p = points[i];
            file << "{x:" << p.x << ",y:" << p.y << ",shade:" << (p.is_shaded ? "true" : "false")
                 << ",boundary:" << (p.is_boundary ? "true" : "false") << ",solid:" << (p.solid_boundary ? "true" : "false")
                 << ",layer:" << p.layer << ",point:" << (p.is_point ? "true" : "false")
                 << "}" << (i + 1 < points.size() ? ",\n" : "\n");
        }
        file << "];\nconst canvas=document.getElementById('graph'),ctx=canvas.getContext('2d');\n"
             << "const xmin=-" << range_x << ",xmax=" << range_x << ",ymin=-" << range_y << ",ymax=" << range_y << ";\n"
             << "const X=x=>(x-xmin)*canvas.width/(xmax-xmin),Y=y=>(ymax-y)*canvas.height/(ymax-ymin);\n"
                "ctx.fillStyle='#fff';ctx.fillRect(0,0,canvas.width,canvas.height);ctx.strokeStyle='#ddd';ctx.lineWidth=1;\n"
                "for(let x=Math.ceil(xmin);x<=xmax;x++){ctx.beginPath();ctx.moveTo(X(x),0);ctx.lineTo(X(x),canvas.height);ctx.stroke()}\n"
                "for(let y=Math.ceil(ymin);y<=ymax;y++){ctx.beginPath();ctx.moveTo(0,Y(y));ctx.lineTo(canvas.width,Y(y));ctx.stroke()}\n"
                "ctx.strokeStyle='#555';ctx.lineWidth=2;if(xmin<=0&&xmax>=0){ctx.beginPath();ctx.moveTo(X(0),0);ctx.lineTo(X(0),canvas.height);ctx.stroke()}"
                "if(ymin<=0&&ymax>=0){ctx.beginPath();ctx.moveTo(0,Y(0));ctx.lineTo(canvas.width,Y(0));ctx.stroke()}\n"
                "const dx=0.1,dy=0.1;for(const p of points){if(p.shade){ctx.fillStyle='hsla('+((p.layer*67)%360)+',75%,48%,0.22)';ctx.fillRect(X(p.x)-dx*canvas.width/(xmax-xmin)/2,Y(p.y)-dy*canvas.height/(ymax-ymin)/2,dx*canvas.width/(xmax-xmin)+1,dy*canvas.height/(ymax-ymin)+1)}}\n"
                "for(const p of points){if(p.point||p.boundary){ctx.fillStyle=p.point?'#e53935':(p.solid?'#0078d7':'#777');ctx.beginPath();ctx.arc(X(p.x),Y(p.y),p.point?4:(p.solid?2:1.5),0,2*Math.PI);ctx.fill()}}\n"
                "ctx.fillStyle='#222';ctx.font='12px sans-serif';ctx.textAlign='center';\n";
        if (prints_angles) {
            for (const SegmentAnnotation& annotation : segment_annotations) {
                file << "ctx.fillText('" << std::fixed << std::setprecision(2) << annotation.length
                     << "',X(" << annotation.x << "),Y(" << annotation.y + 0.5 << "));\n";
            }
            for (const PolygonAngleAnnotation& annotation : polygon_angle_annotations) {
                file << "ctx.fillText('" << std::fixed << std::setprecision(0) << annotation.angle << "°',X("
                     << annotation.x << "),Y(" << annotation.y << "));\n";
            }
        }
        file << "</script></body></html>\n";
    }
}

std::vector<std::complex<double>> find_complex_roots(
    const std::vector<std::pair<std::string, std::string>>& left_side,
    const std::vector<std::pair<std::string, std::string>>& right_side) {
    using Complex = std::complex<double>;
    std::vector<Complex> roots;
    auto residual = [&](Complex value) {
        const Complex x = algebra_variable == "y" ? Complex(0.0, 0.0) : value;
        const Complex y = algebra_variable == "y" ? value : Complex(0.0, 0.0);
        return evaluate_complex_expression(left_side, x, y) -
               evaluate_complex_expression(right_side, x, y);
    };

    const double seeds[] = {-10.0, -5.0, -2.0, -1.0, 0.0, 1.0, 2.0, 5.0, 10.0};
    for (double real_seed : seeds) {
        for (double imag_seed : seeds) {
            Complex value(real_seed, imag_seed);
            for (int iteration = 0; iteration < 100; ++iteration) {
                const Complex error = residual(value);
                if (!std::isfinite(error.real()) || !std::isfinite(error.imag())) break;
                if (std::abs(error) < 1e-9) break;

                const double h = 1e-6 * (1.0 + std::abs(value));
                const Complex derivative = (residual(value + h) - residual(value - h)) / (2.0 * h);
                if (!std::isfinite(derivative.real()) || !std::isfinite(derivative.imag()) ||
                    std::abs(derivative) < 1e-12) break;
                const Complex change = error / derivative;
                bool improved = false;
                for (double scale = 1.0; scale >= 1.0 / 64.0; scale /= 2.0) {
                    const Complex next = value - scale * change;
                    if (!std::isfinite(next.real()) || !std::isfinite(next.imag()) ||
                        std::abs(next) > 1e6) continue;
                    const Complex next_error = residual(next);
                    if (std::isfinite(next_error.real()) && std::isfinite(next_error.imag()) &&
                        std::abs(next_error) < std::abs(error)) {
                        value = next;
                        improved = true;
                        break;
                    }
                }
                if (!improved) break;
            }

            const Complex error = residual(value);
            if (!std::isfinite(error.real()) || !std::isfinite(error.imag()) ||
                std::abs(error) >= 1e-7) continue;
            bool duplicate = false;
            for (const Complex& root : roots) {
                if (std::abs(root - value) < 1e-5) {
                    duplicate = true;
                    break;
                }
            }
            if (!duplicate) roots.push_back(value);
        }
    }
    std::sort(roots.begin(), roots.end(), [](const Complex& a, const Complex& b) {
        return a.real() == b.real() ? a.imag() < b.imag() : a.real() < b.real();
    });
    return roots;
}

std::vector<double> find_roots(const std::vector<std::pair<std::string, std::string>>& left_side, const std::vector<std::pair<std::string, std::string>>& right_side) {
    std::vector<double> found_roots;
    const bool has_imaginary = std::any_of(left_side.begin(), left_side.end(),
        [](const auto& token) { return token.first == "imaginary"; }) ||
        std::any_of(right_side.begin(), right_side.end(),
        [](const auto& token) { return token.first == "imaginary"; });
    if (has_imaginary) {
        const double scan_min = -root_search_limit, scan_max = root_search_limit, scan_step = 0.1;
        auto residual = [&](double value) {
            const double x = algebra_variable == "y" ? 0.0 : value;
            const double y = algebra_variable == "y" ? value : 0.0;
            return evaluate_complex_expression(left_side, x, y) - evaluate_complex_expression(right_side, x, y);
        };
        auto add_root = [&](double root) {
            for (double existing : found_roots)
                if (std::abs(existing - root) < 1e-5) return;
            found_roots.push_back(root);
        };
        auto magnitude = [&](double value) { return std::abs(residual(value)); };
        double previous_previous = std::numeric_limits<double>::infinity();
        double previous = magnitude(scan_min);
        for (int sample = 1; sample <= static_cast<int>((scan_max - scan_min) / scan_step); ++sample) {
            const double x = scan_min + sample * scan_step;
            const double current = magnitude(x);
            if (previous < 1e-8) add_root(x - scan_step);
            if (std::isfinite(previous_previous) && std::isfinite(previous) && std::isfinite(current) &&
                previous <= previous_previous && previous <= current) {
                double low = x - 2.0 * scan_step, high = x;
                const double golden = 0.6180339887498949;
                double left = high - golden * (high - low);
                double right = low + golden * (high - low);
                for (int iteration = 0; iteration < 70; ++iteration) {
                    if (magnitude(left) < magnitude(right)) {
                        high = right; right = left; left = high - golden * (high - low);
                    } else {
                        low = left; left = right; right = low + golden * (high - low);
                    }
                }
                const double candidate = (low + high) / 2.0;
                if (magnitude(candidate) < 1e-7) add_root(candidate);
            }
            previous_previous = previous;
            previous = current;
        }
        std::sort(found_roots.begin(), found_roots.end());
        return found_roots;
    }
    const double min_value = -root_search_limit;
    const double max_value = root_search_limit;
    const double x_tolerance = 1e-12;
    const int sample_count = std::max(1, static_cast<int>(std::ceil(
        (max_value - min_value) / 0.1)));
    const double step_amount = (max_value - min_value) / sample_count;
    const double value_tolerance = 1e-9;

    auto residual = [&](double x) {
        const double varying_x = algebra_variable == "y" ? 0.0 : x;
        const double varying_y = algebra_variable == "y" ? x : 0.0;
        return evaluate_expression(left_side, varying_x, varying_y) -
               evaluate_expression(right_side, varying_x, varying_y);
    };
    auto add_root = [&](double root) {
        if (!std::isfinite(root)) return;
        for (double existing : found_roots) {
            if (std::abs(existing - root) < 1e-6) return;
        }
        found_roots.push_back(root);
    };

    double previous_x = min_value;
    double previous_error = residual(previous_x);
    double before_previous_error = std::numeric_limits<double>::infinity();

    for (int sample = 1; sample <= sample_count; ++sample) {
        const double x = min_value + sample * step_amount;
        const double error = residual(x);

        if (std::isfinite(previous_error) && previous_error == 0.0) {
            add_root(previous_x);
        }
        if (std::isfinite(previous_error) && std::isfinite(error) &&
            ((previous_error < 0 && error > 0) || (previous_error > 0 && error < 0))) {
            double low = previous_x;
            double high = x;
            double low_error = previous_error;
            for (int iteration = 0; iteration < 100 && high - low > x_tolerance; ++iteration) {
                const double mid = low + (high - low) / 2.0;
                const double mid_error = residual(mid);
                if (!std::isfinite(mid_error)) break;
                if (mid_error == 0.0) {
                    low = high = mid;
                    break;
                }
                if ((low_error < 0 && mid_error > 0) || (low_error > 0 && mid_error < 0)) {
                    high = mid;
                } else {
                    low = mid;
                    low_error = mid_error;
                }
            }
            add_root(low + (high - low) / 2.0);
        }

        // Look for even-multiplicity roots, which do not cross the x-axis.
        if (std::isfinite(before_previous_error) && std::isfinite(previous_error) &&
            std::isfinite(error) && std::abs(previous_error) <= std::abs(before_previous_error) &&
            std::abs(previous_error) <= std::abs(error)) {
            double low = previous_x - step_amount;
            double high = previous_x + step_amount;
            const double golden = 0.6180339887498949;
            double left = high - golden * (high - low);
            double right = low + golden * (high - low);
            for (int iteration = 0; iteration < 60; ++iteration) {
                if (std::abs(residual(left)) < std::abs(residual(right))) {
                    high = right;
                    right = left;
                    left = high - golden * (high - low);
                } else {
                    low = left;
                    left = right;
                    right = low + golden * (high - low);
                }
            }
            const double candidate = low + (high - low) / 2.0;
            if (std::abs(residual(candidate)) < value_tolerance) add_root(candidate);
        }

        before_previous_error = previous_error;
        previous_x = x;
        previous_error = error;
    }

    std::sort(found_roots.begin(), found_roots.end());
    return found_roots;
}

void solve_basic_math() {
    const bool has_imaginary = std::any_of(math_input.begin(), math_input.end(),
        [](const auto& token) { return token.first == "imaginary"; });
    if (has_imaginary) {
        std::cout << "Final Solution: " << format_complex(evaluate_complex_expression(math_input, 0.0, 0.0)) << "\n";
    } else {
        const double final_solution = evaluate_expression(math_input, 0.0, 0.0);
        std::cout << "Final Solution: " << final_solution << "\n";
    }
}

void analyze_function_behavior(
    const std::vector<std::pair<std::string, std::string>>& function) {
    const double range = analysis_range;
    const int samples = 10000;
    const double step = 2.0 * range / samples;
    std::vector<double> values(samples + 1, std::numeric_limits<double>::quiet_NaN());
    auto evaluate = [&](double x) {
        return algebra_variable == "y"
            ? evaluate_expression(function, 0.0, x)
            : evaluate_expression(function, x, 0.0);
    };

    for (int i = 0; i <= samples; ++i) {
        const double x = -range + i * step;
        const double y = evaluate(x);
        if (std::isfinite(y)) values[i] = y;
    }

    std::cout << "Approximate function behavior on [" << -range << ", " << range << "]:\n";
    std::cout << "Domain (sampled): ";
    bool found_domain = false;
    for (int i = 0; i <= samples;) {
        if (!std::isfinite(values[i])) { ++i; continue; }
        const int start = i;
        while (i + 1 <= samples && std::isfinite(values[i + 1])) ++i;
        if (found_domain) std::cout << ", ";
        const double left = -range + start * step;
        const double right = -range + i * step;
        std::cout << "[" << std::setprecision(decimal_precision) << left << ", " << right << "]";
        found_domain = true;
        ++i;
    }
    if (!found_domain) std::cout << "no valid sampled values";
    std::cout << "\n";

    const double y_intercept = evaluate(0.0);
    if (std::isfinite(y_intercept))
        std::cout << "Y-intercept: (0, " << std::setprecision(decimal_precision) << y_intercept << ")\n";
    else
        std::cout << "Y-intercept: undefined\n";

    std::vector<double> roots;
    auto add_root = [&](double root) {
        if (!std::isfinite(root)) return;
        for (double existing : roots)
            if (std::abs(existing - root) < step * 0.5) return;
        roots.push_back(root);
    };
    for (int i = 0; i < samples; ++i) {
        if (!std::isfinite(values[i]) || !std::isfinite(values[i + 1])) continue;
        const double x1 = -range + i * step;
        if (std::abs(values[i]) < 1e-10) add_root(x1);
        if ((values[i] < 0.0) != (values[i + 1] < 0.0)) {
            const double fraction = values[i] / (values[i] - values[i + 1]);
            add_root(x1 + fraction * step);
        }
    }
    if (std::isfinite(values[samples]) && std::abs(values[samples]) < 1e-10)
        add_root(range);
    std::sort(roots.begin(), roots.end());
    std::cout << "X-intercepts (approximate): ";
    if (roots.empty()) std::cout << "none found in this range";
    else {
        for (size_t i = 0; i < roots.size(); ++i) {
            if (i) std::cout << ", ";
            std::cout << "(" << std::setprecision(decimal_precision) << roots[i] << ", 0)";
        }
    }
    std::cout << "\n";

    std::vector<std::pair<double, double>> maxima, minima;
    for (int i = 1; i < samples; ++i) {
        if (!std::isfinite(values[i - 1]) || !std::isfinite(values[i]) ||
            !std::isfinite(values[i + 1])) continue;
        const double x = -range + i * step;
        if (values[i] >= values[i - 1] && values[i] > values[i + 1])
            maxima.push_back({x, values[i]});
        if (values[i] <= values[i - 1] && values[i] < values[i + 1])
            minima.push_back({x, values[i]});
    }
    auto print_extrema = [](const std::string& label, const std::vector<std::pair<double, double>>& extrema) {
        std::cout << label;
        if (extrema.empty()) { std::cout << " none detected\n"; return; }
        const size_t count = std::min<size_t>(extrema.size(), 20);
        for (size_t i = 0; i < count; ++i)
            std::cout << (i ? ", " : " ") << "(" << std::setprecision(decimal_precision)
                      << extrema[i].first << ", " << extrema[i].second << ")";
        if (extrema.size() > count) std::cout << ", ...";
        std::cout << "\n";
    };
    print_extrema("Local maxima (approximate):", maxima);
    print_extrema("Local minima (approximate):", minima);
    std::cout << "Results are numerical estimates; the sampled domain and extrema may miss narrow features.\n";
}

bool parse_point_coordinates(const std::string& point, std::pair<double, double>& coordinates) {
    if (point.size() < 5 || point.front() != '(' || point.back() != ')') return false;
    const std::size_t comma = point.find(',');
    if (comma == std::string::npos || point.find(',', comma + 1) != std::string::npos) return false;

    try {
        std::size_t x_end = 0, y_end = 0;
        const double x = std::stod(point.substr(1, comma - 1), &x_end);
        const double y = std::stod(point.substr(comma + 1, point.size() - comma - 2), &y_end);
        if (x_end != comma - 1 || y_end != point.size() - comma - 2 ||
            !std::isfinite(x) || !std::isfinite(y)) return false;
        coordinates = {x, y};
        return true;
    } catch (const std::exception&) {
        return false;
    }
}

bool read_parenthesized_point(const std::string& text, std::size_t open,
    std::pair<double, double>& coordinates, std::size_t& after) {
    if (open >= text.size() || text[open] != '(') return false;
    const std::size_t close = text.find(')', open + 1);
    if (close == std::string::npos ||
        !parse_point_coordinates(text.substr(open, close - open + 1), coordinates)) return false;
    after = close + 1;
    return true;
}

void parse_point(const std::string& point) {
    std::pair<double, double> coordinates;
    if (!parse_point_coordinates(point, coordinates)) {
        std::cout << "Invalid point coordinates. Use numeric values in pnt(x,y).\n";
        return;
    }
    given_points.push_back(coordinates);
}

bool check_inequality(double left, double right, std::string op) {
    if (op == "less_than") return left < right;
    if (op == "greater_than") return left > right;
    if (op == "less_equal") return left <= right;
    if (op == "greater_equal") return left >= right;
    return std::abs(left - right) < 0.00001; 
}

void solve_inequality_range(const std::vector<std::vector<std::pair<std::string, std::string>>>& left_sides, const std::vector<std::vector<std::pair<std::string, std::string>>>& right_side, std::string op) {
    double scan_min = -100.0;
    double scan_max = 100.0;
    double scan_step = 1.0;
    std::vector<std::pair<double, double>> active_intervals;
    bool in_interval = false;
    double interval_start = 0.0;

    for (size_t side = 0; side < left_sides.size(); ++side) {
        in_interval = false;
        for (double x = scan_min; x <= scan_max; x += scan_step) {
            const double eval_x = algebra_variable == "y" ? 0.0 : x;
            const double eval_y = algebra_variable == "y" ? x : 0.0;
            double l_val = evaluate_expression(left_sides[side], eval_x, eval_y);
            double r_val = evaluate_expression(right_side[side], eval_x, eval_y);
            bool match = check_inequality(l_val, r_val, op);

            if (match && !in_interval) {
                in_interval = true;
                interval_start = x;
            } else if (!match && in_interval) {
                in_interval = false;
                active_intervals.push_back({interval_start, x - scan_step});
            }
        }
        if (in_interval) {
            active_intervals.push_back({interval_start, scan_max});
        }

        if (active_intervals.empty()) {
            std::cout << "No real intervals satisfy the inequality within boundaries.\n";
            return;
        }
    }

    std::cout << "Solved Inequality Set! True for ranges:\n";
    for (const auto& interval : active_intervals) {
        if (std::abs(interval.first - scan_min) < 0.1 && std::abs(interval.second - scan_max) < 0.1) {
            std::cout << "All real numbers (All X)\n";
        } else if (std::abs(interval.first - scan_min) < 0.1) {
            std::cout << algebra_variable << " <= " << interval.second << "\n";
        } else if (std::abs(interval.second - scan_max) < 0.1) {
            std::cout << algebra_variable << " >= " << interval.first << "\n";
        } else {
            std::cout << interval.first << " <= " << algebra_variable << " <= " << interval.second << "\n";
        }
    }
}

std::string format_radical_root(double value) {
    if (std::abs(value) < 1e-10) return "0";
    const double radicand = value * value;
    const double nearest_integer = std::round(radicand);
    std::ostringstream out;
    out << std::setprecision(decimal_precision);
    const std::string sign = value < 0.0 ? "-" : "";

    if (std::abs(radicand - nearest_integer) < 1e-6 && nearest_integer <= 1000000000000.0) {
        const long long integer = static_cast<long long>(nearest_integer);
        long long outside = 1;
        long long inside = 1;
        long long remaining = integer;
        for (long long factor = 2; factor * factor <= remaining; ++factor) {
            int exponent = 0;
            while (remaining % factor == 0) {
                remaining /= factor;
                ++exponent;
            }
            for (int count = 0; count < exponent / 2; ++count) outside *= factor;
            if (exponent % 2) inside *= factor;
        }
        if (remaining > 1) inside *= remaining;
        if (inside == 1) return sign + std::to_string(outside);
        if (outside == 1) return sign + "√" + std::to_string(inside);
        return sign + std::to_string(outside) + "√" + std::to_string(inside);
    }

    out << sign << "√(" << radicand << ")";
    return out.str();
}

void solve_basic_algebra() {
    std::vector<std::vector<std::pair<std::string, std::string>>> left_sides;
    std::vector<std::vector<std::pair<std::string, std::string>>> right_sides;
    std::vector<std::pair<std::string, std::string>> left_side;
    std::vector<std::pair<std::string, std::string>> right_side;
    
    bool after_equals = false;
    int number_of_equals = 0;
    std::string boundary_operator = "equals"; 

    for (auto entry : math_input) {
        if (entry.first == "equals" || entry.first == "less_than" || 
            entry.first == "greater_than" || entry.first == "less_equal" || 
            entry.first == "greater_equal") {
            
            number_of_equals++; 
            boundary_operator = entry.first; 
            after_equals = true;
        } else if (entry.first == "semicolon") {
            left_sides.push_back(left_side);
            right_sides.push_back(right_side);
            left_side.clear();
            right_side.clear();
            after_equals = false;
        } else {
            if (!after_equals) {
                left_side.push_back(entry);
            } else {
                right_side.push_back(entry);
            }
        }
    }

    // Store the final equation when there is no trailing semicolon.
    if (!left_side.empty() || !right_side.empty()) {
        left_sides.push_back(left_side);
        right_sides.push_back(right_side);
    }

    if (number_of_equals > 1) {
        std::cout << "Too many equals signs. Could not solve.\n";
        return;
    }

    if (left_sides.empty() || right_sides.empty()) {
        std::cout << "Could not solve: incomplete equation.\n";
        return;
    }

    if (boundary_operator != "equals") {
        relational_operator = boundary_operator;
        solve_inequality_range(left_sides, right_sides, boundary_operator);
        return;
    }

    const bool has_imaginary = std::any_of(math_input.begin(), math_input.end(),
        [](const auto& token) { return token.first == "imaginary"; });
    if (has_imaginary) {
        std::vector<std::complex<double>> solutions;
        for (size_t side = 0; side < left_sides.size(); ++side) {
            const auto side_solutions = find_complex_roots(left_sides[side], right_sides[side]);
            for (const auto& solution : side_solutions) {
                bool duplicate = false;
                for (const auto& existing : solutions)
                    if (std::abs(existing - solution) < 1e-5) duplicate = true;
                if (!duplicate) solutions.push_back(solution);
            }
        }
        if (solutions.empty()) {
            std::cout << "Could not converge on a precise solution.\n";
        } else {
            std::cout << "Solved! Found " << solutions.size() << " solution(s):\n";
            for (const auto& solution : solutions)
                std::cout << algebra_variable << " = " << format_complex(solution) << "\n";
        }
        return;
    }

    std::vector<double> solutions;
    std::vector<std::complex<double>> complex_solutions;
    for (size_t side = 0; side < left_sides.size(); ++side) {
        std::vector<double> side_solutions = find_roots(left_sides[side], right_sides[side]);
        solutions.insert(solutions.end(), side_solutions.begin(), side_solutions.end());

        for (const std::complex<double>& root : find_complex_roots(left_sides[side], right_sides[side])) {
            if (std::abs(root.imag()) < 1e-7) continue;
            bool duplicate = false;
            for (const std::complex<double>& existing : complex_solutions) {
                if (std::abs(existing - root) < 1e-5) {
                    duplicate = true;
                    break;
                }
            }
            if (!duplicate) complex_solutions.push_back(root);
        }
    }

    if (!solutions.empty() || !complex_solutions.empty()) {
        std::cout << "Solved! Found " << solutions.size() + complex_solutions.size() << " solution(s):\n";
        for (double sol : solutions) {
            if (print_square_roots) {
                std::cout << algebra_variable << " = " << format_radical_root(sol) << "\n";
            } else {
                std::cout << algebra_variable << " = " << std::setprecision(decimal_precision) << sol << "\n";
            }
        }
        for (const std::complex<double>& solution : complex_solutions)
            std::cout << algebra_variable << " = " << format_complex(solution) << "\n";
    } else {
        std::cout << "Could not converge on a precise solution.\n";
    }
}

void solve_multivariable_algebra() {
    std::vector<std::pair<std::string, std::string>> eq1_left, eq1_right;
    std::vector<std::pair<std::string, std::string>> eq2_left, eq2_right;

    bool on_second_equation = false;
    bool after_equals = false;

    for (auto entry : math_input) {
        if (entry.first == "semicolon") {
            on_second_equation = true;
            after_equals = false;
        }
        else if (entry.first == "equals") {
            after_equals = true;
        }
        else if (!on_second_equation) {
            if (!after_equals) eq1_left.push_back(entry);
            else eq1_right.push_back(entry);
        }
        else {
            if (!after_equals) eq2_left.push_back(entry);
            else eq2_right.push_back(entry);
        }
    }

    auto residuals = [&](double x, double y) {
        return Residuals{
            evaluate_expression(eq1_left, x, y) - evaluate_expression(eq1_right, x, y),
            evaluate_expression(eq2_left, x, y) - evaluate_expression(eq2_right, x, y)};
    };

    const double epsilon = 1e-7;
    const double seeds[] = {-1000, -100, -10, 0, 10, 100, 1000};
    std::vector<std::pair<double, double>> solutions;

    for (double start_x : seeds) {
        for (double start_y : seeds) {
            double x = start_x;
            double y = start_y;

            for (int iteration = 0; iteration < 100; ++iteration) {
                auto error = residuals(x, y);
                if (!std::isfinite(error.first) || !std::isfinite(error.second)) break;
                if (std::abs(error.first) < epsilon && std::abs(error.second) < epsilon) {
                    bool duplicate = false;
                    for (const auto& solution : solutions) {
                        if (std::abs(solution.first - x) < 1e-4 &&
                            std::abs(solution.second - y) < 1e-4) {
                            duplicate = true;
                            break;
                        }
                    }
                    if (!duplicate) solutions.push_back({x, y});
                    break;
                }

                double h_x = 1e-5 * (1.0 + std::abs(x));
                double h_y = 1e-5 * (1.0 + std::abs(y));
                auto error_x = residuals(x + h_x, y);
                auto error_y = residuals(x, y + h_y);
                double a = (error_x.first - error.first) / h_x;
                double c = (error_x.second - error.second) / h_x;
                double b = (error_y.first - error.first) / h_y;
                double d = (error_y.second - error.second) / h_y;
                double determinant = a * d - b * c;

                if (!std::isfinite(determinant) || std::abs(determinant) < 1e-12) break;

                double delta_x = (-error.first * d + b * error.second) / determinant;
                double delta_y = (c * error.first - a * error.second) / determinant;
                double old_norm = std::abs(error.first) + std::abs(error.second);
                bool improved = false;

                for (double scale = 1.0; scale >= 1.0 / 128.0; scale /= 2.0) {
                    double next_x = x + scale * delta_x;
                    double next_y = y + scale * delta_y;
                    if (!std::isfinite(next_x) || !std::isfinite(next_y) ||
                        std::abs(next_x) > 1e6 || std::abs(next_y) > 1e6) continue;

                    auto next_error = residuals(next_x, next_y);
                    double next_norm = std::abs(next_error.first) + std::abs(next_error.second);
                    if (std::isfinite(next_norm) && next_norm < old_norm) {
                        x = next_x;
                        y = next_y;
                        improved = true;
                        break;
                    }
                }
                if (!improved) break;
            }
        }
    }

    if (solutions.empty()) {
        std::cout << "No matching system solutions found in active bounds.\n";
        return;
    }

    std::cout << "Solved System! Found " << solutions.size() << " solution(s):\n";
    for (const auto& solution : solutions) {
        std::cout << "x = " << solution.first << ", y = " << solution.second << "\n";
    }
}

void parse_equation() {
    needs_vertical = false;
    theta_count = 1.0;
    std::vector<char> found_variables;
    
    std::string clean_equation;
    for (char c : equation) {
        if (c != ' ') {
            clean_equation += c;
        }
    }
    equation = clean_equation;

    // integ(expression, lower, upper) evaluates a definite integral.
    if (equation.rfind("integ(", 0) == 0) {
        if (equation.back() != ')') {
            std::cout << "Invalid integral. Use integ(expression, lower, upper), for example integ(x^2,0,5).\n";
            return;
        }
        std::vector<std::string> arguments;
        const std::string contents = equation.substr(6, equation.size() - 7);
        if (!split_function_arguments(contents, arguments) || arguments.size() != 3 ||
            arguments[0].empty() || arguments[1].empty() || arguments[2].empty()) {
            std::cout << "Invalid integral. Use integ(expression, lower, upper), for example integ(x^2,0,5).\n";
            return;
        }
        if (!parse_finite_number(arguments[1], integral_lower_bound) ||
            !parse_finite_number(arguments[2], integral_upper_bound)) {
            std::cout << "Integral bounds must be finite numbers.\n";
            return;
        }
        calculate_definite_integral = true;
        equation = arguments[0];
    } else if (equation.rfind("sum(", 0) == 0) {
        if (equation.back() != ')') {
            std::cout << "Invalid sigma. Use sum(expression, variable, start, end).\n";
            return;
        }
        std::vector<std::string> arguments;
        const std::string contents = equation.substr(4, equation.size() - 5);
        if (!split_function_arguments(contents, arguments) || arguments.size() != 4 ||
            arguments[0].empty() || arguments[1].size() != 1 ||
            !std::isalpha(static_cast<unsigned char>(arguments[1][0])) ||
            arguments[1] == "i" || arguments[1] == "e" ||
            arguments[2].empty() || arguments[3].empty()) {
            std::cout << "Invalid sigma. Use sum(expression, variable, start, end), for example sum(n^2,n,1,5).\n";
            return;
        }
        try {
            std::size_t start_end = 0, finish_end = 0;
            sigma_lower_bound = std::stoll(arguments[2], &start_end);
            sigma_upper_bound = std::stoll(arguments[3], &finish_end);
            if (start_end != arguments[2].size() || finish_end != arguments[3].size())
                throw std::invalid_argument("Sigma bounds must be integers.");
        } catch (const std::exception&) {
            std::cout << "Sigma bounds must be integers.\n";
            return;
        }
        const long double term_count = static_cast<long double>(sigma_upper_bound) -
                                       static_cast<long double>(sigma_lower_bound) + 1.0L;
        if (term_count > 1000000.0L) {
            std::cout << "Sigma range is too large; use at most 1000000 terms.\n";
            return;
        }
        sigma_variable = arguments[1];
        calculate_sigma = true;
        equation = arguments[0];
    }

    // deriv(expression, point) evaluates the derivative numerically at point.
    if (equation.rfind("deriv(", 0) == 0) {
        const std::size_t open = 5;
        int depth = 0;
        std::size_t comma = std::string::npos;
        std::size_t close = std::string::npos;
        for (std::size_t i = open + 1; i < equation.size(); ++i) {
            if (equation[i] == '(') ++depth;
            else if (equation[i] == ')') {
                if (depth == 0) { close = i; break; }
                --depth;
            } else if (equation[i] == ',' && depth == 0 && comma == std::string::npos) {
                comma = i;
            }
        }
        if (comma == std::string::npos || close == std::string::npos || comma >= close || close + 1 != equation.size()) {
            std::cout << "Invalid derivative. Use deriv(expression, point), for example deriv(x^2,3).\n";
            return;
        }
        try {
            const std::string point_text = equation.substr(comma + 1, close - comma - 1);
            std::size_t parsed = 0;
            derivative_target = std::stod(point_text, &parsed);
            if (parsed != point_text.size() || !std::isfinite(derivative_target)) {
                std::cout << "Invalid derivative point. Use a finite number.\n";
                return;
            }
        } catch (const std::exception&) {
            std::cout << "Invalid derivative point. Use a finite number.\n";
            return;
        }
        calculate_derivative = true;
        equation = equation.substr(open + 1, comma - open - 1);
    }

    // lim(x->a) and lmt(x->a) both evaluate a two-sided limit. limN remains
    // the existing option for setting the root-search range.
    const std::size_t limit_prefix = equation.rfind("lim(", 0) == 0 ? 4 :
                                     equation.rfind("lmt(", 0) == 0 ? 4 : std::string::npos;
    if (limit_prefix != std::string::npos) {
        const std::size_t arrow = equation.find("->", limit_prefix);
        const std::size_t close = equation.find(')', arrow == std::string::npos ? limit_prefix : arrow + 2);
        if (arrow == std::string::npos || close == std::string::npos || close == arrow + 2) {
            std::cout << "Invalid limit. Use lim(x->a)expression, for example lim(x->2)(x^2-4)/(x-2).\n";
            return;
        }
        try {
            const std::string point_text = equation.substr(arrow + 2, close - arrow - 2);
            std::size_t parsed = 0;
            limit_target = std::stod(point_text, &parsed);
            if (parsed != point_text.size() || !std::isfinite(limit_target)) {
                std::cout << "Invalid limit point. Use a finite numeric value.\n";
                return;
            }
            calculate_limit = true;
            equation = equation.substr(close + 1);
            if (equation.empty()) {
                std::cout << "Missing function after the limit point.\n";
                return;
            }
        } catch (const std::exception&) {
            std::cout << "Invalid limit point. Use a finite numeric value.\n";
            return;
        }
    }

    for (size_t i = 0; i < equation.length(); i++) {
        char current_char = equation[i];
        std::string char_str(1, current_char);

        if (i + 3 < equation.length() && equation.substr(i, 4) == "sqrt") {
            math_input.push_back({"square_root", "sqrt"});
            i += 3;
        }
        if (i + 1 < equation.length() && equation.substr(i, 2) == "pi") {
            math_input.push_back({"number", std::to_string(pi)});
            i += 2;
        }
        else if (i + 2 < equation.length() && equation.substr(i, 3) == "ana") {
            analyze_function = true;
            i += 2;
        }
        else if (i + 3 < equation.length() && equation.substr(i, 4) == "prnt") {
            prints_angles = false;
            i += 3;
        }
        else if (i + 3 < equation.length() && equation.substr(i, 4) == "auto") {
            is_automatic = true;
            i += 3;
        }
        else if (i + 3 < equation.length() && equation.substr(i, 4) == "grph") {
            math_input.push_back({"graph_size", "grph"});
            i += 3;
        }
        else if (i + 2 < equation.length() && equation.substr(i, 3) == "fib") {
            has_fib = true;
            i += 2;
        }
        else if (i + 2 < equation.length() && equation.substr(i, 3) == "prc") {
            math_input.push_back({"decimal_precision", "prc"});
            i += 2;
        }
        else if (i + 2 < equation.length() && equation.substr(i, 3) == "lmt") {
            std::cout << "Use lmt(x->a)function for a limit, for example lmt(x->2)(x^2-4)/(x-2).\n";
            return;
        }
        else if (i + 3 < equation.length() && equation.substr(i, 4) == "root") {
            print_square_roots = true;
            i += 3;
        }
        else if (equation.compare(i, 3, "lim") == 0) {
            std::size_t value_start = i + 3;
            if (value_start < equation.length() && equation[value_start] == '=') ++value_start;
            std::size_t value_end = value_start;
            while (value_end < equation.length() &&
                   (std::isdigit(static_cast<unsigned char>(equation[value_end])) || equation[value_end] == '.'))
                ++value_end;
            try {
                const double limit = std::stod(equation.substr(value_start, value_end - value_start));
                if (value_end == value_start || !std::isfinite(limit) || limit <= 0.0 || limit > 1000000.0) {
                    std::cout << "lim must be a positive number no greater than 1000000.\n";
                } else {
                    root_search_limit = limit;
                    analysis_range = std::min(limit, 1000000.0);
                }
            } catch (const std::exception&) {
                std::cout << "lim must be a positive number no greater than 1000000.\n";
            }
            if (value_end > i) i = value_end - 1;
        }
        else if (equation.compare(i, 3, "cnt") == 0) {
            std::size_t value_start = i + 3;
            if (value_start < equation.length() && equation[value_start] == '=') ++value_start;
            std::size_t value_end = value_start;
            while (value_end < equation.length() &&
                   (std::isdigit(static_cast<unsigned char>(equation[value_end])) || equation[value_end] == '.'))
                ++value_end;
            try {
                const double count = std::stod(equation.substr(value_start, value_end - value_start));
                if (value_end == value_start || !std::isfinite(count) || count <= 0.0) {
                    std::cout << "cnt must be a positive number.\n";
                } else {
                    theta_count = count;
                }
            } catch (const std::exception&) {
                std::cout << "cnt must be a positive number.\n";
            }
            if (value_end > i) i = value_end - 1;
        }
        else if (i + 4 < equation.length() && equation.substr(i, 5) == "theta") {
            math_input.push_back({"variable", "theta"});
            i += 4;
        }
        else if (i + 3 < equation.length() && equation.substr(i, 4) == "polr") {
            math_input.push_back({"polar", "polr"});
            has_polar = true;
            i += 3;
        }
        else if (i + 4 < equation.length() && equation.substr(i, 5) == "integ") {
            std::cout << "Use integ(expression, lower, upper) as a complete input.\n";
            return;
        }
        else if (i + 2 < equation.length() && equation.substr(i, 3) == "sum") {
            std::cout << "Use sum(expression, variable, start, end) as a complete input.\n";
        }
        else if ((i + 3 < equation.length() &&
                  (equation.substr(i, 4) == "rayl" || equation.substr(i, 4) == "rayr")) ||
                 (i + 2 < equation.length() && equation.substr(i, 3) == "seg")) {
            const std::string type = equation.substr(i, 3) == "seg" ? "seg" : equation.substr(i, 4);
            const std::size_t command_length = type == "seg" ? 3 : 4;
            std::pair<double, double> first, second;
            std::size_t after_first = 0, after_second = 0;
            if (i + command_length >= equation.size() || equation[i + command_length] != '(' ||
                !read_parenthesized_point(equation, i + command_length, first, after_first) ||
                !read_parenthesized_point(equation, after_first, second, after_second)) {
                std::cout << "Invalid. Use seg(x1,y1)(x2,y2), rayl(x1,y1)(x2,y2), or rayr(x1,y1)(x2,y2).\n";
            } else {
                drawing_primitives.push_back({type, first, second});
                i = after_second - 1;
            }
        }
        else if (equation.compare(i, 4, "asin") == 0 || equation.compare(i, 4, "acos") == 0 ||
                 equation.compare(i, 4, "atan") == 0 || equation.compare(i, 3, "sin") == 0 ||
                 equation.compare(i, 3, "cos") == 0 || equation.compare(i, 3, "tan") == 0 ||
                 equation.compare(i, 3, "log") == 0 || equation.compare(i, 2, "ln") == 0) {
            const std::string function = equation.compare(i, 4, "asin") == 0 ? "asin" :
                equation.compare(i, 4, "acos") == 0 ? "acos" :
                equation.compare(i, 4, "atan") == 0 ? "atan" :
                equation.compare(i, 3, "sin") == 0 ? "sin" :
                equation.compare(i, 3, "cos") == 0 ? "cos" :
                equation.compare(i, 3, "tan") == 0 ? "tan" :
                equation.compare(i, 3, "log") == 0 ? "log" : "ln";
            const std::size_t function_length = function == "ln" ? 2 : (function == "asin" || function == "acos" || function == "atan" ? 4 : 3); // (function == "asin" || function == "acos" || function == "atan
            if (i + function_length >= equation.length() || equation[i + function_length] != '(') {
                std::cout << "Function " << function << " requires parentheses.\n";
            } else {
                math_input.push_back({"function", function});
                i += function_length - 1;
            }
        }
        else if (i + 2 < equation.length() && equation.substr(i, 3) == "pnt") {
            const std::size_t close = equation.find(')', i + 3);
            if (close == std::string::npos) {
                std::cout << "Invalid point. Use pnt(x,y), for example pnt(2,-3).\n";
                i = equation.length();
            } else {
                parse_point(equation.substr(i + 3, close - i - 2));
                i = close;
            }
        }
        else if (current_char == 'e') {
            math_input.push_back({"number", "2.718281828459045"});
        }
        else if (current_char == 'i') {
            math_input.push_back({"imaginary", "i"});
        }
        else if (std::isalpha(current_char)) {
            bool in_variables = false;
            for (char entry : found_variables) {
                if (entry == current_char) {
                    in_variables = true;
                }
            }
            if (in_variables == false) {
                if (variable_count == 0) algebra_variable = char_str;
                variable_count++;
                find_variables(char_str);
                found_variables.push_back(current_char);
            }
            math_input.push_back({"variable", char_str});
        }
        else if (current_char == '+') {
            math_input.push_back({"plus", char_str});
        }
        else if (current_char == '-') {
            math_input.push_back({"minus", char_str});
        }
        else if (current_char == '/') {
            math_input.push_back({"divide", char_str});
        }
        else if (current_char == '*') {
            math_input.push_back({"multiply", char_str});
        }
        else if (current_char == '=') {
            math_input.push_back({"equals", char_str});
            has_equals = true;
        }
        else if (current_char == '(') {
            math_input.push_back({"open_parentheses", char_str});
        }
        else if (current_char == ')') {
            math_input.push_back({"close_parentheses", char_str});
        }
        else if (current_char == '|') {
            if (needs_vertical) {
                math_input.push_back({"close_vertical", char_str});
                needs_vertical = false;
            } else {
                math_input.push_back({"open_vertical", char_str});
                needs_vertical = true;
            }
        }
        else if (current_char == '_') {
            math_input.push_back({"minus", "-"});
        }
        else if (current_char == '.') {
            math_input.push_back({"period", char_str});
        }
        else if (current_char == '^') {
            math_input.push_back({"exponent", char_str});
        }
        else if (current_char == ';') {
            math_input.push_back({"semicolon", char_str});
        }
        else if (current_char == '<') {
            if (i + 1 < equation.length() && equation[i + 1] == '=') {
                math_input.push_back({"less_equal", "<="});
                i++;
            } else {
                math_input.push_back({"less_than", "<"});
            }
            has_equals = true;
        }
        else if (current_char == '>') {
            if (i + 1 < equation.length() && equation[i + 1] == '=') {
                math_input.push_back({"greater_equal", ">="});
                i++;
            } else {
                math_input.push_back({"greater_than", ">"});
            }
            has_equals = true;
        }
        else if (std::isdigit(current_char)) {
            math_input.push_back({"number", char_str});
        }
        else {
            std::cout << "Invalid character detected.\n";
        }
    }

    std::vector<std::pair<std::string, std::string>> combined_input;
    for (size_t i = 0; i < math_input.size(); i++) {
        if (math_input[i].first == "number" || math_input[i].first == "period") {
            std::string full_number = math_input[i].second;
            while (i + 1 < math_input.size() &&
                  (math_input[i + 1].first == "number" || math_input[i + 1].first == "period")) {
                i++;
                full_number += math_input[i].second;
            }
            combined_input.push_back({"number", full_number});
            if (i + 1 < math_input.size() && math_input[i + 1].first == "variable") {
                combined_input.push_back({"multiply", "*"});
            }
        } 
        else if (math_input[i].first == "variable") {
            combined_input.push_back(math_input[i]);
            if (i + 1 < math_input.size() && 
               (math_input[i + 1].first == "number" || math_input[i + 1].first == "open_parentheses")) {
                combined_input.push_back({"multiply", "*"});
            }
        }
        else {
            combined_input.push_back(math_input[i]);
        }
    }
    math_input = combined_input;

    std::vector<std::pair<std::string, std::string>> final_tokens;
    bool has_grph = false;
    for (size_t i = 0; i < math_input.size(); ++i) {
        if (math_input[i].first == "decimal_precision") {
            // Consume the precision value so it cannot be treated as an operand.
            if (i + 1 < math_input.size() && math_input[i + 1].first == "number") {
                const double val = std::stod(math_input[i + 1].second);
                if (std::isfinite(val) && val >= 0.0) {
                    decimal_precision = std::min(15.0, val);
                }
                ++i;
            }
            continue;
        }
        if (math_input[i].first == "graph_size") {
            has_grph = true;
            if (i + 1 < math_input.size() && math_input[i + 1].first == "number") {
                const double val = std::stod(math_input[i + 1].second);
                if (val > 0) {
                    graph_size_x = val;
                    graph_size_y = val;
                }
                ++i;
            }
        } else {
            final_tokens.push_back(math_input[i]);
        }
    }
    math_input = final_tokens;

    if (calculate_sigma) {
        const bool invalid_expression = has_equals ||
            std::any_of(math_input.begin(), math_input.end(), [&](const auto& token) {
                return token.first == "semicolon" || token.first == "imaginary" ||
                    token.first == "equals" || token.first == "less_than" ||
                    token.first == "greater_than" || token.first == "less_equal" ||
                    token.first == "greater_equal" ||
                    (token.first == "variable" && token.second != sigma_variable);
            });
        if (invalid_expression) {
            std::cout << "Use sum(expression, variable, start, end) with only the summation variable, for example sum(n^2,n,1,5).\n";
            return;
        }

        long double total = 0.0L;
        if (sigma_lower_bound <= sigma_upper_bound) {
            for (long long term = sigma_lower_bound;; ++term) {
                auto term_tokens = math_input;
                const std::string value = std::to_string(term);
                for (auto& token : term_tokens)
                    if (token.first == "variable" && token.second == sigma_variable)
                        token = {"number", value};

                const double result = evaluate_expression(term_tokens, 0.0, 0.0);
                if (!std::isfinite(result)) {
                    std::cout << "Sigma could not be evaluated; a term is undefined.\n";
                    return;
                }
                total += result;
                if (!std::isfinite(total)) {
                    std::cout << "Sigma result is outside the supported numeric range.\n";
                    return;
                }
                if (term == sigma_upper_bound) break;
            }
        }
        std::cout << "Sigma sum = " << std::setprecision(decimal_precision) << total << "\n";
        return;
    }

    if (calculate_definite_integral) {
        const bool invalid_expression = has_equals || variable_count > 1 ||
            std::any_of(math_input.begin(), math_input.end(), [](const auto& token) {
                return token.first == "semicolon" || token.first == "imaginary";
            });
        if (invalid_expression) {
            std::cout << "Use integ(expression, lower, upper) with one real-valued function, for example integ(x^2,0,5).\n";
            return;
        }
        const double result = calculate_integral(math_input, integral_lower_bound, integral_upper_bound);
        if (std::isfinite(result)) {
            std::cout << "Approximate integral from " << std::setprecision(decimal_precision)
                      << integral_lower_bound << " to " << integral_upper_bound << " = " << result << "\n";
        } else {
            std::cout << "Integral could not be evaluated; the function may be undefined within the bounds.\n";
        }
        return;
    }

    if (calculate_derivative) {
        const bool invalid_expression = has_equals || variable_count != 1 ||
            std::any_of(math_input.begin(), math_input.end(), [](const auto& token) {
                return token.first == "semicolon" || token.first == "imaginary";
            });
        if (invalid_expression) {
            std::cout << "Use deriv(expression, point) with one real-valued variable, for example deriv(x^2,3).\n";
            return;
        }

        auto evaluate_at = [&](double value) {
            return algebra_variable == "y"
                ? evaluate_expression(math_input, 0.0, value)
                : evaluate_expression(math_input, value, 0.0);
        };
        double h = std::pow(std::numeric_limits<double>::epsilon(), 0.2) *
                   (1.0 + std::abs(derivative_target));
        double best_derivative = std::numeric_limits<double>::quiet_NaN();
        double best_change = std::numeric_limits<double>::infinity();
        double previous_derivative = std::numeric_limits<double>::quiet_NaN();

        for (int refinement = 0; refinement < 8; ++refinement, h *= 0.5) {
            const double fm2 = evaluate_at(derivative_target - 2.0 * h);
            const double fm1 = evaluate_at(derivative_target - h);
            const double fp1 = evaluate_at(derivative_target + h);
            const double fp2 = evaluate_at(derivative_target + 2.0 * h);
            if (!std::isfinite(fm2) || !std::isfinite(fm1) ||
                !std::isfinite(fp1) || !std::isfinite(fp2)) continue;

            const double estimate = (fm2 - 8.0 * fm1 + 8.0 * fp1 - fp2) / (12.0 * h);
            if (!std::isfinite(estimate)) continue;
            if (std::isfinite(previous_derivative)) {
                const double change = std::abs(estimate - previous_derivative);
                if (change < best_change) {
                    best_change = change;
                    best_derivative = estimate;
                }
            }
            previous_derivative = estimate;
        }

        if (!std::isfinite(best_derivative)) {
            std::cout << "Derivative could not be estimated at that point; check the function's domain.\n";
        } else {
            std::cout << "Approximate derivative at " << algebra_variable << " = "
                      << std::setprecision(decimal_precision) << derivative_target << " is "
                      << best_derivative << "\n";
        }
        return;
    }

    if (calculate_limit) {
        const bool invalid_expression = has_equals || variable_count > 1 ||
            std::any_of(math_input.begin(), math_input.end(), [](const auto& token) {
                return token.first == "semicolon" || token.first == "imaginary";
            });
        if (invalid_expression) {
            std::cout << "Use lim(x->a) with one real-valued function, for example lim(x->2)(x^2-4)/(x-2).\n";
            return;
        }

        auto evaluate_at = [&](double value) {
            return algebra_variable == "y"
                ? evaluate_expression(math_input, 0.0, value)
                : evaluate_expression(math_input, value, 0.0);
        };
        std::vector<double> left_values, right_values;
        const double scale = 1.0 + std::abs(limit_target);
        for (int refinement = 1; refinement <= 9; ++refinement) {
            const double distance = scale * std::pow(0.1, refinement);
            const double left = evaluate_at(limit_target - distance);
            const double right = evaluate_at(limit_target + distance);
            left_values.push_back(left);
            right_values.push_back(right);
        }

        auto estimate_side = [](const std::vector<double>& values) {
            for (std::size_t i = values.size(); i >= 3; --i) {
                const double a = values[i - 1], b = values[i - 2], c = values[i - 3];
                if (!std::isfinite(a) || !std::isfinite(b) || !std::isfinite(c)) continue;
                const double tolerance = 1e-5 * std::max(1.0, std::abs(a));
                if (std::abs(a - b) <= tolerance && std::abs(b - c) <= tolerance)
                    return a;
            }
            return std::numeric_limits<double>::quiet_NaN();
        };
        const double left_limit = estimate_side(left_values);
        const double right_limit = estimate_side(right_values);
        if (std::isfinite(left_limit) && std::isfinite(right_limit)) {
            const double tolerance = 1e-4 * std::max({1.0, std::abs(left_limit), std::abs(right_limit)});
            if (std::abs(left_limit - right_limit) <= tolerance) {
                std::cout << "Approximate limit as " << algebra_variable << " -> "
                          << std::setprecision(decimal_precision) << limit_target << " = "
                          << (left_limit + right_limit) / 2.0 << "\n";
            } else {
                std::cout << "Two-sided limit does not exist (the one-sided limits differ).\n";
            }
        } else {
            std::cout << "Limit could not be determined numerically (it may diverge or oscillate).\n";
        }
        return;
    }

    if (has_grph) {
        std::vector<std::vector<std::pair<std::string, std::string>>> graph_expressions;
        std::vector<std::pair<std::string, std::string>> current_expression;
        for (const auto& token : math_input) {
            if (token.first == "semicolon") {
                if (!current_expression.empty()) graph_expressions.push_back(current_expression);
                current_expression.clear();
            } else {
                current_expression.push_back(token);
            }
        }
        if (!current_expression.empty()) graph_expressions.push_back(current_expression);

        graph(graph_expressions, graph_size_x, graph_size_y);
        return;
    }

    if (analyze_function) {
        if (has_equals || variable_count == 0 ||
            std::any_of(math_input.begin(), math_input.end(),
                [](const auto& token) { return token.first == "semicolon" || token.first == "imaginary"; })) {
            std::cout << "Use ana with one real-valued function of a variable, for example: ana x^2-4 lim10\n";
        } else {
            analyze_function_behavior(math_input);
        }
        return;
    }

    if (variable_count == 0 && !has_equals) {
        solve_basic_math();
    }
    else if (variable_count == 0 && has_equals) {
        auto relation = std::find_if(math_input.begin(), math_input.end(), [](const auto& token) {
            return token.first == "equals" || token.first == "less_than" || token.first == "greater_than" ||
                   token.first == "less_equal" || token.first == "greater_equal";
        });
        if (relation == math_input.end()) {
            std::cout << "Could not evaluate the equation.\n";
        } else {
            const std::vector<std::pair<std::string, std::string>> left(math_input.begin(), relation);
            const std::vector<std::pair<std::string, std::string>> right(relation + 1, math_input.end());
            const std::complex<double> lhs = evaluate_complex_expression(left, 0.0, 0.0);
            const std::complex<double> rhs = evaluate_complex_expression(right, 0.0, 0.0);
            bool matches = false;
            if (relation->first == "equals") matches = std::abs(lhs - rhs) < 1e-9;
            else if (std::abs(lhs.imag()) < 1e-10 && std::abs(rhs.imag()) < 1e-10)
                matches = check_inequality(lhs.real(), rhs.real(), relation->first);
            else {
                std::cout << "Inequalities require real-valued sides.\n";
                return;
            }
            std::cout << (matches ? "True: " : "False: ") << format_complex(lhs) << " "
                      << relation->second << " " << format_complex(rhs) << "\n";
        }
    }
    else if (variable_count == 1 && !has_equals) {
        math_input.push_back({"equals", "="});
        math_input.push_back({"number", "0"});
        std::cout << "Equation set to zero to solve\n";
        solve_basic_algebra();
    }
    else if (variable_count == 1 && has_equals) {
        solve_basic_algebra();
    }
    else if (variable_count >= 2) {
        const bool has_second_equation = std::any_of(math_input.begin(), math_input.end(),
            [](const auto& token) { return token.first == "semicolon"; });
        if (!has_second_equation) {
            std::cout << "This uses multiple variables. Add a second equation separated by ';' to solve a system, or use 'grph' to graph it.\n";
            return;
        }
        solve_multivariable_algebra();
        return;
    }
}

int main() {
    std::cout << std::setprecision(15);
    std::cout << "Please type your math problem: \n";
    std::getline(std::cin, equation);
    parse_equation();
    return 0;
}
