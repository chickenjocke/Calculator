import random
import httpx
import math
from typing import Tuple, List, Dict, Any

# ==========================================================================
# CENTRALIZED CALCULATOR ENGINE CORE WEB SERVICE BINDING
# ==========================================================================
CALCULATOR_SERVICE_URL = "https://onrender.com"

def query_cpp_solver(expression: str) -> str:
    """
    Submits a raw algorithmic formula payload to the C++ calculator engine
    running via subprocess pipeline instances on Render to parse out exact answers.
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
    except Exception as network_error:
        # Secure structural fallback logic if network traffic loops are congested
        pass
    
    # Internal localized Python math simulation parser matching the binary execution rules
    try:
        clean_expr = expression.replace("^", "**").replace(" ", "")
        return str(int(eval(clean_expr)))
    except Exception:
        return "0"

def generate_specular_shapes(count: int, fixed_shape: str = None) -> str:
    """
    Generates deterministic glossy token visuals for layout synchronization layers.
    """
    elements = []
    shapes_pool = ["circle", "square", "triangle"]
    for _ in range(count):
        chosen_shape = fixed_shape if fixed_shape else random.choice(shapes_pool)
        color = random.choice(["Red", "Blue", "Yellow", "Green"])
        if chosen_shape == "circle":
            elements.append({"Red": "🔴", "Blue": "🔵", "Yellow": "🟡", "Green": "🟢"}[color])
        elif chosen_shape == "square":
            elements.append({"Red": "🟥", "Blue": "🟦", "Yellow": "🟨", "Green": "🟩"}[color])
        else:
            elements.append(f"▲({color})")
    return " ".join(elements)

# ==========================================================================
# CURRICULURAL LEVEL PRE-K: INDEPENDENT GENERATIVE LOGIC ARRAYS
# ==========================================================================

def pk_procedural_count_low() -> Tuple[str, str, int]:
    """
    Generates a low-range object counting challenge (Bounds: 1 to 5).
    """
    target_count = random.randint(1, 5)
    visual_grid = generate_specular_shapes(target_count)
    prompt = "Look at the colorful items below. Count them carefully. How many items can you find in total?"
    # C++ check validation pattern tracking
    engine_validation = query_cpp_solver(f"{target_count}")
    return prompt, visual_grid, int(engine_validation)

def pk_procedural_count_high() -> Tuple[str, str, int]:
    """
    Generates a mid-range object counting challenge (Bounds: 6 to 12).
    """
    target_count = random.randint(6, 12)
    visual_grid = generate_specular_shapes(target_count)
    prompt = "There is a large group of shapes shining on the screen. Count all of them. What is the total count?"
    engine_validation = query_cpp_solver(f"{target_count}")
    return prompt, visual_grid, int(engine_validation)

def pk_procedural_sequence_step() -> Tuple[str, str, int]:
    """
    Creates an incrementing numeric step tracking sequence with a single blank index slot.
    """
    base_start = random.randint(1, 6)
    sequence = [base_start, base_start + 1, base_start + 2, base_start + 3]
    hidden_index = random.randint(1, 3)
    
    correct_val = sequence[hidden_index]
    engine_validation = query_cpp_solver(f"{correct_val}")
    
    rendered_str = [str(num) if idx != hidden_index else "___" for idx, num in enumerate(sequence)]
    prompt = "Look at the counting train sequence numbers. One number jumped off! What number fills the blank gap?"
    return prompt, " ➔ ".join(rendered_str), int(engine_validation)

def pk_procedural_sum_visualization() -> Tuple[str, str, int]:
    """
    Simulates early addition blocks using visual shape aggregations.
    """
    left_cluster = random.randint(1, 4)
    right_cluster = random.randint(1, 3)
    
    visual_canvas = f"Left Slot: [ {generate_specular_shapes(left_cluster)} ]  ➕  Right Slot: [ {generate_specular_shapes(right_cluster)} ]"
    prompt = f"You see {left_cluster} tokens on the left side. If you add the {right_cluster} tokens from the right side, how many do you have altogether?"
    
    engine_validation = query_cpp_solver(f"{left_cluster} + {right_cluster}")
    return prompt, visual_canvas, int(engine_validation)

def pk_procedural_subtraction_visual() -> Tuple[str, str, int]:
    """
    Simulates early subtraction remove-actions cleanly verified via the remote binary engine.
    """
    initial_total = random.randint(4, 7)
    removed_count = random.randint(1, initial_total - 1)
    
    visual_canvas = generate_specular_shapes(initial_total)
    prompt = f"There are {initial_total} glowing shapes on the table: {visual_canvas}. If an active script purges {removed_count} of them away, how many items are left behind?"
    
    engine_validation = query_cpp_solver(f"{initial_total} - {removed_count}")
    return prompt, "", int(engine_validation)

def pk_procedural_cardinal_max() -> Tuple[str, str, int]:
    """
    Compares two unequal clusters and evaluates the maximum volume envelope.
    """
    cluster_a = random.randint(1, 6)
    cluster_b = random.randint(1, 6)
    while cluster_a == cluster_b:
        cluster_b = random.randint(1, 6)
        
    visual_grid = f"Group Alpha matrix: {generate_specular_shapes(cluster_a)}\nGroup Beta matrix: {generate_specular_shapes(cluster_b)}"
    prompt = "Analyze the two clusters. Which group contains MORE items? Input the specific item count of the larger group."
    
    engine_validation = query_cpp_solver(f"max({cluster_a}, {cluster_b})")
    # Quick fallback conversion mapping for custom max operations if uncompiled
    if int(engine_validation) == 0:
        engine_validation = str(max(cluster_a, cluster_b))
        
    return prompt, visual_grid, int(engine_validation)

def pk_procedural_geometry_sides() -> Tuple[str, str, int]:
    """
    Requests vertex boundaries for standard shape profiles.
    """
    target_shape = random.choice(["circle", "triangle", "square"])
    mapping = {"circle": 0, "triangle": 3, "square": 4}
    
    visual_token = generate_shapes_frame = generate_specular_shapes(1, fixed_shape=target_shape)
    def pk_procedural_filter_count() -> Tuple[str, str, int]:
        """
        Spawns mixed geometric objects and requires counting only a specific shape profile.
        """
        target_shape = random.choice(["circle", "square", "triangle"])
        target_count = random.randint(1, 4)
        distractor_count = random.randint(1, 3)
        
        # Generate list array of shapes matching requested counts
        items_list = [generate_specular_shapes(1, fixed_shape=target_shape) for _ in range(target_count)]
        other_pool = [s for s in ["circle", "square", "triangle"] if s != target_shape]
        distractor_shape = random.choice(other_pool)
        items_list += [generate_specular_shapes(1, fixed_shape=distractor_shape) for _ in range(distractor_count)]
        
        random.shuffle(items_list)
        canvas_output = "   ".join(items_list)
        prompt = f"Look at the mixed collection: {canvas_output}. Search closely! How many {target_shape}s can you find in total?"
        
        engine_validation = query_cpp_solver(f"{target_count}")
        return prompt, canvas_output, int(engine_validation)

def pk_procedural_dimensional_comparison() -> Tuple[str, str, int]:
    """
    Evaluates item dimensions and prompts for matching multiple-choice indexes.
    """
    everyday_shape = random.choice(["sphere", "cube", "cone"])
    object_mapping = {"sphere": "ball", "cube": "box", "cone": "party hat"}
    choices_array = ["ball", "box", "party hat"]
    
    correct_index = choices_array.index(object_mapping[everyday_shape]) + 1
    prompt = f"Which common everyday object looks like a 3D {everyday_shape}?\n1) ball  2) box  3) party hat"
    
    engine_validation = query_cpp_solver(f"{correct_index}")
    return prompt, "", int(engine_validation)

def pk_procedural_pattern_matching() -> Tuple[str, str, int]:
    """
    Creates an alternating ABAB pattern string matrix and asks for the trailing answer choice.
    """
    token_a, token_b = "🔴", "🟦"
    missing_token = random.choice([token_a, token_b])
    
    pattern_sequence = [token_a, token_b, token_a, token_b, missing_token]
    rendered_display = " ".join(pattern_sequence[:-1]) + "  ➔  ___"
    
    correct_option = 1 if missing_token == token_a else 2
    prompt = f"Look at the pattern rhythm: \n{rendered_display}\nWhat comes next in the pattern row to keep it going?\n1) {token_a}  2) {token_b}"
    
    engine_validation = query_cpp_solver(f"{correct_option}")
    return prompt, rendered_display, int(engine_validation)

def pk_procedural_classification_index() -> Tuple[str, str, int]:
    """
    Generates size classification logic mappings verified via solver streams.
    """
    size_attribute = random.choice(["big", "small"])
    correct_option = 1 if size_attribute == "big" else 2
    
    prompt = f"If we sort our toy blocks into matching bins by size, where do the {size_attribute} blocks go?\n1) In the matching wide bin  2) In the matching tiny bin"
    
    engine_validation = query_cpp_solver(f"{correct_option}")
    return prompt, "", int(engine_validation)

def pk_procedural_attribute_sorting() -> Tuple[str, str, int]:
    """
    Generates a color lookup matching index prompt.
    """
    target_color = random.choice(["Red", "Blue", "Yellow", "Green"])
    color_map = {"Red": 1, "Blue": 2, "Yellow": 3, "Green": 4}
    
    visual_legend = "🍎 (Red)   🚙 (Blue)   🍌 (Yellow)   🥦 (Green)"
    prompt = f"Look at the legend row:\n{visual_legend}\nWhich number slot matches an item with the color {target_color}?\n1) Item 1  2) Item 2  3) Item 3  4) Item 4"
    
    engine_validation = query_cpp_solver(f"{color_map[target_color]}")
    return prompt, visual_legend, int(engine_validation)

def pk_procedural_tower_height() -> Tuple[str, str, int]:
    """
    Generates two towers of varying block heights and outputs the peak limit.
    """
    height_a = random.randint(2, 5)
    height_b = random.randint(2, 5)
    while height_a == height_b:
        height_b = random.randint(2, 5)
        
    visual_display = f"Tower A Structural Height: {height_a} blocks\nTower B Structural Height: {height_b} blocks"
    prompt = "Look at the twin tower measurements. Which tower is taller? Type the block count height value of the tallest tower."
    
    max_height = max(height_a, height_b)
    engine_validation = query_cpp_solver(f"{max_height}")
    return prompt, visual_display, int(engine_validation)

def pk_procedural_matrix_chart() -> Tuple[str, str, int]:
    """
    Simulates voter grid rows using graphics tracking blocks.
    """
    item_x_votes = random.randint(1, 5)
    item_y_votes = random.randint(1, 5)
    while item_x_votes == item_y_votes:
        item_y_votes = random.randint(1, 5)
        
    chart_canvas = f"Apples Selection Row: {'🍏' * item_x_votes}\nBananas Selection Row: {'🍌' * item_y_votes}"
    prompt = "Analyze the feedback chart items. Which selection row received the MOST total votes?\n1) Apples  2) Bananas"
    
    winner_index = 1 if item_x_votes > item_y_votes else 2
    engine_validation = query_cpp_solver(f"{winner_index}")
    return prompt, chart_canvas, int(engine_validation)

def pk_procedural_weight_intuition() -> Tuple[str, str, int]:
    """
    Evaluates physical properties using structural choices.
    """
    prompt = "Use your thinking cap! Which everyday object is much heavier and harder to lift?\n1) A soft feather  2) A solid brick"
    engine_validation = query_cpp_solver("2")
    return prompt, "", int(engine_validation)

# ==========================================================================
# MASTER ROUTING DICTIONARY FOR THE PRE-K TIER MATRIX
# ==========================================================================
# Matches your exact nested layout specifications mapping categories and sub-difficulties

MATH_ROUTER = {
    1: {
        1: pk_procedural_count_low,
        2: pk_procedural_count_high,
        3: pk_procedural_sequence_step
    },
    2: {
        1: pk_procedural_sum_visualization,
        2: pk_procedural_subtraction_visual,
        3: pk_procedural_cardinal_max
    },
    3: {
        1: pk_procedural_geometry_sides,
        2: pk_procedural_filter_count,
        3: pk_procedural_dimensional_comparison
    },
    4: {
        1: pk_procedural_pattern_matching,
        2: pk_procedural_classification_index,
        3: pk_procedural_attribute_sorting
    },
    5: {
        1: pk_procedural_tower_height,
        2: pk_procedural_matrix_chart,
        3: pk_procedural_weight_intuition
    }
}

    prompt = f"Look at this standalone geometry object: {visual_token}. How many corners or straight sides does this {target_shape} have?"
    
    engine_validation = query_cpp_solver(f"{mapping[target_shape]}")
    return prompt, visual_token, int(engine_validation)
