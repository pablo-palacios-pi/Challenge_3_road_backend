# VIEWS

from faker import Faker
from schemas import Item_, cursor



faker = Faker()

async def add_item_new(name: str, height: int, mass: int, hair_color: str, skin_color: str, eye_color: str):
    
    uuid = faker.random_number(digits=2)
    
    cursor.execute("""INSERT INTO test.table_items (ids,name,height,mass,hair_color,skin_color,eye_color)
                   VALUES (%s,%s,%s,%s,%s,%s,%s)""",(uuid,name,height,mass,hair_color,skin_color,eye_color))
    
    cursor.connection.commit()


    item = Item_(id=uuid,
                 name=name,
                 height=height,
                 mass=mass,
                 hair_color=hair_color,
                 skin_color=skin_color,
                 eye_color=eye_color)    
    
    return item


async def get_all_items():
    cursor.execute("""SELECT * FROM test.table_items""")
    gets = cursor.fetchall()
    data = []
    for g in gets:
        item = {
            "id":g[0],
            "name":g[1],
            "height":g[2],
            "mass":g[3],
            "hair_color":g[4],
            "skin_color":g[5],
            "eye_color":g[6]
        }
        data.append(item)

    return data

async def get_item_name(name: str):
    cursor.execute("""SELECT * FROM test.table_items 
                   WHERE name = (%s)""",(name))
    gets_ = cursor.fetchone()
    match gets_:
        case None:
            item = None
        case _:
            item = {
                    "id":gets_[0],
                    "name":gets_[1],
                    "height":gets_[2],
                    "mass":gets_[3],
                    "hair_color":gets_[4],
                    "skin_color":gets_[5],
                    "eye_color":gets_[6]
                }
    
    return item


async def delete_item_id(id: int):
    resp = False
    cursor.execute("""SELECT ids FROM test.table_items 
                   WHERE ids = (%s)""",(id))
    
    gets_id = cursor.fetchone()

    if gets_id is not None:
        cursor.execute("DELETE FROM test.table_items WHERE ids = %s",(id,))
        cursor.connection.commit()
        resp = True

    return resp





