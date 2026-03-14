import requests

def generate_ai_report(issues):

    report = f"""
AI Data Quality Report

Issues detected in dataset:
{issues}

Suggested Fix:
1. Fill missing values
2. Remove duplicates
3. Investigate outliers
"""

    return report