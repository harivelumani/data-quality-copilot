from fastapi import FastAPI
from backend.profiler import profile_data
from backend.anomaly_detector import detect_issues
from backend.ai_agent import generate_ai_report

app = FastAPI()

DATASET = "datasets/sales.csv"

@app.get("/analyze")

def analyze():

    profile = profile_data(DATASET)
    issues = detect_issues(DATASET)

    report = generate_ai_report(issues)

    return {
        "profile": profile,
        "issues": issues,
        "ai_report": report
    }