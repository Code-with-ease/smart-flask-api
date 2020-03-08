from src.DB_helper.DB_fetch import db_fecth
from datetime import date
import logging
# {$and:[{"Transaction.item_id":5613},{cust_id:25}]}
# db.collection.update({"name":"vahid"},{$push:{ "visited": {id:2,'date':'324324',noskhe:['d','n']}}})

cust_id=25
item_id=2564
quantity=2

#TODO
def update_rta(cust_id,item_id,quantity):

def add_to_list(cust_id,item_id,quantity):
    db = db_fecth()
    table = db.read_json("transactions")
    date_now=str(date.today())
    item={
            "date":date_now,
            "quantity":int(quantity)
    }
    table.update_one({"Transaction.item_id":item_id,"cust_id":cust_id},{'$push':{"Transaction.$.item_transactions":item}})

def add_to_list_helper(data):
    for transaction in data["transaction"]:
        try:
            add_to_list(data["cust_id"],transaction["item_id"],transaction["quantity"])
        except Exception as err:
            logging.exception(err)


data={
    "cust_id":25,
    "transaction":[
        {"item_id":2564,"quantity":3},
        {"item_id": 2574, "quantity": 3},
    ]
}
add_to_list_helper(data)