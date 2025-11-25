# loader.py

import sqlite3
import pyarrow.parquet as pa

data_path = "data/transactions.parquet"

def import_parquet_into_db():
    connexion = sqlite3.connect("transactions.db")
    cursor = connexion.cursor()

    table = pa.read_table(data_path)
    df= table.to_pandas()

    BD_data = list(df[['id','name','amount']].itertuples(index=False, name=None))
    cursor.executemany(
            "INSERT INTO transactions (id, name, amount) VALUES (?, ?, ?)", 
            BD_data
        )
    
    connexion.commit()
    connexion.close()
    return 0

if __name__ == "__main__":
    import_parquet_into_db()



