import random
import math

def count_items_1_6():
    num = random.choice([2, 4, 5])
    denom = random.choice([3, 4, 6])
    visual = f"lmt(x->0)(sin({num}*x)/(sin({denom}*x)))"
    return "Evaluate the trigonometric function configuration limit as x approaches zero using limit calculation tools:", visual, f"{num}/{denom}"

def count_items_5_10():
    num = random.choice([2, 3, 4])
    visual = f"lmt(x->2)((x^2 - {num*2}*x + {num*2}) / (x - 2))"
    return "Evaluate the rational expression limit function properties using the removable discontinuity resolution engine:", visual, "undefined"

def missing_number_sequence():
    v1 = random.choice([4, 9, 16])
    visual = f"sum(n^2, n, 1, {v1})"
    return "Find the total calculated output string properties for this structural summation sigma sequence expression operation track:", visual, "Sigma sum"

def basic_addition():
    lower = random.choice([0, 1])
    upper = random.randint(2, 4)
    visual = f"integ(3*x^2, {lower}, {upper})"
    correct = (upper ** 3) - (lower ** 3)
    return "Compute the area under the polynomial trajectory using definite integration calculation routines:", visual, correct

def basic_subtraction():
    upper = random.choice([2, 4])
    visual = f"integ(cos(x), 0, {upper})"
    return "Evaluate the dynamic baseline tracking configuration data for this calculus integral definition setup:", visual, "Approximate integral"

def compare_more():
    v1 = random.choice([2, 3, 5])
    visual = f"deriv({v1}*x^2, 3)"
    correct = 2 * v1 * 3
    return "Find the approximate numerical derivative slope estimate calculation at the targeted location marker point:", visual, correct

def identify_sides():
    theta = random.choice([30, 45, 60])
    visual = f"ana sin(theta) lim{theta}"
    rad = (theta * 3.141592653589793) / 180
    correct = round(math.sin(rad), 4)
    return f"Evaluate the trigonometric exact transformation layout function properties value at theta = {theta} degrees:", visual, correct

def count_specific_shape():
    h = random.randint(1, 4)
    k = random.randint(1, 4)
    a = random.randint(2, 4)
    b = random.randint(5, 7)
    visual = f"grph ((x-{h})^2)/{a**2} + ((y-{k})^2)/{b**2} = 1"
    return "Identify the core center position anchor horizontal x-value trajectory path location tracking indicator for this ellipse layout:", visual, h

def match_3d_shape():
    r = random.choice([2, 3, 4])
    visual = f"grph polr cnt=4 {r}*cos(2*theta)"
    return "Evaluate this polar function graphing setup representation configuration. How many floral petal layer paths are rendered across the map canvas visual layer?", visual, 4

def ab_pattern():
    v1 = random.randint(2, 5)
    visual = f"grph y = 1 / (x^2 - {v1**2})"
    return "Identify the positive vertical boundary asymptote track coordinate index location profile for this rational tracking model system:", visual, v1

def size_sorting():
    prompt = "Which choice defines an arithmetic operation mapping vector structure possessing both absolute scaling magnitude units and directional track paths?\n1) Vector notation definition\n2) Matrix transformation row\n3) Scalar coordinate multiplier"
    return prompt, "", 1

def attribute_matching():
    visual = "grph y = 1 / (1 + e^(-x))"
    return "Identify the classic bounded functional path profile structure layout model displayed across the terminal graphing canvas:\n1) Logistic growth distribution profile\n2) Sine periodic wave sequence\n3) Absolute value convergence tracking", visual, 1

def compare_height():
    v1 = random.choice([2, 3, 5])
    return f"Find the specific exponential power matrix tracking size index tracking dimension value calculation profile matching this polynomial function framework: f(x) = x^{v1} - 7x + 2\n1) Degree parameter value equals {v1}\n2) Rational coefficient limits match zero\n3) Linear root transformation count matches one", "", 1

def graph_reading():
    prompt = "Which mapping operational sequence transitions parametric system equations tracking coordinates across independent time step intervals into continuous cartesian path lines?\n1) Parameter elimination conversion rules\n2) Matrix multiplication dot product arrays\n3) Exponent summation transformation logic"
    return prompt, "", 1

def weight_intuition():
    prompt = "Which theorem framework defines numeric evaluation criteria tracking bounds limits stating that a function sequence value sandwiched between matching top and bottom track lines must converge precisely upon that shared destination point?\n1) Squeeze/Sandwich limiting structural theorem\n2) Fundamental calculus continuity baseline\n3) Removable discontinuity validation protocol"
    return prompt, "", 1

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
