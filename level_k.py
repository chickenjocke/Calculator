import random


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    item = _pick_variant(["⭐", "☀️", "●", "■", "🍎"])
    count = random.randint(10, 20)
    prompt = _pick_variant([
        "Count all the objects. How many are there in total?",
        "How many items do you see altogether?",
        "Look closely and count everything. What is the total number?",
        "Count each shape. How many are there altogether?"
    ])
    visual = generate_shapes(count, fixed_shape=item)
    return prompt, visual, count


def count_items_5_10():
    start = random.randint(1, 12)
    step = random.choice([1, 2])
    sequence = [start + i * step for i in range(5)]
    missing_idx = random.randint(1, 3)
    correct = sequence[missing_idx]
    seq_str = [str(x) if i != missing_idx else "___" for i, x in enumerate(sequence)]
    prompt = _pick_variant([
        "What number is missing from this counting pattern?",
        "Fill in the missing number in the sequence.",
        "Which number completes this count?",
        "What number should come next in the pattern?"
    ])
    return prompt, " ".join(seq_str), correct


def missing_number_sequence():
    num1, num2 = random.randint(5, 12), random.randint(5, 12)
    while num1 == num2:
        num2 = random.randint(5, 12)
    smaller = min(num1, num2)
    prompt = _pick_variant([
        "Which group has LESS items? (Type the count of that group)",
        "Which group contains FEWER objects? Type the number in that group.",
        "Look at the groups. Which one has fewer items? Enter the count.",
        "Count each group. Which group has less? Write that number."
    ])
    visual = f"Group A: {generate_shapes(num1)}\nGroup B: {generate_shapes(num2)}"
    return prompt, visual, smaller


def basic_addition():
    num1, num2 = random.randint(1, 8), random.randint(1, 6)
    item = _pick_variant(["⭐", "☀️", "🍎", "●", "■"])
    visual = f"{generate_shapes(num1, fixed_shape=item)}   and   {generate_shapes(num2, fixed_shape=item)}"
    prompt = _pick_variant([
        f"Solve the addition equation: {num1} + {num2} = ____",
        f"How much is {num1} plus {num2}?",
        f"Add the numbers: {num1} + {num2} = ?",
        f"What is the sum of {num1} and {num2}?"
    ])
    return prompt, visual, num1 + num2


def basic_subtraction():
    num1 = random.randint(5, 12)
    num2 = random.randint(1, num1 - 1)
    item = _pick_variant(["⭐", "☀️", "🍎", "●", "■"])
    visual = generate_shapes(num1, fixed_shape=item)
    prompt = _pick_variant([
        f"Solve the subtraction equation: {num1} - {num2} = ____",
        f"Take away {num2} from {num1}. What is left?",
        f"What is {num1} minus {num2}?",
        f"Subtract: {num1} - {num2} = ?"
    ])
    return prompt, visual, num1 - num2


def compare_more():
    given_number = random.randint(1, 9)
    missing = 10 - given_number
    prompt = _pick_variant([
        f"How many more do you need to add to {given_number} to make 10?",
        f"What number goes in the blank to make 10? {given_number} + ____ = 10",
        f"How many more are needed to reach 10 from {given_number}?",
        f"Complete the equation: {given_number} + ____ = 10"
    ])
    visual = f"{given_number} + ____ = 10"
    return prompt, visual, missing


def identify_sides():
    solids = ["cube", "sphere", "cylinder", "cone"]
    flats = ["square", "circle", "triangle", "rectangle"]
    is_asking_3d = random.choice([True, False])
    if is_asking_3d:
        target = random.choice(solids)
        distractor = random.choice(flats)
        prompt = _pick_variant([
            f"Which shape is a 3D (solid) shape?\n1) {target}  2) {distractor}",
            f"Pick the solid shape.\n1) {target}  2) {distractor}",
            f"Which object is 3D?\n1) {target}  2) {distractor}"
        ])
        return prompt, "", 1
    target = random.choice(flats)
    distractor = random.choice(solids)
    prompt = _pick_variant([
        f"Which shape is a 2D (flat) shape?\n1) {distractor}  2) {target}",
        f"Pick the flat shape.\n1) {distractor}  2) {target}",
        f"Which object is 2D?\n1) {distractor}  2) {target}"
    ])
    return prompt, "", 2


def count_specific_shape():
    visual = "     🔵 (Blue Circle)\n    ---------\n     🟩 (Green Square)"
    prompt = _pick_variant([
        "Where is the Blue Circle relative to the Green Square?\n1) ABOVE  2) BELOW",
        "Look at the picture. Is the Blue Circle above or below the Green Square?\n1) ABOVE  2) BELOW",
        "Which position matches the Blue Circle?\n1) ABOVE  2) BELOW"
    ])
    return prompt, visual, 1


def match_3d_shape():
    shape = random.choice(["triangle", "square", "rectangle", "hexagon", "pentagon"])
    sides = {"triangle": 3, "square": 4, "rectangle": 4, "hexagon": 6, "pentagon": 5}[shape]
    prompt = _pick_variant([
        f"How many corners (vertices) does a {shape} have?",
        f"A {shape} has how many corners?",
        f"Count the corners of a {shape}. What is the total?",
        f"How many vertices does a {shape} have?"
    ])
    return prompt, "", sides


def ab_pattern():
    teen_number = random.randint(11, 19)
    left = teen_number - 10
    prompt = _pick_variant([
        "Look at the base-ten breakdown. How many leftover ones are there?",
        "How many ones are left over after making 10?",
        "What is the number of extra ones in this teen number?",
        "In this ten-and-some-more picture, how many ones are left?"
    ])
    visual = f"{teen_number} = 10 + ____"
    return prompt, visual, left


def size_sorting():
    teen_number = random.randint(11, 19)
    ones_remainder = teen_number - 10
    container = _pick_variant(["📦 [Ten-Pack Container]", "🧺 [Ten-Item Basket]", "🗃️ [Ten-Box]"])
    item = _pick_variant(["🍬", "🎯", "⭐", "🔹"])
    visual = container + "  and  " + " ".join([item for _ in range(ones_remainder)])
    prompt = _pick_variant([
        "How many items are there in total?",
        "Count everything together. What is the total number?",
        "How many are there altogether?",
        "Add the ten-pack and the extra ones. What number is it?"
    ])
    return prompt, visual, teen_number


def attribute_matching():
    ones_to_add = random.randint(1, 9)
    prompt = _pick_variant([
        f"What number is made of 10 and {ones_to_add} more ones?",
        f"What total do you get from 10 + {ones_to_add}?",
        f"Add 10 and {ones_to_add}. What is the number?",
        f"Combine 10 and {ones_to_add}. What number is made?"
    ])
    visual = f"10 + {ones_to_add} = ____"
    return prompt, visual, 10 + ones_to_add


def compare_height():
    pairs = [
        ("elephant", "mouse"),
        ("anvil", "feather"),
        ("truck", "bicycle"),
        ("bookcase", "lamp"),
        ("giraffe", "cat")
    ]
    heavy, light = random.choice(pairs)
    choices = [heavy, light]
    random.shuffle(choices)
    correct = 1 if choices[0] == heavy else 2
    prompt = _pick_variant([
        f"Which object is heavier?\n1) {choices[0]}  2) {choices[1]}",
        f"Pick the heavier object.\n1) {choices[0]}  2) {choices[1]}",
        f"Which item is heavier?\n1) {choices[0]}  2) {choices[1]}"
    ])
    return prompt, "", correct


def graph_reading():
    pairs = [
        ("bathtub", "teacup"),
        ("swimming pool", "bucket"),
        ("gallon jug", "juice box"),
        ("large bottle", "small cup"),
        ("watering can", "mug")
    ]
    big, small = random.choice(pairs)
    choices = [big, small]
    random.shuffle(choices)
    correct = 1 if choices[0] == big else 2
    prompt = _pick_variant([
        f"Which object can hold MORE liquid?\n1) {choices[0]}  2) {choices[1]}",
        f"Choose the container that holds more.\n1) {choices[0]}  2) {choices[1]}",
        f"Which one can hold a greater amount?\n1) {choices[0]}  2) {choices[1]}"
    ])
    return prompt, "", correct


def weight_intuition():
    categories = {
        "Fruits": ["🍎 (Apple)", "🍌 (Banana)", "🍇 (Grapes)", "🍊 (Orange)"],
        "Vehicles": ["🚗 (Car)", "✈️ (Airplane)", "🛴 (Scooter)", "🚲 (Bike)"]
    }
    chosen_cat = random.choice(list(categories.keys()))
    other_cat = "Vehicles" if chosen_cat == "Fruits" else "Fruits"
    item = random.choice(categories[chosen_cat])
    options = [chosen_cat, other_cat]
    random.shuffle(options)
    correct = 1 if options[0] == chosen_cat else 2
    prompt = _pick_variant([
        f"If we sort into groups, which group does {item} belong to?\n1) {options[0]}  2) {options[1]}",
        f"Sort this item into the correct group.\n1) {options[0]}  2) {options[1]}",
        f"Which category matches {item}?\n1) {options[0]}  2) {options[1]}"
    ])
    return prompt, "", correct


def generate_shapes(count, fixed_shape=None):
    picture_items = []
    shape = fixed_shape or "⭐"
    for _ in range(count):
        picture_items.append(shape)
    return " ".join(picture_items)


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
