from fastapi import FastAPI
from pipeline.intent_extractor import extract_intent
from pipeline.ir_builder import build_ir
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_config
from pipeline.executor import execute_runtime

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Compiler Running"
    }


@app.post("/generate")
def generate(data: dict):

    prompt = data["prompt"]

    intent = extract_intent(prompt)

    ir = build_ir(intent)

    system_design = design_system(ir)

    config = generate_schema(system_design)

    valid, msg = validate_config(config)

    if valid:
        execute_runtime()

    return {
        "intent": intent,
        "ir": ir,
        "system_design": system_design,
        "config": config,
        "validation": msg
    }