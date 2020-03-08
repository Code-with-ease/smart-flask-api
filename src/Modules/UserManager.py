from src.DB_helper.DB_fetch import db_fecth
import logging


class UserManager:
    def __init__(self):
        self.db = db_fecth()
        self.table = self.db.read_json("customers")

    def authenticate(self, obj):
        customer = self.table.read_json("customers")
        res = customer.find(obj, {"cust_id": 1, "_id": 0})
        for i in res:
            return i["cust_id"], True

        return None, False

    def check_similar_user(self, username):
        res = self.table.find({"username": username})
        for i in res:
            return True
        return False

    def find_max_cust_id(self):
        agr = [{'$group': {'_id': 'null', 'max': {'$max': '$cust_id'}}}]
        val = list(self.table.aggregate(agr))
        if (len(val) > 0):
            return val[0]['max']
        else:
            return 0

    def add_user(self, obj):
        if self.check_similar_user(obj["username"]):
            return False
        try:
            max_cust = self.find_max_cust_id()
            cust_id = max_cust + 1
            obj["cust_id"] = cust_id
            self.table.insert_one(obj)
            return True
        except Exception as ex:
            logging.exception(ex)


