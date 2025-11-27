# data_generator.py

from faker import Faker
import random
import pandas as pd
from config.extract_statics import get_statics

data_path = get_statics("paths")["generated_data"]

def generate_data():
    fake = Faker()
    rows = []
    for id in range(10000):
        data_to_save = {}
        noise = random.uniform(-500 , 500)
        random_amount = random.randint(100, 2_000_000) 
        rows.append({
            "id" : id,
            "name" : fake.name(),
            "amount" : random_amount + noise
        })
    df = pd.DataFrame(rows)
    df.to_parquet(data_path)
    
    return 0
        
if __name__ == "__main__":
    generate_data()
        