import random

def count_items_1_6():
    v1 = random.randint(-15, -2)
    v2 = random.randint(3, 15)
    return "Solve the integer addition problem:", f"{v1} + {v2} = ____", v1 + v2

def count_items_5_10():
    v1 = random.randint(-10, -2)
    v2 = random.randint(-8, -2)
    return "Solve the integer multiplication problem:", f"({v1}) x ({v2}) = ____", v1 * v2

def missing_number_sequence():
    item_cost = random.randint(15, 45)
    markup_pct = random.choice([10, 20, 50])
    ans = int(item_cost * (1 + markup_pct / 100))
    visual = f"Wholesale Price = ${item_cost}, Store Markup = {markup_pct}%"
    return "Calculate the final retail selling price of the item after markup:", visual, ans

def basic_addition():
    ans = random.randint(2, 8)
    coef = random.randint(2, 5)
    const = random.randint(3, 12)
    total = (coef * ans) + const
    return f"Solve the two-step linear equation for x: {coef}x + {const} = {total}", "", ans

def basic_subtraction():
    ans = random.randint(3, 9)
    coef = random.randint(2, 5)
    const = random.randint(2, 10)
    total = (coef * ans) - const
    return f"Solve the two-step linear equation for x: {coef}x - {const} = {total}", "", ans

def compare_more():
    v1 = random.randint(2, 6)
    ans = random.randint(2, 6)
    total = v1 * ans
    return f"Solve the inequality structure calculation: {v1}x > {total}\n1) x > {ans}  2) x < {ans}", "", 1

def identify_sides():
    radius = random.choice([7, 14, 21])
    ans = int(2 * (22 / 7) * radius)
    return "Find the total circumference distance of a circular frame boundary:", f"Radius = {radius} cm (Use pi = 22/7)", ans

def count_specific_shape():
    radius = random.choice([7, 14, 21])
    ans = int((22 / 7) * radius * radius)
    return "Find the complete surface area coverage of a circular element layout:", f"Radius = {radius} cm (Use pi = 22/7)", ans

def match_3d_shape():
    v1 = random.choice([30, 45, 60, 90])
    return f"Two angles are complementary. If one angle measures {v1} degrees, what is the measure of its complement?", "", 90 - v1

def ab_pattern():
    v1 = random.choice([30, 60, 90, 120])
    return f"Two angles form a linear pair and are supplementary. If one angle measures {v1} degrees, what is the measure of its supplement?", "", 180 - v1

def size_sorting():
    total_marbles = 20
    red_marbles = random.randint(3, 8)
    return f"A bag contains {total_marbles} total items. If {red_marbles} of them are red, what is the probability of pulling a red item at random?\n1) {red_marbles}/{total_marbles}  2) 1/2  3) 0", "", 1

def attribute_matching():
    prompt = "Which tracking option defines a sample population configuration that accurately represents an entire school?\n1) Every 5th student entering the school building\n2) Only members of the varsity football squad\n3) Only the teachers in the science department"
    return prompt, "", 1

def compare_height():
    v1 = random.randint(5, 15)
    v2 = random.randint(2, 4)
    return f"A map scale uses 1 inch to represent {v1} real miles. If a road measures {v2} inches on the map grid, how long is it in reality?", "", v1 * v2

def graph_reading():
    v1 = random.randint(2, 6)
    return f"Identify the constant of proportionality unit rate from the direct equation framework: y = {v1}x", "", v1

def weight_intuition():
    prompt = "If a coin is tossed 1000 times, which outcome projection aligns best with probability data standards?\n1) Close to 500 heads\n2) Exactly 1000 heads\n3) Exactly 0 heads"
    return prompt, "", 1

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
