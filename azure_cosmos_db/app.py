import pandas as pd 
import json
import psycopg2


print('Imported packages successfully.')

try:
    conn_string="host=c.demo-cosmos-db-204.postgres.database.azure.com port=5432 dbname=citus user=citus password=cosmos@123 sslmode=require"
    conn = psycopg2.connect(conn_string)
except Exception as exp:
    print(exp)

print("successfully connected")

cursor = conn.cursor()

cursor.execute("Drop table if exists countries")

# Download and read csv file
df = pd.read_csv('https://globaldatalab.org/assets/2019/09/SHDI%20Complete%203.0.csv',encoding='ISO-8859–1',dtype='str')
df = df.reset_index()
df = df.rename(columns={'index':'id'})
df['id'] = df['id'].astype(str)

#create statement for ccountries table
sql_text = pd.io.sql.get_schema(df, "countries")   
print(sql_text)

#create table in the database
cursor.execute(sql_text)

res=cursor.execute("SELECT table_name, column_name, data_type FROM information_schema.columns")
print(res)

# #insert data into posgres table
# for index, row in df.iterrows():       
#     insert_query = 'INSERT INTO countries ('+ str(', '.join(df.columns))+ ') VALUES '+ str(tuple(row.values))
#     print(insert_query)
#     cursor.execute(insert_query)     

#Fetch all rows from table
cursor.execute("Select * from countries where country like 'india%';")
rows = cursor.fetchall()
print("Table data")
for row in rows:
    print(row)
print('Records inserted successfully.')