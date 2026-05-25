

from sqlalchemy import create_engine, text

DB_USER = "rashid"
DB_PASSWORD = "rashid123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "salesdb"

connection_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(connection_url)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("Database connection successful.")
        print(result.fetchone()[0])
except Exception as e:
    print("Database connection failed.")
    print(e)