import random

def count_items_1_6():
    factor1 = random.randint(2, 9)
    factor2 = random.randint(2, 9)
    product = factor1 * factor2
    visual = "\n".join(["● " * factor2 for _ in range(factor1)])
    return f"Look at this array. What is {factor1} groups of {factor2}?", visual, product

def count_items_5_10():
    total = random.randint(12, 40)
    groups = random.choice([2, 3, 4, 5])
    while total % groups != 0:
        total = random.randint(12, 40)
    each = total // groups
    visual = "Total objects: " + "★ " * total
    return f"If you divide these {total} objects equally into {groups} groups, how many are in each group?", visual, each

def missing_number_sequence():
    f1 = random.randint(3, 8)
    f2 = random.randint(3, 8)
    prod = f1 * f2
    return f"Find the missing number: {f1} x ____ = {prod}", "", f2

def basic_addition():
    v1 = random.randint(100, 800)
    v2 = random.randint(100, 199)
    return "Solve the three-digit addition problem:", f"  {v1}\n+ {v2}\n----", v1 + v2

def basic_subtraction():
    v1 = random.randint(500, 999)
    v2 = random.randint(100, 499)
    return "Solve the three-digit subtraction problem:", f"  {v1}\n- {v2}\n----", v1 - v2

def compare_more():
    factor = random.choice([10, 20, 30, 40, 50])
    multiplier = random.randint(2, 9)
    return "Multiply the single digit by a multiple of 10:", f"{multiplier} x {factor} = ____", multiplier * factor

def identify_sides():
    denom = random.choice([2, 3, 4, 6, 8])
    num = random.randint(1, denom - 1)
    visual = f"A shape is divided into {denom} equal parts, and {num} parts are shaded."
    return "What fraction of the shape is shaded?", visual, f"{num}/{denom}"

def count_specific_shape():
    val = random.randint(1, 5)
    visual = "-------\n" + "|     |\n" * val + "-------"
    return "Look at this number line split into equal segments. What fraction represents point A?", visual, f"{val}/{val}"

def match_3d_shape():
    n1 = random.randint(1, 4)
    d1 = random.choice([3, 4, 6, 8])
    n2 = n1 * 2
    d2 = d1 * 2
    return f"Which fraction is equivalent to {n1}/{d1}?\n1) {n2}/{d2}  2) 1/5  3) 7/9", "", 1

def ab_pattern():
    length = random.randint(3, 8)
    width = random.randint(3, 8)
    area = length * width
    visual = f"Length = {length} cm\nWidth = {width} cm"
    return "Find the total area of this rectangle in square centimeters:", visual, area

def size_sorting():
    side1 = random.randint(3, 9)
    side2 = random.randint(3, 9)
    side3 = random.randint(3, 9)
    side4 = random.randint(3, 9)
    perimeter = side1 + side2 + side3 + side4
    visual = f"Sides are: {side1} cm, {side2} cm, {side3} cm, and {side4} cm"
    return "Find the perimeter of this polygon in centimeters:", visual, perimeter

def attribute_matching():
    prompt = "Which subcategory do all squares, rectangles, and rhombuses belong to?\n1) Triangles  2) Quadrilaterals  3) Hexagons"
    return prompt, "", 2

def compare_height():
    v1 = random.randint(100, 500)
    v2 = random.randint(50, 200)
    return f"A bottle holds {v1} milliliters of water. A glass holds {v2} milliliters. How many milliliters do they hold together?", "", v1 + v2

def graph_reading():
    prompt = "A movie starts at 4:15 PM and lasts for 45 minutes. What time does the movie end?\n1) 4:45 PM  2) 5:00 PM  3) 5:30 PM"
    return prompt, "", 2

def weight_intuition():
    items = ["Apple", "Banana", "Orange"]
    weights = [random.randint(2, 5) for _ in items]
    visual = "\n".join([f"{item}: {'█' * w}" for item, w in zip(items, weights)])
    target = items[weights.index(max(weights))]
    return "Look at this bar graph. Which fruit scale bar shows the highest value?", visual, target

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
