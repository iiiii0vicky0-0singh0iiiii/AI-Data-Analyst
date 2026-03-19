from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)

def run_query(sql):
    try:
        df = pd.read_sql(sql, engine)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}