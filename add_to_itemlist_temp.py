from src.DB_helper.DB_fetch import db_fecth

db=db_fecth()
table=db.read_json("itemlist")
for i in range(0,20000):
    name="Item"+" "+str(i)
    table.insert_one({"item_id":i,"item_name":name,"item_category":40})