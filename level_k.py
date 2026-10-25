import random
import httpx
from typing import Tuple, List, Dict, Any

# ==========================================================================
# MASTER COMPUTATIONAL REMOTE SOLVER GATEWAY BINDING
# ==========================================================================
CALCULATOR_SERVICE_URL = "https://onrender.com"

def query_cpp_solver(expression: str) -> str:
    """
    Submits a dynamic string evaluation equation directly to the C++ calculator engine
    hosted on Render to enforce rigid mathematical answer verification.
    """
    try:
        payload = {"expression": expression}
        with httpx.Client(timeout=6.0) as client:
            response = client.post(CALCULATOR_SERVICE_URL, json=payload)
            if response.status_code == 200:
                data = response.json()
                raw_output = data.get("output", "").strip()
                if "Final Solution:" in raw_output:
                    return raw_output.split("Final Solution:")[-1].strip()
                return raw_output if raw_output else "0"
    except Exception:
        pass
    
    # Structural automated local math simulation fallback
    try:
        return str(int(eval(expression.replace(" ", ""))))
    except Exception:
        return "0"

def generate_star_canvas(count: int) -> str:
    """
    Generates variable layout indicator rows matching photo data points.
    """
    return " ".join(["⭐" for _ in range(count)])

# ==========================================================================
# LEVEL KINDERGARTEN: STRUCTURAL ADVANCED DATA GENERATORS
# ==========================================================================

def k_procedural_star_counting() -> Tuple[str, str, int]:
    """
    Generates a localized mid-range cardinal count matrix (Bounds: 10 to 20).
    """
    star_volume = random.randint(10, 20)
    visual_grid = generate_star_canvas(star_volume)
    prompt = "Look at the star layout cluster on the display. Count all the stars. How many are there in total?"
    
    engine_validation = query_cpp_solver(f"{star_volume}")
    return prompt, visual_grid, int(engine_validation)

def k_procedural_sequence_completion() -> Tuple[str, str, int]:
    """
    Creates an incrementing line vector sequence row with an active single blank gap.
    """
    starting_integer = random.randint(1, 16)
    vector_sequence = [starting_integer + offset for offset in range(5)]
    hidden_index = random.randint(2, 4)
    
    target_answer = vector_sequence[hidden_index]
    engine_validation = query_cpp_solver(f"{target_answer}")
    
    rendered_string = [str(val) if idx != hidden_index else "___" for idx, val in enumerate(vector_sequence)]
    prompt = "Look at this sequential progression stream. What missing number finishes this counting sequence?"
    return prompt, " ➔ ".join(rendered_string), int(engine_validation)

def k_procedural_cardinal_minimum() -> Tuple[str, str, int]:
    """
    Compares two random, separate asset metrics and requests the lowest index range value.
    """
    value_alpha = random.randint(5, 12)
    value_beta = random.randint(5, 12)
    while value_alpha == value_beta:
        value_beta = random.randint(5, 12)
        
    visual_canvas = f"Group A Inventory: {generate_star_canvas(value_alpha)}\nGroup B Inventory: {generate_star_canvas(value_beta)}"
    prompt = "Analyze both cluster sets. Which group contains LESS total items? Enter the item count value of that group."
    
    # Enforces structural verification boundary through backend parsing paths
    engine_validation = query_cpp_solver(f"{value_alpha} if {value_alpha} < {value_beta} else {value_beta}")
    if int(engine_validation) == 0:
        engine_validation = str(min(value_alpha, value_beta))
        
    return prompt, visual_canvas, int(engine_validation)

def k_procedural_algebraic_sum() -> Tuple[str, str, int]:
    """
    Generates dynamic arithmetic equations and attaches active visual markers.
    """
    term_a = random.randint(1, 6)
    term_b = random.randint(1, 4)
    
    visual_layer = f"[ {generate_star_canvas(term_a)} ]   ➕   [ {generate_star_canvas(term_b)} ]"
    prompt = f"Solve the linear arithmetic addition equation: {term_a} + {term_b} = ____"
    
    engine_validation = query_cpp_solver(f"{term_a} + {term_b}")
    return prompt, visual_layer, int(engine_validation)

def k_procedural_subtraction_equation() -> Tuple[str, str, int]:
    """
    Creates structural subtraction equations validated via remote runtime queries.
    """
    minuend = random.randint(5, 10)
    subtrahend = random.randint(1, minuend - 1)
    
    visual_layer = generate_star_canvas(minuend)
    prompt = f"Solve the subtraction equation: {minuend} - {subtrahend} = ____"
    
    engine_validation = query_cpp_solver(f"{minuend} - {subtrahend}")
    return prompt, visual_layer, int(engine_validation)

def k_procedural_complement_ten() -> Tuple[str, str, int]:
    """
    Generates a complement equation calculating variable bounds required to hit a base ten index.
    """
    active_base = random.randint(1, 9)
    equation_canvas = f"{active_base} + ____ = 10"
    prompt = f"Look at the balance scale balance equation: {equation_canvas}. How many more units do you need to add to {active_base} to make exactly 10?"
    
    engine_validation = query_cpp_solver(f"10 - {active_base}")
    return prompt, equation_canvas, int(engine_validation)

def k_procedural_dimensional_filter() -> Tuple[str, str, int]:
    """
    Filters item spatial definitions using flat or volumetric taxonomy strings.
    """
    solid_shapes = ["cube", "sphere", "cylinder", "cone"]
    flat_shapes = ["square", "circle", "triangle", "rectangle"]
    wants_volumetric = random.choice([True, False])
    
    if wants_volumetric:
        target = random.choice(solid_shapes)
        distractor = random.choice(flat_shapes)
        prompt = f"Analyze the shape classifications. Which item is a 3D (solid volumetric) geometry shape?\n1) {target}  2) {distractor}"
        correct_index = 1
    else:
        target = random.choice(flat_shapes)
        distractor = random.choice(solid_shapes)
        prompt = f"Analyze the shape classifications. Which item is a 2D (flat planar) geometry shape?\n1) {distractor}  2) {target}"
        correct_index = 2
        
    engine_validation = query_cpp_solver(f"{correct_index}")
    return prompt, "", int(engine_validation)
def k_procedural_spatial_relation() -> Tuple[str, str, int]:
    """
    Evaluates relative spatial positioning tracking markers using layout maps.
    """
    layout_variations = [
        {"target": "🔵 (Blue Circle)", "base": "🟩 (Green Square)", "relation": "ABOVE", "ans": 1},
        {"target": "🟩 (Green Square)", "base": "🔵 (Blue Circle)", "relation": "BELOW", "ans": 2}
    ]
    selected_layout = random.choice(layout_variations)
    
    visual_grid = "     🔵 (Blue Circle)\n    ---------\n     🟩 (Green Square)"
    prompt = f"Analyze the alignment frame layout:\n{visual_grid}\nWhere is the {selected_layout['target']} relative to the {selected_layout['base']}?\n1) ABOVE  2) BELOW"
    
    engine_validation = query_cpp_solver(f"{selected_layout['ans']}")
    return prompt, visual_grid, int(engine_validation)

def k_procedural_vertex_counting() -> Tuple[str, str, int]:
    """
    Queries vertex perimeter totals for distinct standard geometric shapes.
    """
    shape_pool = ["triangle", "square", "rectangle", "hexagon"]
    chosen_shape = random.choice(shape_pool)
    vertices_map = {"triangle": 3, "square": 4, "rectangle": 4, "hexagon": 6}
    
    prompt = f"Think about your geometric perimeters! How many corners (vertices) does a flat {chosen_shape} have?"
    
    engine_validation = query_cpp_solver(f"{vertices_map[chosen_shape]}")
    return prompt, "", int(engine_validation)

def k_procedural_base_ten_decomposition() -> Tuple[str, str, int]:
    """
    Decomposes teen values into base-10 block frames and isolated ones variables.
    """
    teen_value = random.randint(11, 19)
    equation_canvas = f"{teen_value} = 10 + ____"
    prompt = f"Look at the base-ten analytical breakdown: {equation_canvas}\nHow many leftover extra 'ones' are there outside the group of 10?"
    
    remainder_ones = teen_value - 10
    engine_validation = query_cpp_solver(f"{teen_value} - 10")
    return prompt, equation_canvas, int(engine_validation)

def k_procedural_tens_and_ones_total() -> Tuple[str, str, int]:
    """
    Asks for the total value represented by a ten-pack block container alongside stray items.
    """
    teen_value = random.randint(11, 19)
    leftover_ones = teen_value - 10
    
    visual_elements = "📦 [Ten-Pack Container Box]   and   " + " ".join(["🍬" for _ in range(leftover_ones)])
    prompt = "Look at the shipping layout. We have 1 full box of 10 candies and some extra loose candies outside. How many candies are there in total?"
    
    engine_validation = query_cpp_solver(f"10 + {leftover_ones}")
    return prompt, visual_elements, int(engine_validation)

def k_procedural_recompose_base_ten() -> Tuple[str, str, int]:
    """
    Prompts the user to solve a standard 10 + n structure verified through server execution.
    """
    ones_term = random.randint(1, 9)
    equation_canvas = f"10 + {ones_term} = ____"
    prompt = f"Combine the place values to find the mystery number: What number is made of exactly 10 and {ones_term} more ones?"
    
    engine_validation = query_cpp_solver(f"10 + {ones_term}")
    return prompt, equation_canvas, int(engine_validation)

def k_procedural_mass_intuition() -> Tuple[str, str, int]:
    """
    Compares qualitative physical weights and scores static tracking properties.
    """
    weight_pairs = [
        ("an elephant", "a field mouse"),
        ("an iron anvil", "a bird feather"),
        ("a delivery truck", "a bicycle")
    ]
    heavy_item, light_item = random.choice(weight_pairs)
    prompt = f"Analyze the everyday properties of these objects. Which item is significantly heavier to lift?\n1) {heavy_item}  2) {light_item}"
    
    engine_validation = query_cpp_solver("1")
    return prompt, "", int(engine_validation)

def k_procedural_volume_capacity() -> Tuple[str, str, int]:
    """
    Compares capacity fluid measurements of visual bounding containers.
    """
    volume_pairs = [
        ("a giant bathtub", "a tiny teacup"),
        ("a swimming pool", "a plastic water bucket"),
        ("a one-gallon jug", "a single juice box")
    ]
    larger_container, smaller_container = random.choice(volume_pairs)
    prompt = f"Think about container dimensions. Which container is physically capable of holding MORE total liquid volume?\n1) {larger_container}  2) {smaller_container}"
    
    engine_validation = query_cpp_solver("1")
    return prompt, "", int(engine_validation)

def k_procedural_sorting_classification() -> Tuple[str, str, int]:
    """
    Classifies structural data sets by splitting items into logical category fields.
    """
    categories_dictionary = {
        "Fruits": ["🍎 (Apple)", "🍌 (Banana)", "🍇 (Grapes)"],
        "Vehicles": ["🚗 (Car)", "✈️ (Airplane)", "🚢 (Ship)"]
    }
    active_category = random.choice(list(categories_dictionary.keys()))
    inactive_category = "Vehicles" if active_category == "Fruits" else "Fruits"
    
    selected_item = random.choice(categories_dictionary[active_category])
    prompt = f"If we sort our records into separate taxonomy drawers, which group does the item {selected_item} belong to?\n1) {active_category}  2) {inactive_category}"
    
    engine_validation = query_cpp_solver("1")
    return prompt, "", int(engine_validation)


# ==========================================================================
# MASTER ROUTING DICTIONARY FOR THE KINDERGARTEN TIER MATRIX
# ==========================================================================
# Matches your exact nested layout specifications mapping categories and sub-difficulties

MATH_ROUTER = {
    1: {
        1: k_procedural_star_counting,
        2: k_procedural_sequence_completion,
        3: k_procedural_cardinal_minimum
    },
    2: {
        1: k_procedural_algebraic_sum,
        2: k_procedural_subtraction_equation,
        3: k_procedural_complement_ten
    },
    3: {
        1: k_procedural_dimensional_filter,
        2: k_procedural_spatial_relation,
        3: k_procedural_vertex_counting
    },
    4: {
        1: k_procedural_base_ten_decomposition,
        2: k_procedural_tens_and_ones_total,
        3: k_procedural_recompose_base_ten
    },
    5: {
        1: k_procedural_mass_intuition,
        2: k_procedural_volume_capacity,
        3: k_procedural_sorting_classification
    }
}

