import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder

# from sklearn.svm import LinearSVC


def load_data(filename: str) -> pd.DataFrame:
    """
    param:
        filename:str: name of the file to load, must be in the 'Data' folder
    return:
        df: DataFrame in the form of a Pandas DataFrame
    """
    data_path = "./Data/" + filename
    df = pd.read_csv(data_path)
    return df


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    clean data, convert string fields to numeric, remove columns that are not needed,

    Args:
        data (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    # remove columns where the target variable is not null
    data = data.query("vulnerable.notnull()")
    data = data.dropna(axis="columns", how="all")

    boolean_dt = [
        "loan_access",
        "access_to_bank_account",
        "access_to_credit_card",
        "vulnerable",
        "loan_history",
    ]

    # convert TRUE/FALSE dt to numeric
    data[boolean_dt] = data[boolean_dt].astype(int)

    # options are stable/unstable for "income_stability" change to 1 or 0
    data["income_stability"] = data["income_stability"].replace(
        {"Stable": 1, "Unstable": 0}
    )

    # encode categorical data
    categorical_data = ["region", "employment_status"]

    enc = OrdinalEncoder()
    enc.fit(data[categorical_data])
    data[categorical_data] = enc.transform(data[categorical_data])

    return data


if __name__ == "__main__":
    data = load_data("hackathon.csv")
