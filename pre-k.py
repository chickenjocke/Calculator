import random

def count_items_1_6():
    num = random.randint(1, 6)
    return "How many items are there?", generate_shapes(num), num

def count_items_5_10():
    num = random.randint(5, 10)
    return "How many items are there?", generate_shapes(num), num

def missing_number_sequence():
    start = random.randint(1, 5)
    sequence = [start, start + 1, start + 2, start + 3]
    missing_idx = random.randint(1, 3)
    correct = sequence[missing_idx]
    seq_str = [str(x) if i != missing_idx else "___" for i, x in enumerate(sequence)]
    return "What number comes next in the sequence?", " ".join(seq_str), correct

def basic_addition():
    num1, num2 = random.randint(1, 4), random.randint(1, 3)
    visual = f"{generate_shapes(num1)}   and   {generate_shapes(num2)}"
    return f"You have {num1} items. If I give you {num2} more, how many do you have now?", visual, num1 + num2

def basic_subtraction():
    num1 = random.randint(3, 6)
    num2 = random.randint(1, num1 - 1)
    return f"There are {num1} items {generate_shapes(num1)}. If we take {num2} away, how many are left?", "", num1 - num2

def compare_more():
    num1, num2 = random.randint(1, 5), random.randint(1, 5)
    while num1 == num2:
        num2 = random.randint(1, 5)
    visual = f"Group A: {generate_shapes(num1)}\nGroup B: {generate_shapes(num2)}"
    return "Which group has MORE items? (Type the count of that group)", visual, max(num1, num2)

def identify_sides():
    shape = random.choice(["circle", "triangle", "square"])
    sides = {"circle": 0, "triangle": 3, "square": 4}[shape]
    visual = generate_shapes(1, fixed_shape=shape)
    return f"How many sides does this {shape} have?", visual, sides

def count_specific_shape():
    target = random.choice(["circle", "square", "triangle"])
    target_count = random.randint(1, 4)
    other_count = random.randint(1, 3)
    items = [generate_shapes(1, fixed_shape=target) for _ in range(target_count)]
    other_shape = random.choice([s for s in ["circle", "square", "triangle"] if s != target])
    items += [generate_shapes(1, fixed_shape=other_shape) for _ in range(other_count)]
    random.shuffle(items)
    return f"How many {target}s do you see?", " ".join(items), target_count

def match_3d_shape():
    shape_3d = random.choice(["sphere", "cube", "cone"])
    answers = {"sphere": "ball", "cube": "box", "cone": "party hat"}
    prompt = f"Which everyday object looks like a {shape_3d}?\n1) ball  2) box  3) party hat"
    return prompt, "", list(answers.keys()).index(shape_3d) + 1

def ab_pattern():
    sym1, sym2 = "🔴", "🟦"
    missing = random.choice([sym1, sym2])
    pattern = [sym1, sym2, sym1, sym2, missing]
    display = " ".join(pattern[:-1]) + " ___"
    ans = 1 if missing == sym1 else 2
    return f"What comes next in the pattern?\n1) {sym1}  2) {sym2}", display, ans

def size_sorting():
    ans = random.choice(["big", "small"])
    return f"If we sort toys by size, where do the {ans} ones go?\n1) Over here  2) Over there", "", 1 if ans == "big" else 2

def attribute_matching():
    color = random.choice(["red", "blue", "yellow", "green"])
    visual = f"🍎 (Red)  🚙 (Blue)  🍌 (Yellow)  🥦 (Green)"
    ans = {"red": 1, "blue": 2, "yellow": 3, "green": 4}[color]
    return f"Which item matches the color {color}?", visual, ans

def compare_height():
    h1, h2 = random.randint(1, 4), random.randint(1, 4)
    while h1 == h2: h2 = random.randint(1, 4)
    visual = f"Tower A height: {h1} blocks\nTower B height: {h2} blocks"
    return "Which tower is taller? (Type the height of that tower)", visual, max(h1, h2)

def graph_reading():
    apples, bananas = random.randint(1, 5), random.randint(1, 5)
    while apples == bananas: bananas = random.randint(1, 5)
    visual = f"Apples Graph: {'🍏'*apples}\nBananas Graph: {'🍌'*bananas}"
    return "Which fruit has the MOST votes?\n1) Apples  2) Bananas", visual, 1 if apples > bananas else 2

def weight_intuition():
    return "Which object is heavier?\n1) feather  2) brick", "", 2

def generate_shapes(count, fixed_shape=None):
    picture_items = []
    for _ in range(count):
        shape = fixed_shape if fixed_shape else random.choice(["circle", "square", "triangle"])
        color = random.choice(["red", "blue", "yellow", "green"])
        if shape == "circle":
            picture_items.append({"red": "🔴", "blue": "🔵", "yellow": "🟡", "green": "🟢"}[color])
        elif shape == "square":
            picture_items.append({"red": "🟥", "blue": "🟦", "yellow": "🟨", "green": "🟩"}[color])
        else:
            picture_items.append("▲({})".format(color.title()))
    return " ".join(picture_items)

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
