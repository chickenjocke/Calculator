import random

def count_items_1_6():
    steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    idx = random.randint(2, 6)
    target = steps[idx]
    seq_str = [str(x) if i != idx else "___" for i, x in enumerate(steps[:7])]
    return "What number is missing when counting by tens?", " ".join(seq_str), target

def count_items_5_10():
    tens = random.randint(2, 6)
    ones = random.randint(1, 9)
    total = (tens * 10) + ones
    board = f"Blocks: {tens} bundles of 10 and {ones} single blocks."
    return "What total number do these blocks show?", board, total

def missing_number_sequence():
    n1 = random.randint(11, 99)
    n2 = random.randint(11, 99)
    while n1 == n2:
        n2 = random.randint(11, 99)
    return f"Which number is GREATER?\n1) {n1}  2) {n2}", "", max(n1, n2)

def basic_addition():
    v1 = random.randint(5, 12)
    v2 = random.randint(3, 8)
    return "Solve the addition problem:", f"{v1} + {v2} = ____", v1 + v2

def basic_subtraction():
    v1 = random.randint(11, 20)
    v2 = random.randint(4, 10)
    return "Solve the subtraction problem:", f"{v1} - {v2} = ____", v1 - v2

def compare_more():
    v1 = random.randint(4, 8)
    v2 = random.randint(1, 3)
    use_plus = random.choice([True, False])
    if use_plus:
        display = f"{v1} ___ {v2} = {v1 + v2}\n1) +  2) -"
        return "Which sign makes the equation true?", display, 1
    else:
        display = f"{v1} ___ {v2} = {v1 - v2}\n1) +  2) -"
        return "Which sign makes the equation true?", display, 2

def identify_sides():
    hour = random.randint(1, 12)
    minute = random.choice([0, 30])
    time_str = f"{hour}:00" if minute == 0 else f"{hour}:30"
    clock_desc = f"The short hand points at {hour}. The long hand points at {'12' if minute == 0 else '6'}."
    return "What time does this clock show?", clock_desc, time_str

def count_specific_shape():
    prompt = "If you cut a pizza into 2 equal pieces, what is 1 piece called?\n1) a half  2) a quarter"
    return prompt, "", 1

def match_3d_shape():
    prompt = "How many equal pieces make up a whole item cut into QUARTERS?", "", 4

def ab_pattern():
    shape = random.choice(["pentagon", "hexagon", "rectangle"])
    corners = {"pentagon": 5, "hexagon": 6, "rectangle": 4}[shape]
    return f"How many corners does a {shape} have?", "", corners

def size_sorting():
    prompt = "Which trait tells us an object is definitely a TRIANGLE?\n1) It is red  2) It is small  3) It has 3 straight sides"
    return prompt, "", 3

def attribute_matching():
    prompt = "If you put two equal triangles side-by-side along their flat edges, what shape can you make?\n1) A circle  2) A square  3) A cone"
    return prompt, "", 2

def compare_height():
    prompt = "Object A is longer than Object B. Object B is longer than Object C. Which is the longest?\n1) Object A  2) Object B  3) Object C", "", 1

def graph_reading():
    votes = random.randint(4, 8)
    tally_str = "".join(["|" for _ in range(votes)])
    return "How many votes does this tally show?", f"Votes: {tally_str}", votes

def weight_intuition():
    cats = random.randint(3, 6)
    rabbits = random.randint(3, 6)
    while cats == rabbits:
        rabbits = random.randint(3, 6)
    graph = f"Cats: {'■'*cats}\nRabbits: {'■'*rabbits}"
    return "Which pet got MORE total votes?\n1) Cats  2) Rabbits", graph, 1 if cats > rabbits else 2

MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
