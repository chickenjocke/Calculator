import random

def count_items_1_6():
    v1 = random.randint(1000, 9999)
    v2 = random.randint(1000, 9999)
    return "Solve the addition problem:", f"  {v1}\n+ {v2}\n------", v1 + v2

def count_items_5_10():
    v1 = random.randint(5000, 9999)
    v2 = random.randint(1000, 4999)
    return "Solve the subtraction problem:", f"  {v1}\n- {v2}\n------", v1 - v2

def missing_number_sequence():
    v1 = random.randint(10, 99)
    v2 = random.choice([10, 100, 1000])
    return "Multiply the tracking numbers:", f"{v1} x {v2} = ____", v1 * v2

def basic_addition():
    v1 = random.randint(12, 85)
    v2 = random.randint(2, 9)
    return "Find the product using long multiplication steps:", f"  {v1}\n外部 x {v2}\n----", v1 * v2

def basic_subtraction():
    dividend = random.randint(40, 99)
    divisor = random.randint(3, 7)
    quotient = dividend // divisor
    return "Divide the values and find the whole quotient remainder number:", f"{dividend} ÷ {divisor} = ____", quotient

def compare_more():
    v1 = random.randint(100, 999)
    v2 = random.randint(100, 999)
    while v1 == v2:
        v2 = random.randint(100, 999)
    return f"Which statement is correct?\n1) {v1} > {v2}  2) {v1} < {v2}", "", 1 if v1 > v2 else 2

def identify_sides():
    d = random.choice([10, 100])
    n = random.randint(1, d - 1)
    ans = round(n / d, 2)
    return "Convert the fraction value to a dynamic decimal notation:", f"{n}/{d} = ____", str(ans)

def count_specific_shape():
    d = random.choice([5, 6, 8, 10])
    n1 = random.randint(1, d - 2)
    n2 = random.randint(1, d - n1 - 1)
    return "Add the like-denominator fractions together:", f"{n1}/{d} + {n2}/{d} = ____", f"{n1+n2}/{d}"

def match_3d_shape():
    d = random.choice([5, 6, 8, 10])
    n1 = random.randint(3, d - 1)
    n2 = random.randint(1, n1 - 1)
    return "Subtract the tracking fraction path elements:", f"{n1}/{d} - {n2}/{d} = ____", f"{n1-n2}/{d}"

def ab_pattern():
    v = random.choice([30, 45, 60, 90, 120, 135, 150])
    cat = "Acute" if v < 90 else ("Right" if v == 90 else "Obtuse")
    return f"An angle tracking measurement is {v} degrees. What type of angle is it?\n1) Acute  2) Right  3) Obtuse", "", 1 if cat == "Acute" else (2 if cat == "Right" else 3)

def size_sorting():
    return "Which geometric term describes a straight path that starts at one endpoint and goes on forever in one direction?\n1) Line  2) Ray  3) Segment", "", 2

def attribute_matching():
    side = random.randint(3, 12)
    return "Find the total perimeter length of a square configuration if one side length equals:", f"Side = {side} cm", side * 4

def compare_height():
    v1 = random.randint(2, 8)
    return f"Convert the measurement unit scale system: How many ounces are in {v1} pounds?", "Hint: 1 pound = 16 ounces", v1 * 16

def graph_reading():
    v1 = random.randint(2, 6)
    return f"Convert the geometric length units: How many feet are in {v1} yards?", "Hint: 1 yard = 3 feet", v1 * 3

def weight_intuition():
    length = random.randint(5, 12)
    width = random.randint(3, 8)
    return "Find the total geometric area boundaries value of a rectangle element frame:", f"Length = {length} meters, Width = {width} meters", length * width

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
