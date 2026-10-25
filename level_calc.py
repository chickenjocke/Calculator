import random
import math


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    num = random.choice([2, 4, 5])
    denom = random.choice([3, 4, 6])
    visual = f"lmt(x->0)(sin({num}*x)/(sin({denom}*x)))"
    prompt = _pick_variant([
        "Evaluate the trigonometric function configuration limit as x approaches zero using limit calculation tools:",
        "What is this limit as x approaches 0?",
        "Find the value of the limit.",
        "Evaluate the trigonometric limit."
    ])
    return prompt, visual, f"{num}/{denom}"


def count_items_5_10():
    num = random.choice([2, 3, 4])
    visual = f"lmt(x->2)((x^2 - {num*2}*x + {num*2}) / (x - 2))"
    prompt = _pick_variant([
        "Evaluate the rational expression limit function properties using the removable discontinuity resolution engine:",
        "What does this limit evaluate to?",
        "Find the limit of the rational expression.",
        "Compute the limit value."
    ])
    return prompt, visual, "undefined"


def missing_number_sequence():
    v1 = random.choice([4, 9, 16])
    visual = f"sum(n^2, n, 1, {v1})"
    prompt = _pick_variant([
        "Find the total calculated output string properties for this structural summation sigma sequence expression operation track:",
        "What is the sum of the series?",
        "Evaluate this sigma sum.",
        "Compute the total value of the summation."
    ])
    return prompt, visual, "Sigma sum"


def basic_addition():
    lower = random.choice([0, 1])
    upper = random.randint(2, 4)
    visual = f"integ(3*x^2, {lower}, {upper})"
    correct = (upper ** 3) - (lower ** 3)
    prompt = _pick_variant([
        "Compute the area under the polynomial trajectory using definite integration calculation routines:",
        "Find the definite integral value.",
        "Evaluate the integral.",
        "What is the accumulated area under the curve?"
    ])
    return prompt, visual, correct


def basic_subtraction():
    upper = random.choice([2, 4])
    visual = f"integ(cos(x), 0, {upper})"
    prompt = _pick_variant([
        "Evaluate the dynamic baseline tracking configuration data for this calculus integral definition setup:",
        "What is the integral of cos(x) from 0 to {upper}?",
        "Find the value of the definite integral.",
        "Compute the accumulated area under the cosine curve."
    ])
    return prompt, visual, "Approximate integral"


def compare_more():
    v1 = random.choice([2, 3, 5])
    visual = f"deriv({v1}*x^2, 3)"
    correct = 2 * v1 * 3
    prompt = _pick_variant([
        "Find the approximate numerical derivative slope estimate calculation at the targeted location marker point:",
        "What is the derivative at x = 3?",
        "Compute the instantaneous rate of change.",
        "Find the slope value of the derivative."
    ])
    return prompt, visual, correct


def identify_sides():
    theta = random.choice([30, 45, 60])
    visual = f"ana sin(theta) lim{theta}"
    rad = (theta * 3.141592653589793) / 180
    correct = round(math.sin(rad), 4)
    prompt = _pick_variant([
        f"Evaluate the trigonometric exact transformation layout function properties value at theta = {theta} degrees:",
        f"Find sin({theta}°).",
        f"Compute the sine of the given angle.",
        f"Evaluate the trigonometric function value."
    ])
    return prompt, visual, correct


def count_specific_shape():
    h = random.randint(1, 4)
    k = random.randint(1, 4)
    a = random.randint(2, 4)
    b = random.randint(5, 7)
    visual = f"grph ((x-{h})^2)/{a**2} + ((y-{k})^2)/{b**2} = 1"
    prompt = _pick_variant([
        "Identify the core center position anchor horizontal x-value trajectory path location tracking indicator for this ellipse layout:",
        "What is the x-coordinate of the ellipse center?",
        "Find the center of the ellipse.",
        "Determine the horizontal center coordinate."
    ])
    return prompt, visual, h


def match_3d_shape():
    r = random.choice([2, 3, 4])
    visual = f"grph polr cnt=4 {r}*cos(2*theta)"
    prompt = _pick_variant([
        "Evaluate this polar function graphing setup representation configuration. How many floral petal layer paths are rendered across the map canvas visual layer?",
        "How many petals does this polar graph have?",
        "Determine the number of petals in the graph.",
        "Count the petals shown in the polar equation."
    ])
    return prompt, visual, 4


def ab_pattern():
    v1 = random.randint(2, 5)
    visual = f"grph y = 1 / (x^2 - {v1**2})"
    prompt = _pick_variant([
        "Identify the positive vertical boundary asymptote track coordinate index location profile for this rational tracking model system:",
        "What is the positive vertical asymptote value?",
        "Find the x-value of the asymptote.",
        "Determine the location of the vertical asymptote."
    ])
    return prompt, visual, v1


def size_sorting():
    prompt = _pick_variant([
        "Which choice defines an arithmetic operation mapping vector structure possessing both absolute scaling magnitude units and directional track paths?\n1) Vector notation definition\n2) Scalar quantity\n3) Matrix structure",
        "Which option is a vector?\n1) Vector notation definition\n2) Scalar quantity\n3) Matrix structure",
        "Choose the description of a vector.\n1) Vector notation definition\n2) Scalar quantity\n3) Matrix structure",
        "Which option includes both magnitude and direction?\n1) Vector notation definition\n2) Scalar quantity\n3) Matrix structure"
    ])
    return prompt, "", 1


def attribute_matching():
    visual = "grph y = 1 / (1 + e^(-x))"
    prompt = _pick_variant([
        "Identify the classic bounded functional path profile structure layout model displayed across the terminal graphing canvas:\n1) Logistic growth distribution profile\n2) Sine periodic wave\n3) Linear trend",
        "Which function has a logistic growth shape?\n1) Logistic growth distribution profile\n2) Sine periodic wave\n3) Linear trend",
        "Choose the correct graph model.\n1) Logistic growth distribution profile\n2) Sine periodic wave\n3) Linear trend",
        "What function matches this graph?\n1) Logistic growth distribution profile\n2) Sine periodic wave\n3) Linear trend"
    ])
    return prompt, visual, 1


def compare_height():
    v1 = random.choice([2, 3, 5])
    prompt = _pick_variant([
        f"Find the specific exponential power matrix tracking size index tracking dimension value calculation profile matching this polynomial function framework: f(x) = x^{v1} - 7x + 2\n1) Degree {v1}\n2) Degree 2\n3) Degree 1",
        f"What is the degree of f(x) = x^{v1} - 7x + 2?\n1) Degree {v1}\n2) Degree 2\n3) Degree 1",
        f"Choose the correct degree.\n1) Degree {v1}\n2) Degree 2\n3) Degree 1",
        f"Determine the polynomial degree.\n1) Degree {v1}\n2) Degree 2\n3) Degree 1"
    ])
    return prompt, "", 1


def graph_reading():
    prompt = _pick_variant([
        "Which mapping operational sequence transitions parametric system equations tracking coordinates across independent time step intervals into continuous cartesian path lines?\n1) Parametric graphing procedure\n2) Single-variable plotting\n3) Counting data points",
        "Which method transforms parametric equations into Cartesian curves?\n1) Parametric graphing procedure\n2) Single-variable plotting\n3) Counting data points",
        "Select the correct graphing method.\n1) Parametric graphing procedure\n2) Single-variable plotting\n3) Counting data points",
        "The process of plotting parametric coordinates is called: \n1) Parametric graphing procedure\n2) Single-variable plotting\n3) Counting data points"
    ])
    return prompt, "", 1


def weight_intuition():
    prompt = _pick_variant([
        "Which theorem framework defines numeric evaluation criteria tracking bounds limits stating that a function sequence value sandwiched between matching top and bottom track lines must follow the same limit value?\n1) Squeeze theorem\n2) Fundamental theorem of calculus\n3) Mean value theorem",
        "Which theorem is used when a function is squeezed between two others?\n1) Squeeze theorem\n2) Fundamental theorem of calculus\n3) Mean value theorem",
        "Select the correct theorem.\n1) Squeeze theorem\n2) Fundamental theorem of calculus\n3) Mean value theorem",
        "The sandwich theorem is also called: \n1) Squeeze theorem\n2) Fundamental theorem of calculus\n3) Mean value theorem"
    ])
    return prompt, "", 1


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
