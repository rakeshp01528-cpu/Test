import duckdb
import pandas as pd

# Create an in-memory DuckDB database
con = duckdb.connect(database=':memory:')

# Create a table
con.execute("CREATE TABLE users (id INTEGER, name VARCHAR)")

# Insert sample data
con.execute("INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")

# Query the data
result = con.execute("SELECT * FROM users ORDER BY id").fetchall()
print(result)
df=pd.DataFrame(result, columns=['id', 'name'])
print(df)

# Close connection
con.close()



