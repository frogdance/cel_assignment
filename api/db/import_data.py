
# # import dependancies
import psycopg2
import psycopg2.extras as extras
import pandas as pd
import os

# # database connection
conn = psycopg2.connect(database=os.getenv('POSTGRES_DB'), user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'), host=os.getenv('HOST'), port = "5432")
cur = conn.cursor()

if 'item' and 'outlet' and 'sale_report' not in list(pd.read_sql("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""", con=conn).index):
# ## import data function
    def execute_values(conn, df, table):
    
        tuples = [tuple(x) for x in df.to_numpy()]
    
        cols = ','.join(list(df.columns))
    
        # SQL query to execute
        query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
        cursor = conn.cursor()
        try:
            extras.execute_values(cursor, query, tuples)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            conn.rollback()
            cursor.close()
            return 1
        print("execute_values() done")
        cursor.close()

    # # load data
    df = pd.read_csv('https://s3.amazonaws.com/coderbyteprojectattachments/simcel-6pk70-1jk5iqdp-train_v9rqX0R.csv')
    # # process data

    item = df[['Item_Identifier', 'Item_Weight', 'Item_Fat_Content', 'Item_Type']]
    item = item.sort_values(by=['Item_Identifier', 'Item_Weight'], ascending=True)
    item.ffill(inplace=True)
    # item['Item_Fat_Content'].unique()
    # item['Item_Type'].unique()
    item['Item_Fat_Content'] = item['Item_Fat_Content'].replace('LF', 'Low Fat').replace('low fat', 'Low Fat').replace('reg', 'Regular')
    item.drop_duplicates(inplace=True)

    outlet = df[['Outlet_Identifier', 'Outlet_Establishment_Year', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']]
    outlet.drop_duplicates(inplace=True)

    sale_report = df[['Item_Identifier', 'Outlet_Identifier', 'Item_Visibility', 'Item_MRP', 'Item_Outlet_Sales']]

    # # create tables and import data to database
    # ## item table

    sql = """
    CREATE TABLE item (
        item_identifier CHAR(5) PRIMARY KEY,
        item_weight REAL,
        item_fat_content VARCHAR(10),
        item_type VARCHAR(30)
    );
    """
    cur.execute(sql)

    execute_values(conn, item, 'item')

    # ## store table

    sql = """
    CREATE TABLE outlet (
        outlet_identifier CHAR(6) PRIMARY KEY,
        outlet_establishment_year SMALLINT,
        outlet_size VARCHAR(10),
        outlet_location_Type CHAR(6),
        outlet_type VARCHAR(20)
    );
    """
    cur.execute(sql)

    execute_values(conn, outlet, 'outlet')

    # ## sale_report table

    sql = """
    CREATE TABLE sale_report (
        id SERIAL PRIMARY KEY,
        item_identifier CHAR(5) REFERENCES item(Item_Identifier),
        outlet_identifier CHAR(6) REFERENCES outlet(Outlet_Identifier),
        item_visibility REAL,
        item_mrp REAL,
        item_outlet_sales REAL
    );
    """
    cur.execute(sql)

    sale_report['id'] = sale_report.index
    execute_values(conn, sale_report, 'sale_report')