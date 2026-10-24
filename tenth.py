import random
import math

def count_items_1_6():
    h = random.randint(1, 5)
    k = random.randint(-4, 4)
    visual = f"grph y = log(x - {h}) + {k}"
    return "Identify the vertical asymptote boundary line position coordinate x-value for this logarithmic function configuration:", visual, h

def count_items_5_10():
    h = random.randint(-3, 3)
    k = random.randint(1, 4)
    visual = f"grph y = 1 / (x - {h}) + {k}"
    return "Identify the horizontal asymptote boundary layer position coordinate y-value for this rational distribution setup:", visual, k

def missing_number_sequence():
    v1 = random.choice([4, 9, 16, 25])
    visual = f"Solve the radical variable isolation calculation parameter: sqrt(x) = {int(v1**0.5)}"
    return "Compute the value of x that satisfies the basic radical function equation:", visual, v1

def basic_addition():
    r = random.choice([2, 3, 5])
    theta = random.choice([30, 45, 60, 90])
    rad = (theta * 3.14159) / 180
    x = round(r * math.cos(rad), 2)
    visual = f"grph polr cnt=1 theta sin(theta) with points at angle {theta}"
    return f"Convert the polar position parameters (r={r}, theta={theta} degrees) into a Cartesian horizontal x-coordinate location path:", visual, x

def basic_subtraction():
    a = random.choice([1, 2])
    h = random.randint(-2, 2)
    k = random.randint(-2, 2)
    visual = f"grph y = {a}*(x - {h})^3 + {k}"
    return "Identify the transformation inflection point anchor horizontal x-value coordinate for this cubic polynomial track:", visual, h

def compare_more():
    v1 = random.randint(2, 4)
    v2 = random.randint(2, 3)
    ans = v1 ** v2
    return f"Apply exponential conversion rule tracking properties: Solve log_{v1}(x) = {v2}", "", ans

def identify_sides():
    v1 = random.randint(2, 5)
    return f"Evaluate the imaginary component unit operations format values: Find the simplified numerical evaluation for the loop pattern i^{v1 * 4}", "", 1

def count_specific_shape():
    r1 = random.randint(2, 4)
    r2 = random.randint(5, 7)
    visual = f"grph y = sqrt({r1}*x); y = sqrt({r2}*x)"
    return "Determine the total intersection root count value for these two starting radical function tracks matching at the origin:", visual, 1

def match_3d_shape():
    h = random.randint(1, 4)
    k = random.randint(1, 4)
    r = random.choice([3, 4, 5])
    visual = f"grph (x - {h})^2 + (y - {k})^2 = {r**2}"
    return "Identify the matching center position anchor horizontal x-value path tracking component for this geometric circle layout profile:", visual, h

def ab_pattern():
    prompt = "Which choice defines an even functional profile distribution mirroring perfectly across the vertical y-axis tracking plane?\n1) f(x) = x^2\n2) f(x) = x^3\n3) f(x) = x + 1"
    return prompt, "", 1

def size_sorting():
    prompt = "Which parent reference representation track models a cyclic transformation pattern repeating wave intervals over constant periods?\n1) Sine function wave configuration\n2) Exponential decay trajectory profile\n3) Logarithmic scale distribution baseline"
    return prompt, "", 1

def attribute_matching():
    v1 = random.randint(2, 5)
    return f"Find the common ratio multiplier constant calculation rule metric details for this geometric structural sequence progression: {v1}, {v1*3}, {v1*9}, {v1*27}", "", 3

def compare_height():
    v1 = random.randint(2, 10)
    return f"Find the total count metrics for all potential roots (including complex duplicates) as dictated by the Fundamental Theorem of Algebra: f(x) = x^{v1} - 4x^2 + 1", "", v1

def graph_reading():
    prompt = "Which standard statistical summary distribution spread layer evaluates parameter deviation variables relative to sample data average baseline levels?\n1) Standard deviation metric calculation\n2) Interquartile variance range parameters\n3) Median distribution tracking point"
    return prompt, "", 1

def weight_intuition():
    prompt = "Which function track configuration defines an inverse operations structural pairing conversion partner template relationship for an exponential progression y = b^x?\n1) Logarithmic distribution scale template y = log_b(x)\n2) Rational division inverse layout y = 1/x\n3) Quadratic exponent polynomial pathway y = x^2"
    return prompt, "", 1

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
