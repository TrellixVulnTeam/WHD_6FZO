import sqlite3
from os import path
import random
import string
import threading
import load_model

userpath = path.join("users")
datapatg= path.join("data")

class databse(object):
    def __init__(self,data):
        self.data=data
        self.connection = sqlite3.connect(path.join(userpath,"Database.sqlite"))
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS users (ID TEXT, NAME TEXT, FDN TEXT,SEX TEXT, H INTERGER) ")
    
    def create(self):
        # FC= Frecuencia cardiaca, FR=Frecuencia respiratoria,SO=Saturacion de oxigeno
        # MO=Masa osea, MM=Masa muscular, 
        create="CREATE TABLE IF NOT EXISTS"
        self.cursor.execute(f"INSERT INTO users (ID,NAME,FDN,SEX,H) VALUES (?,?,?,?,?)", (self.data[0],self.data[1],self.data[2],self.data[3],self.data[5]))
        self.cursor.execute(f"{create} data_daily_{self.data[0]} (DATE TEXT, FC INTEGER, FR INTEGER, SO INTEGER)")
        self.cursor.execute(f"{create} data_week_{self.data[0]} (DATE TEXT, MO INTEGER, MM INTERGER, FAT INTERGER, MASS INTERGER)")
        self.connection.commit()
    
    def find(self):
        self.cursor.execute(f"SELECT ID,FDN,SEX,H FROM users WHERE name= '%s' "%self.data[-1])
        return self.cursor.fetchall()[0]

    def insert_daily(self):
        self.cursor.execute(f"SELECT ID FROM users WHERE name= '%s' "%self.data[-1])
        self.cursor.execute(f"INSERT INTO data_daily_{self.cursor.fetchone()[0]} (DATE, FC, FR, SO) VALUES (?,?,?,?)",(self.data[0],self.data[1],self.data[2],self.data[3]))
        self.connection.commit()

    def insert_week(self):
        self.cursor.execute(f"INSERT INTO data_week_{self.data[-1]} (DATE, MO, MM, FAT, MASS) VALUES (?,?,?,?,?)",(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4]))
        self.connection.commit()

    def data_all(self):
        print(self.data)
        self.cursor.execute(f"SELECT ID FROM users WHERE name= '%s'" %self.data[0])
        idx=None
        for idx in self.cursor.fetchone():
            if idx==None:
                pass
            else:
                idx=idx
                self.cursor.execute(f"SELECT FC,FR FROM data_daily_{idx} WHERE  SO=0")
                daily=self.cursor.fetchall()
                self.cursor.execute(f"SELECT MO ,MM,FAT,MASS FROM data_week_{idx} LAST_VALUE")
                week=self.cursor.fetchone()
                return daily,week

if path.exists(path.join(userpath,"Database.sqlite")):
    pass
else:
    with open(path.join(userpath,'Database.sqlite'), 'w') as fp: 
        pass


def datos(nombre,fdn,sexo,peso,altura):
    id_key= ''.join([random.choice(string.ascii_letters) for n in range(8)]) 
    data=[id_key,nombre,fdn,sexo,peso,altura]
    crear=databse(data)
    crear.create()

def daily(data):
    for lista in data:
        insertar=databse(lista)
        insertar.insert_daily()

def get_data(data):
    getinfo=databse(data)
    return getinfo.find()

def week(data):
    insertar=databse(data)
    insertar.insert_week()

def data(nombre):
    datai=[nombre,0]
    data=databse(datai)
    daily,week= data.data_all()
    print(daily,week)
    # calidad =load_model.main(daily)
    # sueno=f"Weekly sleep quality: {calidad[0]}"
    # MO=f"Bone mass: {week[0]} Kg"
    # MM=f"Muscle mass: {week[1]} Kg"
    # FAT=f"Fat: {week[2]} Kg"
    # MASS=f"Mass: {week[3]} Kg"
    # data=f"{sueno}%\n{MO}\n{MM}\n{FAT}\n{MASS}"
    return data