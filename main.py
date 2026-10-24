from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os
import random

app = FastAPI(title="Unified Math Platform API (Calculator Engine & Question Matrix)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Safely load curriculum modules so an import issue doesn't crash the server on startup
GLOBAL_MODULE_CATALOG = {}

modules_config = {
    0: ("level_prek", "MATH_ROUTER"),
    1: ("level_k", "MATH_ROUTER"),
    2: ("level_1", "MATH_ROUTER"),
    3: ("level_2", "MATH_ROUTER"),
    4: ("level_3", "MATH_ROUTER"),
    5: ("level_4", "MATH_ROUTER"),
    6: ("level_5", "MATH_ROUTER"),
    7: ("level_6", "MATH_ROUTER"),
    8: ("level_7", "MATH_ROUTER"),
    9: ("level_8", "MATH_ROUTER"),
    10: ("level_geom", "MATH_ROUTER"),
    11: ("level_alg2", "MATH_ROUTER"),
    12: ("level_precalc", "MATH_ROUTER"),
    13: ("level_calc", "MATH_ROUTER"),
}

for grade_key, (mod_name, attr_name) in modules_config.items():
    try:
        mod = __import__(mod_name, fromlist=[attr_name])
        GLOBAL_MODULE_CATALOG[grade_key] = getattr(mod, attr_name)
    except Exception as e:
        print(f"Warning: Could not load module {mod_name}: {e}")

@app.get("/")
def home():
    return {
        "status": "online",
        "service": "Unified Render Math Service",
        "modules_loaded": len(GLOBAL_MODULE_CATALOG)
    }

# --- Question Generator API Route ---
@app.get("/api/question")
def serve_distributed_question(grade: int, category: int, sub_difficulty: int):
    if grade not in GLOBAL_MODULE_CATALOG:
        raise HTTPException(status_code=404, detail=f"Grade curriculum tier {grade} not found or failed to load.")
        
    target_router = GLOBAL_MODULE_CATALOG[grade]
    
    if category not in target_router or sub_difficulty not in target_router[category]:
        raise HTTPException(status_code=404, detail="Targeted question math matrix index not found.")
    
    question, visual, correct_answer = target_router[category][sub_difficulty]()
    
    choices = [correct_answer]
    if isinstance(correct_answer, int):
        distractors = [v for v in range(max(0, correct_answer - 15), correct_answer + 16) if v != correct_answer]
        choices.extend(random.sample(distractors, min(3, len(distractors))))
    else:
        choices.extend(["Alternative Distractor X", "Alternative Distractor Y", "Alternative Distractor Z"])
    
    random.shuffle(choices)
    
    return {
        "question": question,
        "visual": visual,
        "choices": [str(c) for c in choices],
        "correct_answer": str(correct_answer)
    }

# --- C++ Calculator Solver API Route ---
@app.post("/api/calculate")
def execute_calculator(payload: dict = Body(...)):
    expression = payload.get("expression", "")
    if not expression:
        raise HTTPException(status_code=400, detail="Expression cannot be empty.")
    
    binary_path = "./calculator_engine"
    if not os.path.exists(binary_path):
        if os.path.exists("calculator_engine.cpp"):
            compile_res = subprocess.run(["g++", "-O3", "calculator_engine.cpp", "-o", binary_path], capture_output=True, text=True)
            if compile_res.returncode != 0:
                raise HTTPException(status_code=500, detail=f"Compilation failed: {compile_res.stderr}")
        else:
            raise HTTPException(status_code=500, detail="Calculator engine binary/source missing.")

    try:
        process = subprocess.run(
            [binary_path],
            input=expression + "\n",
            capture_output=True,
            text=True,
            timeout=5
        )
        return {
            "output": process.stdout,
            "error": process.stderr
        }
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Calculator execution timed out.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
