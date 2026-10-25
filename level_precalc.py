import random
import math


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    h = random.randint(1, 5)
    k = random.randint(-4, 4)
    visual = f"grph y = log(x - {h}) + {k}"
    prompt = _pick_variant([
        "Identify the vertical asymptote boundary line position coordinate x-value for this logarithmic function configuration:",
        "What is the vertical asymptote x-value for this log graph?",
        "Find the x-value where the graph has its vertical asymptote.",
        "Determine the vertical asymptote of the logarithmic function."
    ])
    return prompt, visual, h


def count_items_5_10():
    h = random.randint(-3, 3)
    k = random.randint(1, 4)
    visual = f"grph y = 1 / (x - {h}) + {k}"
    prompt = _pick_variant([
        "Identify the horizontal asymptote boundary layer position coordinate y-value for this rational distribution setup:",
        "What is the horizontal asymptote y-value for this graph?",
        "Find the y-value of the horizontal asymptote.",
        "Determine the horizontal asymptote of the rational function."
    ])
    return prompt, visual, k


def missing_number_sequence():
    v1 = random.choice([4, 9, 16, 25])
    visual = f"Solve the radical variable isolation calculation parameter: sqrt(x) = {int(v1**0.5)}"
    prompt = _pick_variant([
        "Compute the value of x that satisfies the basic radical function equation:",
        "Solve for x in the square root equation.",
        "What value of x makes the equation true?",
        "Find the x-value for the radical equation."
    ])
    return prompt, visual, v1


def basic_addition():
    r = random.choice([2, 3, 5])
    theta = random.choice([30, 45, 60, 90])
    rad = (theta * 3.14159) / 180
    x = round(r * math.cos(rad), 2)
    visual = f"grph polr cnt=1 theta sin(theta) with points at angle {theta}"
    prompt = _pick_variant([
        f"Convert the polar position parameters (r={r}, theta={theta} degrees) into a Cartesian horizontal x-coordinate location path:",
        f"Find the x-coordinate for the polar point.",
        f"Convert this polar point to Cartesian x-value.",
        f"What is the x-coordinate of this point?"
    ])
    return prompt, visual, x


def basic_subtraction():
    a = random.choice([1, 2])
    h = random.randint(-2, 2)
    k = random.randint(-2, 2)
    visual = f"grph y = {a}*(x - {h})^3 + {k}"
    prompt = _pick_variant([
        "Identify the transformation inflection point anchor horizontal x-value coordinate for this cubic polynomial track:",
        "What is the x-value of the inflection point?",
        "Find the x-coordinate of the cubic’s inflection point.",
        "Determine the inflection point x-value."
    ])
    return prompt, visual, h


def compare_more():
    v1 = random.randint(2, 4)
    v2 = random.randint(2, 3)
    ans = v1 ** v2
    prompt = _pick_variant([
        f"Apply exponential conversion rule tracking properties: Solve log_{v1}(x) = {v2}",
        f"Find x in the logarithmic equation.",
        f"Solve for the value of x.",
        f"What value makes this logarithm equation true?"
    ])
    return prompt, "", ans


def identify_sides():
    v1 = random.randint(2, 5)
    prompt = _pick_variant([
        f"Evaluate the imaginary component unit operations format values: Find the simplified numerical evaluation for the loop pattern i^{v1 * 4}",
        f"Simplify the imaginary power expression.",
        f"What is the value of i raised to the given power?",
        f"Evaluate this complex number power."
    ])
    return prompt, "", 1


def count_specific_shape():
    r1 = random.randint(2, 4)
    r2 = random.randint(5, 7)
    visual = f"grph y = sqrt({r1}*x); y = sqrt({r2}*x)"
    prompt = _pick_variant([
        "Determine the total intersection root count value for these two starting radical function tracks matching at the origin:",
        "How many intersections do these radical graphs share?",
        "Count the intersection points of the two graphs.",
        "Determine the number of common points."
    ])
    return prompt, visual, 1


def match_3d_shape():
    h = random.randint(1, 4)
    k = random.randint(1, 4)
    r = random.choice([3, 4, 5])
    visual = f"grph (x - {h})^2 + (y - {k})^2 = {r**2}"
    prompt = _pick_variant([
        "Identify the matching center position anchor horizontal x-value path tracking component for this geometric circle layout profile:",
        "What is the x-coordinate of the circle center?",
        "Find the center x-value of the circle.",
        "Determine the x-coordinate of the center."
    ])
    return prompt, visual, h


def ab_pattern():
    prompt = _pick_variant([
        "Which choice defines an even functional profile distribution mirroring perfectly across the vertical y-axis tracking plane?\n1) f(x) = x^2\n2) f(x) = x^3\n3) f(x) = x + 1",
        "Which function is even?\n1) f(x) = x^2\n2) f(x) = x^3\n3) f(x) = x + 1",
        "Select the even function.\n1) f(x) = x^2\n2) f(x) = x^3\n3) f(x) = x + 1",
        "Choose the graph that is symmetric about the y-axis.\n1) f(x) = x^2\n2) f(x) = x^3\n3) f(x) = x + 1"
    ])
    return prompt, "", 1


def size_sorting():
    prompt = _pick_variant([
        "Which parent reference representation track models a cyclic transformation pattern repeating wave intervals over constant periods?\n1) Sine function wave configuration\n2) Exponential growth function\n3) Linear function",
        "Which function has a repeating wave pattern?\n1) Sine function wave configuration\n2) Exponential growth function\n3) Linear function",
        "Select the periodic function.\n1) Sine function wave configuration\n2) Exponential growth function\n3) Linear function",
        "Which option best models a periodic wave?\n1) Sine function wave configuration\n2) Exponential growth function\n3) Linear function"
    ])
    return prompt, "", 1


def attribute_matching():
    v1 = random.randint(2, 5)
    prompt = _pick_variant([
        f"Find the common ratio multiplier constant calculation rule metric details for this geometric structural sequence progression: {v1}, {v1*3}, {v1*9}, {v1*27}",
        f"What is the common ratio in this sequence? {v1}, {v1*3}, {v1*9}, {v1*27}",
        f"Determine the ratio between terms in the sequence.",
        f"What multiplier repeats in this geometric sequence?"
    ])
    return prompt, "", 3


def compare_height():
    v1 = random.randint(2, 10)
    prompt = _pick_variant([
        f"Find the total count metrics for all potential roots (including complex duplicates) as dictated by the Fundamental Theorem of Algebra: f(x) = x^{v1} - 4x^2 + 1",
        f"How many roots does the polynomial have?",
        f"Use the Fundamental Theorem of Algebra to determine the number of roots.",
        f"Find the degree-based root count for this polynomial."
    ])
    return prompt, "", v1


def graph_reading():
    prompt = _pick_variant([
        "Which standard statistical summary distribution spread layer evaluates parameter deviation variables relative to sample data average baseline levels?\n1) Standard deviation metric calculation\n2) Median value\n3) Mode count",
        "Which measure compares data to the mean by measuring spread?\n1) Standard deviation metric calculation\n2) Median value\n3) Mode count",
        "Choose the standard deviation description.\n1) Standard deviation metric calculation\n2) Median value\n3) Mode count",
        "Which option measures variability around the mean?\n1) Standard deviation metric calculation\n2) Median value\n3) Mode count"
    ])
    return prompt, "", 1


def weight_intuition():
    prompt = _pick_variant([
        "Which function track configuration defines an inverse operations structural pairing conversion partner template relationship for an exponential progression y = b^x?\n1) Logarithmic decay function\n2) Linear function\n3) Quadratic function",
        "What is the inverse of an exponential function?\n1) Logarithmic decay function\n2) Linear function\n3) Quadratic function",
        "Select the inverse function type.\n1) Logarithmic decay function\n2) Linear function\n3) Quadratic function",
        "The inverse of y = b^x is which function type?\n1) Logarithmic decay function\n2) Linear function\n3) Quadratic function"
    ])
    return prompt, "", 1


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
