import random

def count_items_1_6():
    num = random.randint(10, 20)
    return "Count all the stars. How many are there in total?", generate_shapes(num), num

def count_items_5_10():
    num = random.randint(1, 16)
    sequence = [num, num + 1, num + 2, num + 3, num + 4]
    missing_idx = random.randint(2, 4)
    correct = sequence[missing_idx]
    seq_str = [str(x) if i != missing_idx else "___" for i, x in enumerate(sequence)]
    return "What missing number finishes this counting sequence?", " ".join(seq_str), correct

def missing_number_sequence():
    num1, num2 = random.randint(5, 12), random.randint(5, 12)
    while num1 == num2:
        num2 = random.randint(5, 12)
    visual = f"Group A: {generate_shapes(num1)}\nGroup B: {generate_shapes(num2)}"
    return "Which group has LESS items? (Type the count of that group)", visual, min(num1, num2)

def basic_addition():
    num1, num2 = random.randint(1, 6), random.randint(1, 4)
    visual = f"{generate_shapes(num1)}   and   {generate_shapes(num2)}"
    return f"Solve the addition equation: {num1} + {num2} = ____", visual, num1 + num2

def basic_subtraction():
    num1 = random.randint(5, 10)
    num2 = random.randint(1, num1 - 1)
    visual = generate_shapes(num1)
    return f"Solve the subtraction equation: {num1} - {num2} = ____", visual, num1 - num2

def compare_more():
    given_number = random.randint(1, 9)
    visual = f"{given_number} + ____ = 10"
    return f"How many more do you need to add to {given_number} to make 10?", visual, 10 - given_number

def identify_sides():
    solids = ["cube", "sphere", "cylinder", "cone"]
    flats = ["square", "circle", "triangle", "rectangle"]
    is_asking_3d = random.choice([True, False])
    if is_asking_3d:
        target = random.choice(solids)
        prompt = f"Which shape is a 3D (solid) shape?\n1) {target}  2) {random.choice(flats)}"
        return prompt, "", 1
    else:
        target = random.choice(flats)
        prompt = f"Which shape is a 2D (flat) shape?\n1) {random.choice(solids)}  2) {target}"
        return prompt, "", 2

def count_specific_shape():
    visual = "     🔵 (Blue Circle)\n    ---------\n     🟩 (Green Square)"
    return "Where is the Blue Circle relative to the Green Square?\n1) ABOVE  2) BELOW", visual, 1

def match_3d_shape():
    shape = random.choice(["triangle", "square", "rectangle", "hexagon"])
    sides = {"triangle": 3, "square": 4, "rectangle": 4, "hexagon": 6}[shape]
    return f"How many corners (vertices) does a {shape} have?", "", sides

def ab_pattern():
    teen_number = random.randint(11, 19)
    visual = f"{teen_number} = 10 + ____"
    return "Look at the base-ten breakdown. How many leftover ones are there?", visual, teen_number - 10

def size_sorting():
    teen_number = random.randint(11, 19)
    ones_remainder = teen_number - 10
    visual = "📦 [Ten-Pack Container]  and  " + " ".join(["🍬" for _ in range(ones_remainder)])
    return "How many items are there in total?", visual, teen_number

def attribute_matching():
    ones_to_add = random.randint(1, 9)
    visual = f"10 + {ones_to_add} = ____"
    return "What number is made of 10 and some more ones?", visual, 10 + ones_to_add

def compare_height():
    pairs = [("elephant", "mouse"), ("anvil", "feather"), ("truck", "bicycle")]
    heavy, light = random.choice(pairs)
    return f"Which object is heavier?\n1) {heavy}  2) {light}", "", 1

def graph_reading():
    pairs = [("bathtub", "teacup"), ("swimming pool", "bucket"), ("gallon jug", "juice box")]
    big, small = random.choice(pairs)
    return f"Which object can hold MORE liquid?\n1) {big}  2) {small}", "", 1

def weight_intuition():
    categories = {"Fruits": ["🍎 (Apple)", "🍌 (Banana)"], "Vehicles": ["🚗 (Car)", "✈️ (Airplane)"]}
    chosen_cat = random.choice(list(categories.keys()))
    other_cat = "Vehicles" if chosen_cat == "Fruits" else "Fruits"
    item = random.choice(categories[chosen_cat])
    return f"If we sort into groups, which group does {item} belong to?\n1) {chosen_cat}  2) {other_cat}", "", 1

def generate_shapes(count, fixed_shape=None):
    picture_items = []
    for _ in range(count):
        picture_items.append("⭐")
    return " ".join(picture_items)

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
