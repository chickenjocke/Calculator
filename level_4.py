import random


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    v1 = random.randint(1000, 9999)
    v2 = random.randint(1000, 9999)
    prompt = _pick_variant([
        "Solve the addition problem:",
        "Add these numbers together:",
        "Find the sum of the values:",
        "What is the total of these two numbers?"
    ])
    return prompt, f"  {v1}\n+ {v2}\n------", v1 + v2


def count_items_5_10():
    v1 = random.randint(5000, 9999)
    v2 = random.randint(1000, 4999)
    prompt = _pick_variant([
        "Solve the subtraction problem:",
        "Subtract to find the difference:",
        "Find the result of this subtraction:",
        "What is the difference between these numbers?"
    ])
    return prompt, f"  {v1}\n- {v2}\n------", v1 - v2


def missing_number_sequence():
    v1 = random.randint(10, 99)
    v2 = random.choice([10, 100, 1000])
    prompt = _pick_variant([
        "Multiply the tracking numbers:",
        "Find the product of the numbers:",
        "Solve this multiplication problem:",
        "What is the result when multiplying these values?"
    ])
    return prompt, f"{v1} x {v2} = ____", v1 * v2


def basic_addition():
    v1 = random.randint(12, 85)
    v2 = random.randint(2, 9)
    prompt = _pick_variant([
        "Find the product using long multiplication steps:",
        "Multiply using the standard algorithm:",
        "Compute the product:",
        "What is the result of this multiplication?"
    ])
    return prompt, f"  {v1}\n    x {v2}\n----", v1 * v2


def basic_subtraction():
    dividend = random.randint(40, 99)
    divisor = random.randint(3, 7)
    quotient = dividend // divisor
    prompt = _pick_variant([
        "Divide the values and find the whole quotient remainder number:",
        "How much is the quotient of this division?",
        "Solve the division and give the whole-number result:",
        "What is the quotient of these numbers?"
    ])
    return prompt, f"{dividend} ÷ {divisor} = ____", quotient


def compare_more():
    v1 = random.randint(100, 999)
    v2 = random.randint(100, 999)
    while v1 == v2:
        v2 = random.randint(100, 999)
    prompt = _pick_variant([
        f"Which statement is correct?\n1) {v1} > {v2}  2) {v1} < {v2}",
        f"Compare the values. Which statement is true?\n1) {v1} > {v2}  2) {v1} < {v2}",
        f"Pick the correct comparison.\n1) {v1} > {v2}  2) {v1} < {v2}",
        f"Which is correct?\n1) {v1} > {v2}  2) {v1} < {v2}"
    ])
    return prompt, "", 1 if v1 > v2 else 2


def identify_sides():
    d = random.choice([10, 100])
    n = random.randint(1, d - 1)
    ans = round(n / d, 2)
    prompt = _pick_variant([
        f"Convert the fraction value to a dynamic decimal notation:",
        f"Write the fraction as a decimal:",
        f"Change this fraction to a decimal:",
        f"What decimal is equivalent to {n}/{d}?"
    ])
    return prompt, f"{n}/{d} = ____", str(ans)


def count_specific_shape():
    d = random.choice([5, 6, 8, 10])
    n1 = random.randint(1, d - 2)
    n2 = random.randint(1, d - n1 - 1)
    prompt = _pick_variant([
        "Add the like-denominator fractions together:",
        "Find the sum of these fractions:",
        "What is the result of this addition?",
        "Compute the total of the two fractions."
    ])
    return prompt, f"{n1}/{d} + {n2}/{d} = ____", f"{n1+n2}/{d}"


def match_3d_shape():
    d = random.choice([5, 6, 8, 10])
    n1 = random.randint(3, d - 1)
    n2 = random.randint(1, n1 - 1)
    prompt = _pick_variant([
        "Subtract the tracking fraction path elements:",
        "Find the difference of these fractions:",
        "Compute the subtraction result:",
        "What is the value of this fraction subtraction?"
    ])
    return prompt, f"{n1}/{d} - {n2}/{d} = ____", f"{n1-n2}/{d}"


def ab_pattern():
    v = random.choice([30, 45, 60, 90, 120, 135, 150])
    cat = "Acute" if v < 90 else ("Right" if v == 90 else "Obtuse")
    prompt = _pick_variant([
        f"An angle tracking measurement is {v} degrees. What type of angle is it?\n1) Acute  2) Right  3) Obtuse",
        f"Classify this angle: {v} degrees.\n1) Acute  2) Right  3) Obtuse",
        f"What kind of angle measures {v} degrees?\n1) Acute  2) Right  3) Obtuse",
        f"Determine the angle type for {v} degrees.\n1) Acute  2) Right  3) Obtuse"
    ])
    return prompt, "", 1 if cat == "Acute" else (2 if cat == "Right" else 3)


def size_sorting():
    prompt = _pick_variant([
        "Which geometric term describes a straight path that starts at one endpoint and goes on forever in one direction?\n1) Line  2) Ray  3) Segment",
        "Choose the correct geometric term.\n1) Line  2) Ray  3) Segment",
        "Which option is a ray?\n1) Line  2) Ray  3) Segment",
        "A line that begins at one endpoint and continues forever in one direction is called: \n1) Line  2) Ray  3) Segment"
    ])
    return prompt, "", 2


def attribute_matching():
    side = random.randint(3, 12)
    prompt = _pick_variant([
        "Find the total perimeter length of a square configuration if one side length equals:",
        "What is the perimeter of a square with side length:",
        "A square has side length. What is the perimeter?",
        "Compute the perimeter of the square."
    ])
    return prompt, f"Side = {side} cm", side * 4


def compare_height():
    v1 = random.randint(2, 8)
    prompt = _pick_variant([
        f"Convert the measurement unit scale system: How many ounces are in {v1} pounds?",
        f"How many ounces are in {v1} pounds?",
        f"Change {v1} pounds to ounces.",
        f"Use the fact that 1 pound = 16 ounces. What is {v1} pounds in ounces?"
    ])
    return prompt, "Hint: 1 pound = 16 ounces", v1 * 16


def graph_reading():
    v1 = random.randint(2, 6)
    prompt = _pick_variant([
        f"Convert the geometric length units: How many feet are in {v1} yards?",
        f"How many feet is {v1} yards?",
        f"Use 1 yard = 3 feet. What is {v1} yards in feet?",
        f"Change {v1} yards to feet."
    ])
    return prompt, "Hint: 1 yard = 3 feet", v1 * 3


def weight_intuition():
    length = random.randint(5, 12)
    width = random.randint(3, 8)
    prompt = _pick_variant([
        "Find the total geometric area boundaries value of a rectangle element frame:",
        "What is the area of this rectangle?",
        "Calculate the area using the given dimensions:",
        "Find the rectangle area with the listed length and width."
    ])
    return prompt, f"Length = {length} meters, Width = {width} meters", length * width


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
