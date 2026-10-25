import random
import math


def _pick_variant(options):
    return random.choice(options)


def count_items_1_6():
    x1, y1 = 0, 0
    x2, y2 = random.choice([3, 6, 5]), random.choice([4, 8, 12])
    dist = int(math.hypot(x2 - x1, y2 - y1))
    visual = f"grph seg({x1},{y1})({x2},{y2})"
    prompt = _pick_variant([
        "Find the linear coordinate distance length of this line segment using the coordinate distance formula:",
        "What is the distance between these two points?",
        "Use the distance formula to compute the segment length.",
        "Find the coordinate distance for the given segment."
    ])
    return prompt, visual, dist


def count_items_5_10():
    x1, y1 = random.choice([2, 4]), random.choice([2, 6])
    x2, y2 = random.choice([6, 8]), random.choice([4, 10])
    mx, my = (x1 + x2) // 2, (y1 + y2) // 2
    visual = f"grph pnt({x1},{y1}) pnt({x2},{y2})"
    prompt = _pick_variant([
        "Find the horizontal x-axis coordinate value for the midpoint of the segment connecting these two points:",
        "What is the x-coordinate of the midpoint?",
        "Locate the midpoint and identify its x-value.",
        "Compute the midpoint x-coordinate."
    ])
    return prompt, visual, mx


def missing_number_sequence():
    v1 = random.randint(40, 80)
    visual = f"grph seg(0,0)(5,0) seg(0,0)(4,3) lines forming vertical angles"
    prompt = _pick_variant([
        f"Two intersecting lines form vertical angles. If one angle measures {v1} degrees, what is the degree measure of its matching opposite vertical angle?",
        f"Find the measure of the vertical angle opposite {v1} degrees.",
        f"What is the value of the opposite vertical angle?",
        f"If one vertical angle is {v1} degrees, what is the other?"
    ])
    return prompt, visual, v1


def basic_addition():
    a = random.randint(35, 75)
    b = random.randint(35, 75)
    c = 180 - (a + b)
    visual = "grph seg(0,0)(5,0) seg(5,0)(2,3) seg(2,3)(0,0)"
    prompt = _pick_variant([
        f"Inside a triangle structure setup, two interior angles measure {a} and {b} degrees. Find the missing third interior angle metric calculation:",
        f"A triangle has angles {a} and {b}. What is the third angle?",
        f"Solve for the missing angle in the triangle.",
        f"Find the third angle of this triangle."
    ])
    return prompt, visual, c


def basic_subtraction():
    scale = random.choice([2, 3])
    a, b = 3, 4
    sa, sb = a * scale, b * scale
    visual = f"Triangle 1: sides 3, 4, 5. Triangle 2: sides {sa}, {sb}, x."
    prompt = _pick_variant([
        f"Two right triangles are geometrically similar. If the base scaling sides are matching pairs, find the length of missing hypotenuse side x:",
        f"The triangles are similar. Find the missing hypotenuse length.",
        f"Solve for x in the similar triangle proportion.",
        f"What is the missing side length?"
    ])
    return prompt, visual, 5 * scale


def compare_more():
    v1 = random.randint(15, 55)
    visual = "grph seg(0,0)(4,0) seg(0,0)(0,4) circle arc inside"
    prompt = _pick_variant([
        f"An angle inscribed inside a circle subtends an intercepted arc tracking element measuring {v1 * 2} degrees. Find the inscribed angle measure calculation:",
        f"If the intercepted arc is {v1 * 2} degrees, what is the inscribed angle?",
        f"Find the inscribed angle from the arc measure.",
        f"Compute the angle from the intercepted arc."
    ])
    return prompt, visual, v1


def identify_sides():
    b = random.randint(5, 12)
    h = random.randint(4, 10)
    visual = f"grph seg(0,0)({b},0) seg(0,0)(0,{h}) seg(0,{h})({b},0)"
    prompt = _pick_variant([
        "Find the total interior geometric surface layer area of this right triangle frame configuration:",
        "What is the area of this right triangle?",
        "Compute the area of the triangle.",
        "Find the triangle’s area using the base and height."
    ])
    return prompt, visual, (b * h) // 2


def count_specific_shape():
    r = random.choice([7, 14])
    area = int((22 / 7) * r * r)
    visual = f"grph y = sqrt({r**2} - x^2); y = -sqrt({r**2} - x^2)"
    prompt = _pick_variant([
        "Compute the total geometric boundary area enclosed inside this circle configuration layout: Area = pi * r^2 (Use pi = 22/7)",
        "What is the area of the circle?",
        "Find the enclosed area of the circle.",
        "Calculate the area using the radius."
    ])
    return prompt, visual, area


def match_3d_shape():
    r = random.choice([3, 5])
    h = random.choice([6, 9])
    vol = int((1 / 3) * 3.14 * r * r * h)
    visual = f"Cone profile dimensions: base radius = {r} cm, height dimension = {h} cm"
    prompt = _pick_variant([
        "Compute the third-grade structural volume calculation framework profile output for this cone setup: Volume = (1/3) * pi * r^2 * h",
        "What is the volume of this cone?",
        "Find the cone’s volume.",
        "Use the formula to compute the cone volume."
    ])
    return prompt, visual, vol


def ab_pattern():
    v1 = random.randint(35, 75)
    prompt = _pick_variant([
        f"An angle tracking measurement is {v1} degrees. What is the total degree measurement of its complementary angle partner sequence?",
        f"Find the complement of {v1} degrees.",
        f"What angle goes with {v1} degrees to make 90°?",
        f"Determine the complementary angle."
    ])
    return prompt, "", 90 - v1


def size_sorting():
    v1 = random.randint(45, 135)
    prompt = _pick_variant([
        f"An angle tracking measurement is {v1} degrees. What is the total degree measurement of its supplementary angle partner sequence?",
        f"Find the supplement of {v1} degrees.",
        f"What angle goes with {v1} degrees to make 180°?",
        f"Determine the supplementary angle."
    ])
    return prompt, "", 180 - v1


def attribute_matching():
    prompt = _pick_variant([
        "Which mapping constraint transformation flips a geometric figure across a specified line boundary vector field to produce a mirror image layout?\n1) Reflection alignment\n2) Translation shift\n3) Rotation turn",
        "Which transformation creates a mirror image?\n1) Reflection alignment\n2) Translation shift\n3) Rotation turn",
        "Choose the correct geometric transformation.\n1) Reflection alignment\n2) Translation shift\n3) Rotation turn",
        "A mirror image across a line is what type of transformation?\n1) Reflection alignment\n2) Translation shift\n3) Rotation turn"
    ])
    return prompt, "", 1


def compare_height():
    prompt = _pick_variant([
        "Which geometric descriptor defines a precise structural line track that intersects a segment exactly at its center point while maintaining a 90-degree angle?\n1) Perpendicular bisector\n2) Angle bisector\n3) Parallel line",
        "Which line intersects a segment at its midpoint at a right angle?\n1) Perpendicular bisector\n2) Angle bisector\n3) Parallel line",
        "Select the correct segment special line.\n1) Perpendicular bisector\n2) Angle bisector\n3) Parallel line",
        "What is the name of the line that cuts a segment in half at a right angle?\n1) Perpendicular bisector\n2) Angle bisector\n3) Parallel line"
    ])
    return prompt, "", 1


def graph_reading():
    prompt = _pick_variant([
        "Which tracking operation matches a sequence of geometric transformations that preserve the original size and shape dimensions layout properties?\n1) Rigid motion congruence transformation\n2) Dilation stretch\n3) Shear distortion",
        "Which transformation preserves shape and size?\n1) Rigid motion congruence transformation\n2) Dilation stretch\n3) Shear distortion",
        "Choose the transformation that keeps size and shape unchanged.\n1) Rigid motion congruence transformation\n2) Dilation stretch\n3) Shear distortion",
        "A congruence transformation is which of these?\n1) Rigid motion congruence transformation\n2) Dilation stretch\n3) Shear distortion"
    ])
    return prompt, "", 1


def weight_intuition():
    prompt = _pick_variant([
        "Which path describes the longest possible line track connecting two boundary points across a circle while passing through the center location metric?\n1) Diameter track lines\n2) Radius segment\n3) Chord line",
        "What is the longest line across a circle through its center called?\n1) Diameter track lines\n2) Radius segment\n3) Chord line",
        "Choose the correct term.\n1) Diameter track lines\n2) Radius segment\n3) Chord line",
        "The line through the center connecting two points on a circle is called: \n1) Diameter track lines\n2) Radius segment\n3) Chord line"
    ])
    return prompt, "", 1


MATH_ROUTER = {
    1: {1: count_items_1_6, 2: count_items_5_10, 3: missing_number_sequence},
    2: {1: basic_addition, 2: basic_subtraction, 3: compare_more},
    3: {1: identify_sides, 2: count_specific_shape, 3: match_3d_shape},
    4: {1: ab_pattern, 2: size_sorting, 3: attribute_matching},
    5: {1: compare_height, 2: graph_reading, 3: weight_intuition}
}
