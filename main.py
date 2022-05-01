from xml.etree.ElementPath import prepare_descendant
from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'], port='9042')
session = cluster.connect("store")

# READ SIMPLE
print("Reading data simply!")
rows = session.execute("select * from store.shopping_cart;")
for row in rows:
    print(row)

# READ PERFORMANT
print("Read data performant!")
prepared_statement = session.prepare(
    "select * from store.shopping_cart where userid = ?")
ids_to_lookup = ['1234', '9876']

for ids in ids_to_lookup:
    row = session.execute(prepared_statement, [ids]).one()
    print(row)

# WRITE SYNC
print("Writing Synchronously!")

# session.execute(
#     "INSERT INTO store.shopping_cart (userid, item_count, last_update_timestamp) VALUES ('5678', 10, toTimeStamp(now()))")

session.shutdown()

session = cluster.connect("store")
# WRITE ASYNC
print("Writing Asynchronously!")
future = session.execute_async(
    "INSERT INTO store.shopping_cart (userid, item_count, last_update_timestamp) VALUES ('9750', 19, toTimeStamp(now()));")
print(future)

session.shutdown()
