import random

def count_items_1_6():
    n1 = random.randint(2, 5)
    n2 = random.randint(6, 9)
    mult = random.randint(2, 4)
    visual = f"Group A has {n1} items, Group B has {n2} items."
    return f"The ratio of items is {n1}:{n2}. If Group A scales up to {n1 * mult} items, how many items will Group B have?", visual, n2 * mult

def count_items_5_10():
    whole = random.choice([20, 40, 50, 100, 200])
    pct = random.choice([10, 25, 50, 75, 90])
    ans = int(whole * (pct / 100))
    return f"What is {pct}% of {whole}?", "", ans

def missing_number_sequence():
    ans = random.randint(3, 15)
    coef = random.randint(2, 6)
    prod = ans * coef
    return f"Solve for the missing value: {coef}x = {prod}", "", ans

def basic_addition():
    ans = random.randint(5, 20)
    subtrahend = random.randint(3, 15)
    total = ans + subtrahend
    return f"Solve for the missing value: x + {subtrahend} = {total}", "", ans

def basic_subtraction():
    ans = random.randint(5, 20)
    subtrahend = random.randint(3, 15)
    return f"Solve for the missing value: x - {subtrahend} = {ans}", "", ans + subtrahend

def compare_more():
    v1 = random.randint(-15, -1)
    v2 = random.randint(-15, -1)
    while v1 == v2:
        v2 = random.randint(-15, -1)
    return f"Which negative value statement is true?\n1) {v1} > {v2}  2) {v1} < {v2}", "", 1 if v1 > v2 else 2

def identify_sides():
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    quad = random.randint(1, 4)
    mx = x if quad in [1, 4] else -x
    my = y if quad in [1, 2] else -y
    return f"In which quadrant does the coordinate point ({mx}, {my}) lie?\n1) Quadrant I  2) Quadrant II  3) Quadrant III  4) Quadrant IV", "", quad

def count_specific_shape():
    fixed = random.randint(-9, 9)
    v1 = random.randint(1, 8)
    v2 = random.randint(1, 8)
    while v1 == v2:
        v2 = random.randint(1, 8)
    use_vertical = random.choice([True, False])
    if use_vertical:
        visual = f"Point A: ({fixed}, {v1})\nPoint B: ({fixed}, {-v2})"
    else:
        visual = f"Point A: ({v1}, {fixed})\nPoint B: ({-v2}, {fixed})"
    return "Find the total distance between Point A and Point B across the axis line:", visual, v1 + v2

def match_3d_shape():
    v1 = random.randint(3, 8)
    v2 = random.randint(3, 8)
    return "Find the missing structural variable calculation: Area of a triangle = (base x height) / 2", f"Base = {v1} cm, Height = {v2} cm", (v1 * v2) // 2

def ab_pattern():
    v1 = random.randint(4, 9)
    v2 = random.randint(3, 6)
    v3 = random.randint(2, 5)
    total = (v1 * v2 * 2) + (v1 * v3 * 2) + (v2 * v3 * 2)
    visual = f"Length = {v1} cm, Width = {v2} cm, Height = {v3} cm"
    return "Find the total surface area of a rectangular prism with these dimensions:", visual, total

def size_sorting():
    nums = [random.randint(1, 10) for _ in range(5)]
    ans = sum(nums) // 5
    visual = "Data points: " + ", ".join(map(str, nums))
    return "Find the mean (average) value calculation for this dataset:", visual, ans

def attribute_matching():
    nums = sorted([random.randint(1, 20) for _ in range(5)])
    ans = nums[2]
    visual = "Data points: " + ", ".join(map(str, nums))
    return "Find the median value calculation for this sorted dataset:", visual, ans

def compare_height():
    nums = [random.randint(5, 25) for _ in range(5)]
    ans = max(nums) - min(nums)
    visual = "Data points: " + ", ".join(map(str, nums))
    return "Find the statistical range variation metric (Maximum - Minimum) for this dataset:", visual, ans

def graph_reading():
    v = random.randint(2, 10)
    return f"Evaluate the absolute numerical value magnitude: |-{v}| = ____", "", v

def weight_intuition():
    prompt = "Which choice is a statistical question that anticipates variability in the answers?\n1) How old am I?\n2) How many pets do the students in my school have?\n3) How many sides does a triangle have?"
    return prompt, "", 2

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
