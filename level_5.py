import random


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    v1 = random.randint(-15, -2)
    v2 = random.randint(3, 15)
    prompt = _pick_variant([
        "Solve the integer addition problem:",
        "Add the integers together:",
        "Find the sum of the numbers:",
        "What is the result of this addition?"
    ])
    return prompt, f"{v1} + {v2} = ____", v1 + v2


def count_items_5_10():
    v1 = random.randint(-10, -2)
    v2 = random.randint(-8, -2)
    prompt = _pick_variant([
        "Solve the integer multiplication problem:",
        "Multiply the integers:",
        "Find the product:",
        "What is the result of this multiplication?"
    ])
    return prompt, f"({v1}) x ({v2}) = ____", v1 * v2


def missing_number_sequence():
    item_cost = random.randint(15, 45)
    markup_pct = random.choice([10, 20, 50])
    ans = int(item_cost * (1 + markup_pct / 100))
    visual = f"Wholesale Price = ${item_cost}, Store Markup = {markup_pct}%"
    prompt = _pick_variant([
        "Calculate the final retail selling price of the item after markup:",
        "Find the selling price after the markup:",
        "What is the item’s price after the markup?",
        "Compute the final retail price."
    ])
    return prompt, visual, ans


def basic_addition():
    ans = random.randint(2, 8)
    coef = random.randint(2, 5)
    const = random.randint(3, 12)
    total = (coef * ans) + const
    prompt = _pick_variant([
        f"Solve the two-step linear equation for x: {coef}x + {const} = {total}",
        f"Find x in: {coef}x + {const} = {total}",
        f"Solve for x in this equation: {coef}x + {const} = {total}",
        f"What value of x makes the equation true? {coef}x + {const} = {total}"
    ])
    return prompt, "", ans


def basic_subtraction():
    ans = random.randint(3, 9)
    coef = random.randint(2, 5)
    const = random.randint(2, 10)
    total = (coef * ans) - const
    prompt = _pick_variant([
        f"Solve the two-step linear equation for x: {coef}x - {const} = {total}",
        f"Find x in: {coef}x - {const} = {total}",
        f"Solve for x in this equation: {coef}x - {const} = {total}",
        f"What value of x makes the equation true? {coef}x - {const} = {total}"
    ])
    return prompt, "", ans


def compare_more():
    v1 = random.randint(2, 6)
    ans = random.randint(2, 6)
    total = v1 * ans
    prompt = _pick_variant([
        f"Solve the inequality structure calculation: {v1}x > {total}\n1) x > {ans}  2) x < {ans}",
        f"Which inequality is true?\n1) x > {ans}  2) x < {ans}",
        f"Choose the correct solution statement.\n1) x > {ans}  2) x < {ans}",
        f"Interpret the inequality: {v1}x > {total}.\n1) x > {ans}  2) x < {ans}"
    ])
    return prompt, "", 1


def identify_sides():
    radius = random.choice([7, 14, 21])
    ans = int(2 * (22 / 7) * radius)
    prompt = _pick_variant([
        "Find the total circumference distance of a circular frame boundary:",
        "What is the circumference of this circle?",
        "Compute the circumference of the circular object:",
        "Determine the distance around the circle."
    ])
    return prompt, f"Radius = {radius} cm (Use pi = 22/7)", ans


def count_specific_shape():
    radius = random.choice([7, 14, 21])
    ans = int((22 / 7) * radius * radius)
    prompt = _pick_variant([
        "Find the complete surface area coverage of a circular element layout:",
        "What is the area of the circle?",
        "Compute the area of the circle using the given radius:",
        "Find the total area of this circular region."
    ])
    return prompt, f"Radius = {radius} cm (Use pi = 22/7)", ans


def match_3d_shape():
    v1 = random.choice([30, 45, 60, 90])
    prompt = _pick_variant([
        f"Two angles are complementary. If one angle measures {v1} degrees, what is the measure of its complement?",
        f"A complementary angle pair includes {v1} degrees. What is the other angle?",
        f"Find the complement of an angle measuring {v1} degrees.",
        f"What angle adds to {v1} degrees to make a right angle?"
    ])
    return prompt, "", 90 - v1


def ab_pattern():
    v1 = random.choice([30, 60, 90, 120])
    prompt = _pick_variant([
        f"Two angles form a linear pair and are supplementary. If one angle measures {v1} degrees, what is the measure of its supplement?",
        f"A supplementary angle pair includes {v1} degrees. What is the other angle?",
        f"Find the supplement of an angle measuring {v1} degrees.",
        f"What angle adds to {v1} degrees to make a straight line?"
    ])
    return prompt, "", 180 - v1


def size_sorting():
    total_marbles = 20
    red_marbles = random.randint(3, 8)
    prompt = _pick_variant([
        f"A bag contains {total_marbles} total items. If {red_marbles} of them are red, what is the probability of pulling a red item at random?\n1) {red_marbles}/{total_marbles}  2) 1/2  3) 0",
        f"What is the probability of drawing a red marble?\n1) {red_marbles}/{total_marbles}  2) 1/2  3) 0",
        f"Choose the correct probability.\n1) {red_marbles}/{total_marbles}  2) 1/2  3) 0",
        f"A bag has {total_marbles} marbles with {red_marbles} red. Probability of red?\n1) {red_marbles}/{total_marbles}  2) 1/2  3) 0"
    ])
    return prompt, "", 1


def attribute_matching():
    prompt = _pick_variant([
        "Which tracking option defines a sample population configuration that accurately represents an entire school?\n1) Every 5th student entering the school building\n2) Only members of the basketball team\n3) The first 20 students in the cafeteria",
        "Which sampling method best represents the whole school?\n1) Every 5th student entering the school building\n2) Only members of the basketball team\n3) The first 20 students in the cafeteria",
        "Choose the unbiased sample.\n1) Every 5th student entering the school building\n2) Only members of the basketball team\n3) The first 20 students in the cafeteria",
        "Which option is a representative sample of the student body?\n1) Every 5th student entering the school building\n2) Only members of the basketball team\n3) The first 20 students in the cafeteria"
    ])
    return prompt, "", 1


def compare_height():
    v1 = random.randint(5, 15)
    v2 = random.randint(2, 4)
    prompt = _pick_variant([
        f"A map scale uses 1 inch to represent {v1} real miles. If a road measures {v2} inches on the map grid, how long is it in reality?",
        f"Use the scale to find the real distance for {v2} inches on the map.",
        f"How many miles is a road that measures {v2} inches on a {v1}-mile-per-inch map?",
        f"Determine the real length of a road shown as {v2} inches on the map."
    ])
    return prompt, "", v1 * v2


def graph_reading():
    v1 = random.randint(2, 6)
    prompt = _pick_variant([
        f"Identify the constant of proportionality unit rate from the direct equation framework: y = {v1}x",
        f"What is the constant of proportionality in y = {v1}x?",
        f"Find the unit rate for the equation y = {v1}x.",
        f"Determine the constant of proportionality in this equation."
    ])
    return prompt, "", v1


def weight_intuition():
    prompt = _pick_variant([
        "If a coin is tossed 1000 times, which outcome projection aligns best with probability data standards?\n1) Close to 500 heads\n2) Exactly 1000 heads\n3) Exactly 0 heads",
        "What is the most likely result after 1000 coin tosses?\n1) Close to 500 heads\n2) Exactly 1000 heads\n3) Exactly 0 heads",
        "Which outcome is best supported by probability?\n1) Close to 500 heads\n2) Exactly 1000 heads\n3) Exactly 0 heads",
        "Choose the most reasonable result for 1000 tosses.\n1) Close to 500 heads\n2) Exactly 1000 heads\n3) Exactly 0 heads"
    ])
    return prompt, "", 1


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}


def play_game(level, difficulty):
    question, visual, correct_answer = MATH_ROUTER[level][difficulty]()

    print(question)
    if visual:
        print(visual)

    choices = [correct_answer]
    if isinstance(correct_answer, int):
        possible_distractors = [v for v in range(max(0, correct_answer - 50), correct_answer + 51) if v != correct_answer]
        choices.extend(random.sample(possible_distractors, min(3, len(possible_distractors))))
    elif "/" in str(correct_answer) or "." in str(correct_answer):
        choices.extend(["0.5", "1.25", "3/10", "4/5", "0.75"])
        choices = list(set(choices))
        if correct_answer not in choices:
            choices.append(correct_answer)
        choices = choices[:4]
    else:
        choices.extend(["Option Variant X", "Option Variant Y", "Option Variant Z"])
        choices = list(set(choices))[:4]
        if correct_answer not in choices:
            choices.append(correct_answer)

    random.shuffle(choices)
    letters = ["A", "B", "C", "D"][:len(choices)]

    print("\nChoices:")
    for letter, choice in zip(letters, choices):
        print(f"Option {letter}: {choice}")

    while True:
        try:
            answer = input().strip().upper()
            if answer in letters:
                break
            print(f"Invalid response. Please type one of: {', '.join(letters)}")
        except EOFError:
            print("Input closed. Exiting question.")
            return None

    selected_answer = choices[letters.index(answer)]
    if str(selected_answer) == str(correct_answer):
        print("Correct!")
    else:
        print(f"You did not answer correctly. The answer was {correct_answer}.")

    return selected_answer
