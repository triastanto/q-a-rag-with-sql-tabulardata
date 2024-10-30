from langchain_community.utilities.sql_database import SQLDatabase
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Employee LIMIT 10;")