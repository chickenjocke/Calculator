import random

def count_items_1_6():
    num = random.choice([2, 3, 4, 5])
    visual = f"lmt(x->3)((x^2 - {num+3}*x + {num*3}) / (x - 3))"
    return "Evaluate the limit analytically by canceling the removable discontinuity hole factor:", visual, num - 3

def count_items_5_10():
    power = random.randint(2, 5)
    visual = f"lmt(x->pi)((x^{power}) / (e^x))"
    return "Evaluate the continuous limit using direct substitution property guidelines:", visual, "Limit could not be determined"

def missing_number_sequence():
    v1 = random.choice([1, 2, 3])
    visual = f"lmt(x->0)(sin({v1}*x)/x)"
    return "Find the exact horizontal vector target limit value using the special trigonometric limit identities property:", visual, v1

def basic_addition():
    lower = random.choice([0, 1, 2])
    upper = random.choice([3, 4, 5])
    coef = random.choice([2, 3, 4])
    visual = f"integ({coef}*x, {lower}, {upper})"
    ans = int((0.5 * coef * (upper**2)) - (0.5 * coef * (lower**2)))
    return "Find the area accumulation under the curve using the First Fundamental Theorem of Calculus:", visual, ans

def basic_subtraction():
    upper = random.choice([1, 2, 3])
    visual = f"integ(e^x, 0, {upper})"
    return "Evaluate the definite integral representation property for this exponential tracking curve layout:", visual, "Approximate integral"

def compare_more():
    v1 = random.choice([2, 3, 4])
    pt = random.choice([1, 2, 3])
    visual = f"deriv({v1}*x^3, {pt})"
    ans = 3 * v1 * (pt**2)
    return "Find the exact instantaneous rate of change (derivative slope value) at the targeted location coordinate point:", visual, ans

def identify_sides():
    v1 = random.choice([4, 5, 6])
    pt = random.choice([2, 3, 4])
    visual = f"deriv(ln(x), {pt})"
    return "Compute the numerical derivative estimate for this transcendental function pathway layout sequence:", visual, "Approximate derivative"

def count_specific_shape():
    h = random.randint(1, 4)
    k = random.randint(1, 4)
    visual = f"grph y = (x - {h})^2 + {k}"
    return "Find the critical stationary point local minimum coordinate horizontal x-value position where the derivative equals zero:", visual, h

def match_3d_shape():
    visual = "grph y = x^3 - 3*x"
    return "Find the tracking inflection point x-axis coordinate position location where concavity changes polarity:\n1) x = 0\n2) x = 1\n3) x = -1", visual, 1

def ab_pattern():
    v1 = random.choice([2, 3, 4])
    visual = f"sum((1/{v1})^n, n, 1, 100)"
    return "Evaluate the convergence trajectory output value for this infinite geometric progression summation series series path:", visual, "Sigma sum"

def size_sorting():
    prompt = "Which validation protocol confirms a function profile is fully differentiable across a closed interval tracking window?\n1) It must maintain strict continuity without corner kinks, cusps, or vertical tangent paths\n2) The aggregate area boundaries sum matches zero\n3) The horizontal root trajectory intercepts match the origin"
    return prompt, "", 1

def attribute_matching():
    prompt = "Which theorem confirms a continuous function on a closed interval must achieve its average slope value at some interior point?\n1) Mean Value Theorem (MVT)\n2) Intermediate Value Theorem (IVT)\n3) L'Hopital's Rule limit optimization"
    return prompt, "", 1

def compare_height():
    prompt = "Which tool optimizes an indeterminate limit sequence (0/0 or inf/inf) by analyzing the derivative profiles of its numerator and denominator tracks?\n1) L'Hopital's Rule validation sequence\n2) Riemann sum partition tracking matrices\n3) Taylor polynomial series expansion framework"
    return prompt, "", 1

def graph_reading():
    prompt = "Which calculus concept accumulates total volumetric capacities by sweeping nested cross-sectional slicing frames across a path range?\n1) Disk/Washer solid revolution integration rules\n2) Power rule differentiation sequences\n3) Newton-Raphson approximation iterations"
    return prompt, "", 1

def weight_intuition():
    prompt = "Which sequence configuration represents a function track using an infinite summation series built out of tracking polynomial power variables centered around zero?\n1) Maclaurin series expansion model\n2) Fourier cyclic oscillation path sequence\n3) Alternating rational difference series tracker"
    return prompt, "", 1

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
