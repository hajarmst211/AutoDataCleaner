from cleaner import main_cleaner
import pandas as pd
def main():
    test_df = pd.DataFrame({
        "name": [" Alice ", "Bob", "Alice ", None, "Charlie"],
        "age": ["23", "30", None, "30", "23"],
        "amount": ["100.5", None, "100.5", "100.5", None],
        "date_str": ["2024-01-01", "notadate", None, "2022-05-05", "2024-01-01"],
        "extra_nulls": [None, None, None, None, None]  # column likely to be dropped
    })
    
    print("==== RAW DATAFRAME ====")
    print(test_df.info())


    cleaned = main_cleaner("sample_test.csv")
    print(cleaned.info())

    print("\n==== CLEANED DATAFRAME ====")
    print(cleaned)