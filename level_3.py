import random


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    factor1 = random.randint(2, 9)
    factor2 = random.randint(2, 9)
    product = factor1 * factor2
    visual = "\n".join(["● " * factor2 for _ in range(factor1)])
    prompt = _pick_variant([
        f"Look at this array. What is {factor1} groups of {factor2}?",
        f"How many are in {factor1} groups of {factor2}?",
        f"Count the array. What is {factor1} times {factor2}?",
        f"Find the total number in this arrangement: {factor1} groups of {factor2}."
    ])
    return prompt, visual, product


def count_items_5_10():
    total = random.randint(12, 40)
    groups = random.choice([2, 3, 4, 5])
    while total % groups != 0:
        total = random.randint(12, 40)
    each = total // groups
    visual = "Total objects: " + "★ " * total
    prompt = _pick_variant([
        f"If you divide these {total} objects equally into {groups} groups, how many are in each group?",
        f"Split {total} objects into {groups} equal groups. How many in each group?",
        f"Share {total} objects equally among {groups} groups. How many per group?",
        f"What is the equal group size for {total} items divided into {groups} groups?"
    ])
    return prompt, visual, each


def missing_number_sequence():
    f1 = random.randint(3, 8)
    f2 = random.randint(3, 8)
    prod = f1 * f2
    prompt = _pick_variant([
        f"Find the missing number: {f1} x ____ = {prod}",
        f"What number makes this true? {f1} x ____ = {prod}",
        f"Solve for the blank: {f1} × ____ = {prod}",
        f"Complete the multiplication fact: {f1} x ____ = {prod}"
    ])
    return prompt, "", f2


def basic_addition():
    v1 = random.randint(100, 800)
    v2 = random.randint(100, 199)
    prompt = _pick_variant([
        "Solve the three-digit addition problem:",
        "Add the three-digit numbers:",
        "Find the sum of these numbers:",
        "What is the total of these values?"
    ])
    return prompt, f"  {v1}\n+ {v2}\n----", v1 + v2


def basic_subtraction():
    v1 = random.randint(500, 999)
    v2 = random.randint(100, 499)
    prompt = _pick_variant([
        "Solve the three-digit subtraction problem:",
        "Subtract to find the difference:",
        "Find the result of this subtraction:",
        "What is the difference between these numbers?"
    ])
    return prompt, f"  {v1}\n- {v2}\n----", v1 - v2


def compare_more():
    factor = random.choice([10, 20, 30, 40, 50])
    multiplier = random.randint(2, 9)
    prompt = _pick_variant([
        "Multiply the single digit by a multiple of 10:",
        "Find the product of the single digit and the multiple of 10:",
        "Solve this multiplication problem:",
        "What is the result of this calculation?"
    ])
    return prompt, f"{multiplier} x {factor} = ____", multiplier * factor


def identify_sides():
    denom = random.choice([2, 3, 4, 6, 8])
    num = random.randint(1, denom - 1)
    visual = f"A shape is divided into {denom} equal parts, and {num} parts are shaded."
    prompt = _pick_variant([
        "What fraction of the shape is shaded?",
        "What fraction is represented by the shaded portion?",
        "Which fraction matches the shaded part?",
        "Write the fraction of the shape that is shaded."
    ])
    return prompt, visual, f"{num}/{denom}"


def count_specific_shape():
    val = random.randint(1, 5)
    visual = "-------\n" + "|     |\n" * val + "-------"
    prompt = _pick_variant([
        "Look at this number line split into equal segments. What fraction represents point A?",
        "What fraction matches point A on this number line?",
        "Determine the fraction for point A.",
        "Which fraction is shown by point A?"
    ])
    return prompt, visual, f"{val}/{val}"


def match_3d_shape():
    n1 = random.randint(1, 4)
    d1 = random.choice([3, 4, 6, 8])
    n2 = n1 * 2
    d2 = d1 * 2
    prompt = _pick_variant([
        f"Which fraction is equivalent to {n1}/{d1}?\n1) {n2}/{d2}  2) 1/5  3) 7/9",
        f"Choose the equivalent fraction for {n1}/{d1}.\n1) {n2}/{d2}  2) 1/5  3) 7/9",
        f"Which option equals {n1}/{d1}?\n1) {n2}/{d2}  2) 1/5  3) 7/9",
        f"Select the equivalent fraction.\n1) {n2}/{d2}  2) 1/5  3) 7/9"
    ])
    return prompt, "", 1


def ab_pattern():
    length = random.randint(3, 8)
    width = random.randint(3, 8)
    area = length * width
    visual = f"Length = {length} cm\nWidth = {width} cm"
    prompt = _pick_variant([
        "Find the total area of this rectangle in square centimeters:",
        "What is the area of this rectangle?",
        "Calculate the area of the rectangle.",
        "Find the surface area of the rectangle in square centimeters."
    ])
    return prompt, visual, area


def size_sorting():
    side1 = random.randint(3, 9)
    side2 = random.randint(3, 9)
    side3 = random.randint(3, 9)
    side4 = random.randint(3, 9)
    perimeter = side1 + side2 + side3 + side4
    visual = f"Sides are: {side1} cm, {side2} cm, {side3} cm, and {side4} cm"
    prompt = _pick_variant([
        "Find the perimeter of this polygon in centimeters:",
        "What is the perimeter of this shape?",
        "Add the side lengths. What is the total perimeter?",
        "Calculate the distance around the polygon."
    ])
    return prompt, visual, perimeter


def attribute_matching():
    prompt = _pick_variant([
        "Which subcategory do all squares, rectangles, and rhombuses belong to?\n1) Triangles  2) Quadrilaterals  3) Hexagons",
        "Which group includes squares, rectangles, and rhombuses?\n1) Triangles  2) Quadrilaterals  3) Hexagons",
        "All of these shapes are what type of polygon?\n1) Triangles  2) Quadrilaterals  3) Hexagons",
        "Choose the category for squares, rectangles, and rhombuses.\n1) Triangles  2) Quadrilaterals  3) Hexagons"
    ])
    return prompt, "", 2


def compare_height():
    v1 = random.randint(100, 500)
    v2 = random.randint(50, 200)
    prompt = _pick_variant([
        f"A bottle holds {v1} milliliters of water. A glass holds {v2} milliliters. How many milliliters do they hold together?",
        f"Add the total liquid capacity of the bottle and the glass.",
        f"What is the combined volume of the bottle and glass?",
        f"Find the total milliliters in both containers."
    ])
    return prompt, "", v1 + v2


def graph_reading():
    prompt = _pick_variant([
        "A movie starts at 4:15 PM and lasts for 45 minutes. What time does the movie end?\n1) 4:45 PM  2) 5:00 PM  3) 5:30 PM",
        "If a movie starts at 4:15 PM and lasts 45 minutes, when does it end?\n1) 4:45 PM  2) 5:00 PM  3) 5:30 PM",
        "What time is it after adding 45 minutes to 4:15 PM?\n1) 4:45 PM  2) 5:00 PM  3) 5:30 PM",
        "Which time matches the end of a 45-minute movie starting at 4:15 PM?\n1) 4:45 PM  2) 5:00 PM  3) 5:30 PM"
    ])
    return prompt, "", 2


def weight_intuition():
    items = ["Apple", "Banana", "Orange"]
    weights = [random.randint(2, 5) for _ in items]
    visual = "\n".join([f"{item}: {'█' * w}" for item, w in zip(items, weights)])
    target = items[weights.index(max(weights))]
    prompt = _pick_variant([
        "Look at this bar graph. Which fruit scale bar shows the highest value?",
        "Which fruit has the tallest bar on the graph?",
        "Which item shows the greatest value in this bar graph?",
        "Find the fruit with the highest bar."
    ])
    return prompt, visual, target


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
