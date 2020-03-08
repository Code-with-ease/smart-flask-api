from src.DB_helper.DB_fetch import db_fecth

db=db_fecth()
table=db.read_json("customers")
for i in range(1,61):
    name="test"+str(i)
    email=str(i)+"@gmail.com"
    table.insert_one({"cust_id":int(i),"email":email,"username":name,"password":name})