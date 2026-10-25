import random


def count_items_1_6():
    num = random.randint(10, 20)
    templates = [
        "Count all the stars. How many are there in total?",
        "Look at the stars and count them. What is the total number?",
        "How many stars are there altogether?",
        "Count the stars. What number do you get when you count all of them?"
    ]
    return random.choice(templates), generate_shapes(num), num


def count_items_5_10():
    num = random.randint(1, 16)
    sequence = [num, num + 1, num + 2, num + 3, num + 4]
    missing_idx = random.randint(2, 4)
    correct = sequence[missing_idx]
    seq_str = [str(x) if i != missing_idx else "___" for i, x in enumerate(sequence)]
    templates = [
        "What missing number finishes this counting sequence?",
        "Fill in the blank to complete the number pattern.",
        "Which number belongs in the empty spot?",
        "What number is missing from this sequence?"
    ]
    return random.choice(templates), " ".join(seq_str), correct


def missing_number_sequence():
    num1, num2 = random.randint(5, 12), random.randint(5, 12)
    while num1 == num2:
        num2 = random.randint(5, 12)
    visual = f"Group A: {generate_shapes(num1)}\nGroup B: {generate_shapes(num2)}"
    templates = [
        "Which group has LESS items? (Type the count of that group)",
        "Which set has fewer items? Write the number in that set.",
        "Count each group. Which group has the smaller total?",
        "Which group has the least number of items?"
    ]
    return random.choice(templates), visual, min(num1, num2)


def basic_addition():
    num1, num2 = random.randint(1, 6), random.randint(1, 4)
    visual = f"{generate_shapes(num1)}   and   {generate_shapes(num2)}"
    templates = [
        f"Solve the addition equation: {num1} + {num2} = ____",
        f"Add the groups together. {num1} + {num2} = ?",
        f"What is the total? {num1} + {num2} = ____",
        f"Combine the groups and find the sum: {num1} + {num2} = ____"
    ]
    return random.choice(templates), visual, num1 + num2


def basic_subtraction():
    num1 = random.randint(5, 10)
    num2 = random.randint(1, num1 - 1)
    visual = generate_shapes(num1)
    templates = [
        f"Solve the subtraction equation: {num1} - {num2} = ____",
        f"Take away {num2}. What is left? {num1} - {num2} = ?",
        f"Find the difference: {num1} - {num2} = ____",
        f"How many are left after subtracting {num2}? {num1} - {num2} = ____"
    ]
    return random.choice(templates), visual, num1 - num2


def compare_more():
    given_number = random.randint(1, 9)
    visual = f"{given_number} + ____ = 10"
    templates = [
        f"How many more do you need to add to {given_number} to make 10?",
        f"What number makes the equation true: {given_number} + __ = 10?",
        f"How many more are needed to reach 10 from {given_number}?",
        f"What is the missing addend to make 10 with {given_number}?"
    ]
    return random.choice(templates), visual, 10 - given_number


def identify_sides():
    solids = ["cube", "sphere", "cylinder", "cone"]
    flats = ["square", "circle", "triangle", "rectangle"]
    is_asking_3d = random.choice([True, False])
    if is_asking_3d:
        target = random.choice(solids)
        distractor = random.choice(flats)
        templates = [
            f"Which shape is a 3D (solid) shape?\n1) {target}  2) {distractor}",
            f"Pick the solid shape.\n1) {target}  2) {distractor}",
            f"Which one is 3D?\n1) {target}  2) {distractor}",
            f"Which shape is not flat?\n1) {target}  2) {distractor}"
        ]
        return random.choice(templates), "", 1
    else:
        target = random.choice(flats)
        distractor = random.choice(solids)
        templates = [
            f"Which shape is a 2D (flat) shape?\n1) {distractor}  2) {target}",
            f"Pick the flat shape.\n1) {distractor}  2) {target}",
            f"Which one is 2D?\n1) {distractor}  2) {target}",
            f"Which shape is flat instead of solid?\n1) {distractor}  2) {target}"
        ]
        return random.choice(templates), "", 2


def count_specific_shape():
    variants = [
        ("     🔵 (Blue Circle)\n    ---------\n     🟩 (Green Square)", "Where is the Blue Circle relative to the Green Square?\n1) ABOVE  2) BELOW"),
        ("     🟩 (Green Square)\n    ---------\n     🔵 (Blue Circle)", "Where is the Blue Circle compared to the Green Square?\n1) ABOVE  2) BELOW"),
        ("     🔵 (Blue Circle)\n     🟩 (Green Square)", "Which direction is the Blue Circle from the Green Square?\n1) ABOVE  2) BELOW"),
        ("     🟩 (Green Square)\n     🔵 (Blue Circle)", "Is the Blue Circle above or below the Green Square?\n1) ABOVE  2) BELOW")
    ]
    visual, prompt = random.choice(variants)
    return prompt, visual, 1


def match_3d_shape():
    shape = random.choice(["triangle", "square", "rectangle", "hexagon"])
    sides = {"triangle": 3, "square": 4, "rectangle": 4, "hexagon": 6}[shape]
    templates = [
        f"How many corners (vertices) does a {shape} have?",
        f"How many vertices does a {shape} have?",
        f"A {shape} has how many corners?",
        f"Count the corners of a {shape}. How many are there?"
    ]
    return random.choice(templates), "", sides


def ab_pattern():
    teen_number = random.randint(11, 19)
    visual = f"{teen_number} = 10 + ____"
    templates = [
        "Look at the base-ten breakdown. How many leftover ones are there?",
        "How many ones are left after making a ten?",
        "What number is left over after the ten?",
        "How many extra ones are there after the ten?"
    ]
    return random.choice(templates), visual, teen_number - 10


def size_sorting():
    teen_number = random.randint(11, 19)
    ones_remainder = teen_number - 10
    visual = "📦 [Ten-Pack Container]  and  " + " ".join(["🍬" for _ in range(ones_remainder)])
    templates = [
        "How many items are there in total?",
        "Count the full set. What is the total number?",
        "How many objects are there altogether?",
        "What is the total count of all the items shown?"
    ]
    return random.choice(templates), visual, teen_number


def attribute_matching():
    ones_to_add = random.randint(1, 9)
    visual = f"10 + {ones_to_add} = ____"
    templates = [
        "What number is made of 10 and some more ones?",
        "How many in all when you add 10 and the leftover ones?",
        "What total do you get from 10 plus the extras?",
        "If you combine 10 with the ones shown, what number is it?"
    ]
    return random.choice(templates), visual, 10 + ones_to_add


def compare_height():
    pairs = [("elephant", "mouse"), ("anvil", "feather"), ("truck", "bicycle")]
    heavy, light = random.choice(pairs)
    templates = [
        f"Which object is heavier?\n1) {heavy}  2) {light}",
        f"Choose the heavier item.\n1) {heavy}  2) {light}",
        f"Which one weighs more?\n1) {heavy}  2) {light}",
        f"Pick the object with greater mass.\n1) {heavy}  2) {light}"
    ]
    return random.choice(templates), "", 1


def graph_reading():
    pairs = [("bathtub", "teacup"), ("swimming pool", "bucket"), ("gallon jug", "juice box")]
    big, small = random.choice(pairs)
    templates = [
        f"Which object can hold MORE liquid?\n1) {big}  2) {small}",
        f"Choose the container that holds more.\n1) {big}  2) {small}",
        f"Which item has greater capacity?\n1) {big}  2) {small}",
        f"Which object can hold the most liquid?\n1) {big}  2) {small}"
    ]
    return random.choice(templates), "", 1


def weight_intuition():
    categories = {"Fruits": ["🍎 (Apple)", "🍌 (Banana)"], "Vehicles": ["🚗 (Car)", "✈️ (Airplane)"]}
    chosen_cat = random.choice(list(categories.keys()))
    other_cat = "Vehicles" if chosen_cat == "Fruits" else "Fruits"
    item = random.choice(categories[chosen_cat])
    templates = [
        f"If we sort into groups, which group does {item} belong to?\n1) {chosen_cat}  2) {other_cat}",
        f"Sort this item into the correct category.\n1) {chosen_cat}  2) {other_cat}",
        f"Which group matches {item}?\n1) {chosen_cat}  2) {other_cat}",
        f"Where should {item} go?\n1) {chosen_cat}  2) {other_cat}"
    ]
    return random.choice(templates), "", 1


def generate_shapes(count, fixed_shape=None):
    shape = fixed_shape or "⭐"
    picture_items = []
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
