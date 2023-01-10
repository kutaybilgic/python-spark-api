import json
from uuid import UUID

# filename = 'productdb.json'


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


def read_json(db):
    with open(db, 'r', encoding="utf-8") as f:
        return json.load(f)


# add new product to productDb.json file
def write_json(db, data):
    with open(db, 'r+', encoding="utf-8") as f:
        temp = json.load(f)
        print(data.__dict__)
        temp.append(data.__dict__)
        f.seek(0)
        json.dump(temp, f, cls=UUIDEncoder)
        f.truncate()

    # with open(filename, 'w') as f:
    #     json.dump(data.__dict__, f, cls=UUIDEncoder)

def find_movie(db, productName):
    print("Kutay")
    productDb = read_json(db)
    for product in productDb:
        if product['Series_Title'] == productName:
            return product
    return None
