#initialize db table
from utils import *

conn, cursor = connect_db()

# #drop table if exist
# sql = """
#     DROP TABLE IF EXISTS "Amazon_inventory" CASCADE;
#     DROP TABLE IF EXISTS "Amazon_warehouse" CASCADE;
#     DROP TABLE IF EXISTS "Amazon_product" CASCADE;
# """

# exec_db(sql, conn, cursor)
sql1 = f"""
    TRUNCATE "Amazon_inventory", "Amazon_order", "Amazon_product" CASCADE;
    TRUNCATE TABLE "Amazon_package" RESTART IDENTITY CASCADE;
    TRUNCATE TABLE "Amazon_warehouse" RESTART IDENTITY CASCADE;
"""
exec_db(sql1, conn, cursor)

#initialize table
sql = f"""
    INSERT INTO "Amazon_product" (name, description, price) VALUES
    ('apple', 'sweet', 1),
    ('banana', 'nice', 2),
    ('orange', 'buy', 3),
    ('kiwi', 'love', 4),
    ('cherry', 'try', 5);
"""
exec_db(sql, conn, cursor)

sql2 = f"""
    INSERT INTO "Amazon_warehouse" (wh_x, wh_y) VALUES
    (1, 1),
    (2, 2),
    (3, 3);
"""
exec_db(sql2, conn, cursor)

sql3 = """
    SELECT "Amazon_warehouse".id AS warehouse, "Amazon_product".id AS product 
    FROM "Amazon_warehouse" 
    CROSS JOIN "Amazon_product"
"""
cursor.execute(sql3)
rows = cursor.fetchall()
# Insert into the inventory table where the rows are the warehouse id and product id, and the quantity column is a hardcoded 100
for row in rows:
    sql4 = f"""
        INSERT INTO "Amazon_inventory" (quantity, product_id, warehouse_id) VALUES
        (0, {row[1]}, {row[0]} );
    """
    cursor.execute(sql4)
    
cursor.close()

