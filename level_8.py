import random


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    m = random.choice([2, 3, 4, 5, -2, -3])
    b = random.choice([1, 2, 3, 4, -1, -2])
    visual = f"grph y = {m}*x + {b}"
    prompt = _pick_variant([
        "Identify the y-intercept value from the given linear function graphing setup:",
        "What is the y-intercept of this graph?",
        "Find the value where the line crosses the y-axis.",
        "Use the graph to identify the y-intercept."
    ])
    return prompt, visual, b


def count_items_5_10():
    m = random.choice([2, 3, 4, 5, -2, -3])
    b = random.choice([1, 2, 3, 4, -1, -2])
    visual = f"grph y = {m}*x + {b}"
    prompt = _pick_variant([
        "Identify the slope calculation rate (m) from the active function graphing layout:",
        "What is the slope of this line?",
        "Find the rate of change for the line.",
        "Determine the slope from the graph equation."
    ])
    return prompt, visual, m


def missing_number_sequence():
    x = random.choice([2, 3, 4, -2, -3])
    y = random.choice([1, 2, 5, -1, -4])
    c1 = 2 * x + y
    c2 = x - y
    visual = f"grph 2*x + y = {c1}; x - y = {c2}"
    prompt = _pick_variant([
        "Find the horizontal x-axis component for the intersection root point solution coordinates of this multi-variable system:",
        "Solve the system and identify the x-value at the intersection.",
        "What is the x-coordinate of the intersection point?",
        "Find the x-value where the lines intersect."
    ])
    return prompt, visual, x


def basic_addition():
    base = random.randint(2, 5)
    exp1 = random.randint(2, 4)
    exp2 = random.randint(2, 4)
    visual = f"{base}^{exp1} * {base}^{exp2} = {base}^____"
    prompt = _pick_variant([
        "Apply exponent expansion rules to find the missing exponent index sum value:",
        "What exponent completes this equation?",
        "Use the exponent rules to solve for the missing exponent.",
        "Find the value needed to complete the power law."
    ])
    return prompt, visual, exp1 + exp2


def basic_subtraction():
    base = random.randint(2, 5)
    exp1 = random.randint(5, 8)
    exp2 = random.randint(2, 4)
    visual = f"{base}^{exp1} / {base}^{exp2} = {base}^____"
    prompt = _pick_variant([
        "Apply quotient power reduction rules to find the missing exponent subtraction outcome value:",
        "What exponent makes this quotient rule true?",
        "Use the quotient of powers rule to solve for the missing exponent.",
        "Determine the exponent difference here."
    ])
    return prompt, visual, exp1 - exp2


def compare_more():
    v = random.randint(2, 8)
    prompt = _pick_variant([
        f"Rewrite the root calculation configuration into equivalent scientific notation string properties: {v}0000\n1) {v} * 10^4  2) {v} * 10^-4  3) {v} * 10^5",
        f"Which scientific notation matches {v}0000?\n1) {v} * 10^4  2) {v} * 10^-4  3) {v} * 10^5",
        f"Choose the correct scientific notation form.\n1) {v} * 10^4  2) {v} * 10^-4  3) {v} * 10^5",
        f"Select the equivalent scientific notation for {v}0000.\n1) {v} * 10^4  2) {v} * 10^-4  3) {v} * 10^5"
    ])
    return prompt, "", 1


def identify_sides():
    a = 3
    b = 4
    visual = f"grph seg(0,0)({a},0) seg({a},0)({a},{b}) seg(0,0)({a},{b})"
    prompt = _pick_variant([
        "Use the Pythagorean theorem properties to compute the hypotenuse vector distance calculation across the grid path:",
        "What is the length of the hypotenuse?",
        "Find the distance across the right triangle.",
        "Use the Pythagorean theorem to solve for the hypotenuse."
    ])
    return prompt, visual, 5


def count_specific_shape():
    r = random.choice([2, 3, 4, 5])
    visual = f"Cylinder profile: radius = {r} cm, height = 10 cm"
    prompt = _pick_variant([
        "Calculate the total interior structural capacity metric volume calculation output: Volume = 3.14 * r^2 * h",
        "What is the volume of the cylinder?",
        "Find the volume using the given radius and height.",
        "Compute the cylinder’s capacity."
    ])
    return prompt, visual, int(3.14 * r * r * 10)


def match_3d_shape():
    r = random.choice([2, 3, 4])
    visual = f"Sphere core: radius = {r} cm"
    prompt = _pick_variant([
        "Find the cubic structural capacity volume calculation metric profile output: Volume = (4/3) * 3.14 * r^3",
        "What is the sphere’s volume?",
        "Compute the volume of the sphere.",
        "Find the capacity of the sphere using the radius."
    ])
    return prompt, visual, int((4 / 3) * 3.14 * (r ** 3))


def ab_pattern():
    visual = "grph pnt(1,2) pnt(2,4) pnt(3,5) pnt(4,7) pnt(5,8) pnt(6,10)"
    prompt = _pick_variant([
        "Evaluate this data tracking plot. What line distribution pattern does it model?\n1) Positive linear association  2) Negative association  3) Non-linear transformation",
        "Which description matches the plotted data?\n1) Positive linear association  2) Negative association  3) Non-linear transformation",
        "Pick the correct pattern for this graph.\n1) Positive linear association  2) Negative association  3) Non-linear transformation",
        "What trend does the data show?\n1) Positive linear association  2) Negative association  3) Non-linear transformation"
    ])
    return prompt, visual, 1


def size_sorting():
    prompt = _pick_variant([
        "Which mapping constraint sequence defines a valid functional distribution rule relationship?\n1) Each single tracking input value maps to exactly one unique output value\n2) One tracking input can have multiple outputs\n3) Outputs are always equal for all inputs",
        "Choose the correct definition of a function.\n1) Each single tracking input value maps to exactly one unique output value\n2) One tracking input can have multiple outputs\n3) Outputs are always equal for all inputs",
        "Which statement is true about functions?\n1) Each single tracking input value maps to exactly one unique output value\n2) One tracking input can have multiple outputs\n3) Outputs are always equal for all inputs",
        "Select the valid function rule.\n1) Each single tracking input value maps to exactly one unique output value\n2) One tracking input can have multiple outputs\n3) Outputs are always equal for all inputs"
    ])
    return prompt, "", 1


def attribute_matching():
    v1 = random.randint(2, 5)
    prompt = _pick_variant([
        f"Solve the single-variable multi-step tracking equation calculation: {v1}x + 2 = {v1}x + 5\n1) Infinitely many solutions  2) No solution  3) x = 0",
        f"What type of solution does {v1}x + 2 = {v1}x + 5 have?\n1) Infinitely many solutions  2) No solution  3) x = 0",
        f"Choose the correct result.\n1) Infinitely many solutions  2) No solution  3) x = 0",
        f"Interpret the equation: {v1}x + 2 = {v1}x + 5.\n1) Infinitely many solutions  2) No solution  3) x = 0"
    ])
    return prompt, "", 2


def compare_height():
    v1 = random.randint(2, 5)
    prompt = _pick_variant([
        f"Solve the linear balanced sequence layout structural value calculation: {v1}x + 4 = {v1}x + 4\n1) Infinitely many solutions  2) No solution  3) x = 4",
        f"What is the solution to {v1}x + 4 = {v1}x + 4?\n1) Infinitely many solutions  2) No solution  3) x = 4",
        f"Choose the correct classification.\n1) Infinitely many solutions  2) No solution  3) x = 4",
        f"What kind of solution does the equation have?\n1) Infinitely many solutions  2) No solution  3) x = 4"
    ])
    return prompt, "", 1


def graph_reading():
    prompt = _pick_variant([
        "Which choice defines an irrational real number value configuration data property?\n1) Square root of 2  2) Square root of 9  3) 0.75",
        "Which number is irrational?\n1) Square root of 2  2) Square root of 9  3) 0.75",
        "Select the irrational value.\n1) Square root of 2  2) Square root of 9  3) 0.75",
        "Which option is not rational?\n1) Square root of 2  2) Square root of 9  3) 0.75"
    ])
    return prompt, "", 1


def weight_intuition():
    prompt = _pick_variant([
        "Which geometric sequence dynamic changes properties when a triangle experiences a rigid coordinate transformation translation shift?\n1) Exterior angle paths orientation rotation data\n2) Side lengths change\n3) Angles and side lengths stay the same",
        "What happens to a triangle under a translation?\n1) Exterior angle paths orientation rotation data\n2) Side lengths change\n3) Angles and side lengths stay the same",
        "Choose the correct result of translation.\n1) Exterior angle paths orientation rotation data\n2) Side lengths change\n3) Angles and side lengths stay the same",
        "A translated triangle keeps what property?\n1) Exterior angle paths orientation rotation data\n2) Side lengths change\n3) Angles and side lengths stay the same"
    ])
    return prompt, "", 3


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
