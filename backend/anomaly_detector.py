import pandas as pd

def detect_issues(file_path):

    df = pd.read_csv(file_path)

    issues = []

    # Missing values
    missing = df.isnull().sum()

    for col, count in missing.items():
        if count > 0:
            issues.append(f"Missing values in column {col}: {count}")

    # duplicates
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        issues.append(f"Duplicate rows detected: {duplicates}")

    # Outliers
    for col in df.select_dtypes(include=['int64','float64']):
        if df[col].max() > df[col].mean() * 5:
            issues.append(f"Possible outlier detected in column {col}")

    return issues