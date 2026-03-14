import pandas as pd

def profile_data(file_path):

    df = pd.read_csv(file_path)

    profile = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_values": {k: int(v) for k, v in df.isnull().sum().to_dict().items()},
        "duplicates": int(df.duplicated().sum())
    }

    return profile