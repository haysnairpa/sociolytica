from sqlalchemy import create_engine

# Test connection
DATABASE_URL = "mysql+pymysql://root@localhost:3306/sociolytica?charset=utf8mb4"
engine = create_engine(DATABASE_URL)

try:
    # Try to connect
    with engine.connect() as connection:
        print("Successfully connected to database!")
except Exception as e:
    print(f"Error connecting to database: {str(e)}")
