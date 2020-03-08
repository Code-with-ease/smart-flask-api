from src.DB_helper.DB_fetch import db_fecth

class fetch_details():
    def __init__(self):
        self.db=db_fecth()
        self.table_names=self.db.read_json("itemlist")
        self.table_category=self.db.read_json("category")
        
    def fetch_item_details(self,arr):
        res=self.table_names.find({"item_id":{"$in":arr}})
        item_list=[]
        for i in res:
            item_obj={}
            item_obj["itemid"]=int(i["item_id"])
            item_obj["item_name"]=str(i["item_name"])
            item_obj["item_category"] = str(i["item_category"])
            item_list.append(item_obj)
        return(item_list)




