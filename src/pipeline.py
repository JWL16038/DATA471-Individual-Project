
from clean import clean_dataset
from data import load_data, save_data
from preprocessor import split_dataframe


def run():
    df = load_data()
    df = clean_dataset(df)
    save_data(df)
    X_train, X_test, y_train, y_test = split_dataframe(df) 


if __name__ == "__main__":
    run()
