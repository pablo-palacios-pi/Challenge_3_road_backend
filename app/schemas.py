from pydantic import BaseModel
from typing import Optional


" CLASES "
class Item_Create(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: Optional[str] 
    skin_color: Optional[str] 
    eye_color: Optional[str] 


class Item_(Item_Create):
    id: int




" CONEXION BASE DATOS NO RELACIONAL"
#redis_db = redis.Redis(host="localhost",port=6379,db=0, decode_responses=True)


"""" CONEXION CON LIBRERIA SINCRONICA """

import pymysql
try:
    conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="test"
        )
    cursor = conn.cursor()
except Exception as e:
    raise Exception(F"ERROR CONEXION BASEDATOS: {e}")




""" CONEXION CON LIBRERIA ASINCRONICA """
# import aiomysql
# import asyncio


# try:
#     conn = aiomysql.connect(
#         host="127.0.0.1",
#         user="root",
#         password="",
#         db="test"
#     )

#     cursor = conn.cursor()

# except Exception as e:
#     raise BaseException(e)








