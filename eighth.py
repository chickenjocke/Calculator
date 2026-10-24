import random

def count_items_1_6():
    m = random.choice([2, 3, 4, 5, -2, -3])
    b = random.choice([1, 2, 3, 4, -1, -2])
    visual = f"grph y = {m}*x + {b}"
    return "Identify the y-intercept value from the given linear function graphing setup:", visual, b

def count_items_5_10():
    m = random.choice([2, 3, 4, 5, -2, -3])
    b = random.choice([1, 2, 3, 4, -1, -2])
    visual = f"grph y = {m}*x + {b}"
    return "Identify the slope calculation rate (m) from the active function graphing layout:", visual, m

def missing_number_sequence():
    x = random.choice([2, 3, 4, -2, -3])
    y = random.choice([1, 2, 5, -1, -4])
    c1 = 2 * x + y
    c2 = x - y
    visual = f"grph 2*x + y = {c1}; x - y = {c2}"
    return "Find the horizontal x-axis component for the intersection root point solution coordinates of this multi-variable system:", visual, x

def basic_addition():
    base = random.randint(2, 5)
    exp1 = random.randint(2, 4)
    exp2 = random.randint(2, 4)
    visual = f"{base}^{exp1} * {base}^{exp2} = {base}^____"
    return "Apply exponent expansion rules to find the missing exponent index sum value:", visual, exp1 + exp2

def basic_subtraction():
    base = random.randint(2, 5)
    exp1 = random.randint(5, 8)
    exp2 = random.randint(2, 4)
    visual = f"{base}^{exp1} / {base}^{exp2} = {base}^____"
    return "Apply quotient power reduction rules to find the missing exponent subtraction outcome value:", visual, exp1 - exp2

def compare_more():
    v = random.randint(2, 8)
    return f"Rewrite the root calculation configuration into equivalent scientific notation string properties: {v}0000\n1) {v} * 10^4  2) {v} * 10^-4  3) {v} * 10^5", "", 1

def identify_sides():
    a = 3
    b = 4
    visual = f"grph seg(0,0)({a},0) seg({a},0)({a},{b}) seg(0,0)({a},{b})"
    return "Use the Pythagorean theorem properties to compute the hypotenuse vector distance calculation across the grid path:", visual, 5

def count_specific_shape():
    r = random.choice([2, 3, 4, 5])
    visual = f"Cylinder profile: radius = {r} cm, height = 10 cm"
    return "Calculate the total interior structural capacity metric volume calculation output: Volume = 3.14 * r^2 * h", visual, int(3.14 * r * r * 10)

def match_3d_shape():
    r = random.choice([2, 3, 4])
    visual = f"Sphere core: radius = {r} cm"
    return "Find the cubic structural capacity volume calculation metric profile output: Volume = (4/3) * 3.14 * r^3", visual, int((4 / 3) * 3.14 * (r ** 3))

def ab_pattern():
    visual = "grph pnt(1,2) pnt(2,4) pnt(3,5) pnt(4,7) pnt(5,8) pnt(6,10)"
    return "Evaluate this data tracking plot. What line distribution pattern does it model?\n1) Positive linear association  2) Negative association  3) Non-linear transformation", visual, 1

def size_sorting():
    prompt = "Which mapping constraint sequence defines a valid functional distribution rule relationship?\n1) Each single tracking input value maps to exactly one unique output value\n2) One tracking input coordinates set maps simultaneously to multiple outcomes\n3) Output paths exist with no corresponding input location metrics"
    return prompt, "", 1

def attribute_matching():
    v1 = random.randint(2, 5)
    return f"Solve the single-variable multi-step tracking equation calculation: {v1}x + 2 = {v1}x + 5\n1) Infinitely many solutions  2) No solution  3) x = 0", "", 2

def compare_height():
    v1 = random.randint(2, 5)
    return f"Solve the linear balanced sequence layout structural value calculation: {v1}x + 4 = {v1}x + 4\n1) Infinitely many solutions  2) No solution  3) x = 4", "", 1

def graph_reading():
    prompt = "Which choice defines an irrational real number value configuration data property?\n1) Square root of 2  2) Square root of 9  3) 0.75"
    return prompt, "", 1

def weight_intuition():
    prompt = "Which geometric sequence dynamic changes properties when a triangle experiences a rigid coordinate transformation translation shift?\n1) Exterior angle paths orientation rotation data\n2) Linear side edge distance dimensions metric scale\n3) The spatial tracking location coordinates position across the grid frame map"
    return prompt, "", 3

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
