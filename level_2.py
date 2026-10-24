import random

def count_items_1_6():
    start = random.randint(100, 900)
    step = random.choice([5, 10, 100])
    sequence = [start + (i * step) for i in range(5)]
    missing_idx = random.randint(1, 4)
    correct = sequence[missing_idx]
    seq_str = [str(x) if i != missing_idx else "___" for i, x in enumerate(sequence)]
    return f"Count skip-counting by {step}. What number is missing?", " ".join(seq_str), correct

def count_items_5_10():
    hundreds = random.randint(1, 9)
    tens = random.randint(0, 9)
    ones = random.randint(0, 9)
    total = (hundreds * 100) + (tens * 10) + ones
    board = f"Blocks: {hundreds} flats of 100, {tens} rods of 10, and {ones} unit cubes."
    return "What is the standard form number for these base-ten blocks?", board, total

def missing_number_sequence():
    n1 = random.randint(100, 999)
    n2 = random.randint(100, 999)
    while n1 == n2:
        n2 = random.randint(100, 999)
    return f"Which number statement is true?\n1) {n1} > {n2}  2) {n1} < {n2}", "", 1 if n1 > n2 else 2

def basic_addition():
    v1 = random.randint(10, 90)
    v2 = random.randint(10, 90)
    return "Solve the two-digit addition problem:", f"  {v1}\n+ {v2}\n----", v1 + v2

def basic_subtraction():
    v1 = random.randint(50, 99)
    v2 = random.randint(10, 49)
    return "Solve the two-digit subtraction problem:", f"  {v1}\n- {v2}\n----", v1 - v2

def compare_more():
    v1 = random.randint(10, 50)
    v2 = random.randint(10, 50)
    v3 = random.randint(10, 50)
    return "Add three numbers together:", f"{v1} + {v2} + {v3} = ____", v1 + v2 + v3

def identify_sides():
    hour = random.randint(1, 12)
    minute = random.choice([5, 15, 20, 40, 45, 55])
    time_str = f"{hour}:{minute:02d}"
    clock_desc = f"The short hand is near {hour}. The long hand points directly at the {minute // 5} marker."
    return "What time does this analog clock show?", clock_desc, time_str

def count_specific_shape():
    quarters = random.randint(0, 3)
    dimes = random.randint(0, 4)
    nickels = random.randint(0, 5)
    total = (quarters * 25) + (dimes * 10) + (nickels * 5)
    board = f"Wallet contains: {quarters} quarters, {dimes} dimes, and {nickels} nickels."
    return "How many total cents do you have?", board, total

def match_3d_shape():
    rows = random.randint(2, 5)
    cols = random.randint(2, 5)
    total = rows * cols
    board = "\n".join(["[■]" * cols for _ in range(rows)])
    return f"Look at this rectangular array. How many blocks are there in total?", board, total

def ab_pattern():
    shape = random.choice(["cube", "rectangular prism", "pyramid"])
    faces = {"cube": 6, "rectangular prism": 6, "pyramid": 5}[shape]
    return f"How many flat faces does a {shape} have?", "", faces

def size_sorting():
    shape = random.choice(["pentagon", "hexagon", "quadrilateral"])
    sides = {"pentagon": 5, "hexagon": 6, "quadrilateral": 4}[shape]
    return f"How many side paths does a {shape} shape have?", "", sides

def attribute_matching():
    prompt = "If we slice a circle exactly down the middle into two equal parts, what shape is made?\n1) square  2) rectangle  3) semicircle"
    return prompt, "", 3

def compare_height():
    unit = random.choice(["inches", "centimeters"])
    v1 = random.randint(10, 30)
    v2 = random.randint(35, 60)
    return f"Object A is {v1} {unit} long. Object B is {v2} {unit} long. How much longer is Object B than Object A?", "", v2 - v1

def graph_reading():
    measurements = [random.randint(2, 6) for _ in range(5)]
    unique_vals = sorted(list(set(measurements)))
    plot_lines = []
    for val in unique_vals:
        count = measurements.count(val)
        plot_lines.append(f"{val} inches: {'X' * count}")
    board = "\n".join(plot_lines)
    target_val = max(set(measurements), key=measurements.count)
    return "Look at this line plot. Which measurement occurred the MOST times?", board, target_val

def weight_intuition():
    prompt = "Which tool would you use to measure the exact length of a classroom desk?\n1) A weight scale  2) A ruler or measuring tape  3) A thermometer"
    return prompt, "", 2

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
