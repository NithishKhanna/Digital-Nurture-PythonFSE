import os
from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017/')

db = client['shop']
collection = db['orders']

# Deleting any existing records (D)
collection.delete_many({}) 

# 1. Creating the dataset (C)

print("Inserting the sample data")
sample_data = [
        { "product": "Laptop", "category": "Electronics", "price": 1200, "status": "completed" },
        { "product": "Phone", "category": "Electronics", "price": 800, "status": "completed" },
        { "product": "Shirt", "category": "Apparel", "price": 40, "status": "completed" },
        { "product": "Chair", "category": "Furniture", "price": 150, "status": "pending" }
    ]

insert_result = collection.insert_many(sample_data)
print(f"Successfully inserted {len(insert_result.inserted_ids)} documents.\n\n")

#2 Reading the database (R)

print("Finding all 'completed' documents")
completed_orders = collection.find({"status":"completed"})
for order in completed_orders:
    print(f"     {order['product']} (${order['price']})")

# Modifying the dataset (U)

print("\n[UPDATE] Updating 'Chair' status from 'pending' to 'completed'...")
update_result = collection.update_one(
    { "product": "Chair" }, 
    { "$set": { "status": "completed" } }
)
print(f" Documents matched: {update_result.matched_count}, Modified: {update_result.modified_count}")

result = client['shop']['orders'].aggregate([
    {
        '$match': {
            'status': 'completed'
        }
    }, {
        '$group': {
            '_id': '$category', 
            'totalRevenue': {
                '$sum': '$price'
            }
        }
    }
])

print("Aggregation Pipeline Results")
for doc in result:
    print(f"Category: {doc['_id']} | Total Revenue: ${doc['totalRevenue']}")

client.close()

"""
O/P:
Inserting the sample data
Successfully inserted 4 documents.


Finding all 'completed' documents
     Laptop ($1200)
     Phone ($800)
     Shirt ($40)

[UPDATE] Updating 'Chair' status from 'pending' to 'completed'...
 Documents matched: 1, Modified: 1
Aggregation Pipeline Results
Category: Apparel | Total Revenue: $40
Category: Electronics | Total Revenue: $2000
Category: Furniture | Total Revenue: $150
"""