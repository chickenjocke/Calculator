import random


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    start = random.randint(100, 900)
    step = random.choice([5, 10, 100])
    sequence = [start + (i * step) for i in range(5)]
    missing_idx = random.randint(1, 4)
    correct = sequence[missing_idx]
    seq_str = [str(x) if i != missing_idx else "___" for i, x in enumerate(sequence)]
    prompt = _pick_variant([
        f"Count skip-counting by {step}. What number is missing?",
        f"Fill in the missing value while counting by {step}.",
        f"Which number belongs in the blank in this skip-count sequence?",
        f"What number is missing from this pattern counting by {step}?"
    ])
    return prompt, " ".join(seq_str), correct


def count_items_5_10():
    hundreds = random.randint(1, 9)
    tens = random.randint(0, 9)
    ones = random.randint(0, 9)
    total = (hundreds * 100) + (tens * 10) + ones
    board = f"Blocks: {hundreds} flats of 100, {tens} rods of 10, and {ones} unit cubes."
    prompt = _pick_variant([
        "What is the standard form number for these base-ten blocks?",
        "Read the base-ten blocks. What number do they show?",
        "How many is this number in standard form?",
        "Write the value shown by these blocks."
    ])
    return prompt, board, total


def missing_number_sequence():
    n1 = random.randint(100, 999)
    n2 = random.randint(100, 999)
    while n1 == n2:
        n2 = random.randint(100, 999)
    prompt = _pick_variant([
        f"Which number statement is true?\n1) {n1} > {n2}  2) {n1} < {n2}",
        f"Compare the numbers. Which is true?\n1) {n1} > {n2}  2) {n1} < {n2}",
        f"Pick the correct comparison.\n1) {n1} > {n2}  2) {n1} < {n2}",
        f"Which expression is correct?\n1) {n1} > {n2}  2) {n1} < {n2}"
    ])
    return prompt, "", 1 if n1 > n2 else 2


def basic_addition():
    v1 = random.randint(10, 90)
    v2 = random.randint(10, 90)
    prompt = _pick_variant([
        "Solve the two-digit addition problem:",
        "Add the numbers together:",
        "Find the sum:",
        "What is the total of these two-digit numbers?"
    ])
    return prompt, f"  {v1}\n+ {v2}\n----", v1 + v2


def basic_subtraction():
    v1 = random.randint(50, 99)
    v2 = random.randint(10, 49)
    prompt = _pick_variant([
        "Solve the two-digit subtraction problem:",
        "Subtract to find the difference:",
        "Find the result:",
        "What is the difference between the numbers?"
    ])
    return prompt, f"  {v1}\n- {v2}\n----", v1 - v2


def compare_more():
    v1 = random.randint(10, 50)
    v2 = random.randint(10, 50)
    v3 = random.randint(10, 50)
    prompt = _pick_variant([
        "Add three numbers together:",
        "Find the sum of these three values:",
        "Combine the numbers and find the total:",
        "What is the total of all three numbers?"
    ])
    return prompt, f"{v1} + {v2} + {v3} = ____", v1 + v2 + v3


def identify_sides():
    hour = random.randint(1, 12)
    minute = random.choice([5, 15, 20, 40, 45, 55])
    time_str = f"{hour}:{minute:02d}"
    clock_desc = f"The short hand is near {hour}. The long hand points directly at the {minute // 5} marker."
    prompt = _pick_variant([
        "What time does this analog clock show?",
        "Read the clock. What time is it?",
        "Which time is displayed on the clock?",
        "Tell the time shown by the analog clock."
    ])
    return prompt, clock_desc, time_str


def count_specific_shape():
    quarters = random.randint(0, 3)
    dimes = random.randint(0, 4)
    nickels = random.randint(0, 5)
    total = (quarters * 25) + (dimes * 10) + (nickels * 5)
    board = f"Wallet contains: {quarters} quarters, {dimes} dimes, and {nickels} nickels."
    prompt = _pick_variant([
        "How many total cents do you have?",
        "Find the total value in cents.",
        "What is the total amount of money shown?",
        "Add the coins together. How much money is that?"
    ])
    return prompt, board, total


def match_3d_shape():
    rows = random.randint(2, 5)
    cols = random.randint(2, 5)
    total = rows * cols
    board = "\n".join(["[■]" * cols for _ in range(rows)])
    prompt = _pick_variant([
        f"Look at this rectangular array. How many blocks are there in total?",
        f"Count all the blocks in this rectangle. How many are there?",
        f"How many squares are in this array altogether?",
        f"What is the total count of the tiles in this array?"
    ])
    return prompt, board, total


def ab_pattern():
    shape = random.choice(["cube", "rectangular prism", "pyramid"])
    faces = {"cube": 6, "rectangular prism": 6, "pyramid": 5}[shape]
    prompt = _pick_variant([
        f"How many flat faces does a {shape} have?",
        f"Count the flat surfaces of a {shape}. How many are there?",
        f"A {shape} has how many flat faces?",
        f"How many faces are flat on a {shape}?"
    ])
    return prompt, "", faces


def size_sorting():
    shape = random.choice(["pentagon", "hexagon", "quadrilateral"])
    sides = {"pentagon": 5, "hexagon": 6, "quadrilateral": 4}[shape]
    prompt = _pick_variant([
        f"How many side paths does a {shape} shape have?",
        f"Count the sides of a {shape}. How many are there?",
        f"How many sides does a {shape} have?",
        f"A {shape} has how many sides?"
    ])
    return prompt, "", sides


def attribute_matching():
    prompt = _pick_variant([
        "If we slice a circle exactly down the middle into two equal parts, what shape is made?\n1) square  2) rectangle  3) semicircle",
        "A circle is cut into two equal parts. What shape is each piece?\n1) square  2) rectangle  3) semicircle",
        "What shape results from splitting a circle into two equal halves?\n1) square  2) rectangle  3) semicircle",
        "Which shape matches a half-circle?\n1) square  2) rectangle  3) semicircle"
    ])
    return prompt, "", 3


def compare_height():
    unit = random.choice(["inches", "centimeters"])
    v1 = random.randint(10, 30)
    v2 = random.randint(35, 60)
    prompt = _pick_variant([
        f"Object A is {v1} {unit} long. Object B is {v2} {unit} long. How much longer is Object B than Object A?",
        f"Compare the lengths. How many {unit} longer is Object B than Object A?",
        f"Object B is longer than Object A by how many {unit}?",
        f"Find the difference in length between these objects in {unit}."
    ])
    return prompt, "", v2 - v1


def graph_reading():
    measurements = [random.randint(2, 6) for _ in range(5)]
    unique_vals = sorted(list(set(measurements)))
    plot_lines = []
    for val in unique_vals:
        count = measurements.count(val)
        plot_lines.append(f"{val} inches: {'X' * count}")
    board = "\n".join(plot_lines)
    target_val = max(set(measurements), key=measurements.count)
    prompt = _pick_variant([
        "Look at this line plot. Which measurement occurred the MOST times?",
        "Which value appears most often in the line plot?",
        "Find the most frequent measurement shown.",
        "Which reading is the mode in this plot?"
    ])
    return prompt, board, target_val


def weight_intuition():
    prompt = _pick_variant([
        "Which tool would you use to measure the exact length of a classroom desk?\n1) A weight scale  2) A ruler or measuring tape  3) A thermometer",
        "Choose the best tool to measure a desk length.\n1) A weight scale  2) A ruler or measuring tape  3) A thermometer",
        "What instrument measures the length of a classroom desk accurately?\n1) A weight scale  2) A ruler or measuring tape  3) A thermometer",
        "Which option is the correct measuring tool?\n1) A weight scale  2) A ruler or measuring tape  3) A thermometer"
    ])
    return prompt, "", 2


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
