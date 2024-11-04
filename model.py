import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

def load_data(filename: str) -> pd.DataFrame:
   """
    param:
        filename:str: name of the file to load, must be in the 'Data' folder
    return:
        df:DataFrame in the form of a Pandas DataFrame
   """
    df = pd.read_csv('./Data/'+filename)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
   """

   """


if __name__ == "__main__":
    data = load_data('./Data/hackathon.csv')