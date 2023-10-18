import sqlite3
conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
c=conn.cursor()
c.execute('''CREATE TABLE coffee (id integer PRIMARY KEY AUTOINCREMENT,
          list varchar (30) not null,
          price varchar (30) not null)''',)
conn.commit
c.execute('''CREATE TABLE shot (id integer PRIMARY KEY AUTOINCREMENT,
          list varchar (30) not null,
          price varchar (30) not null)''',)
conn.commit
c.execute('''CREATE TABLE size (id integer PRIMARY KEY AUTOINCREMENT,
          list varchar (30) not null,
          price varchar (30) not null)''',)
conn.commit
c.execute('''CREATE TABLE type (id integer PRIMARY KEY AUTOINCREMENT,
          list varchar (30) not null,
          price varchar (30) not null)''',)
conn.commit
c.execute('''CREATE TABLE sweetness (id integer PRIMARY KEY AUTOINCREMENT,
          list varchar (30) not null,
          price varchar (30) not null)''',)
conn.commit
c.execute('''CREATE TABLE user_id (id integer PRIMARY KEY AUTOINCREMENT,
          name varchar (30) not null,
          number INT (10) not null)''',)
conn.commit
c.execute('''CREATE TABLE "Order" (id INTEGER PRIMARY KEY AUTOINCREMENT,
    coffee VARCHAR(30) NOT NULL,
    shot VARCHAR(30) NOT NULL,
    type VARCHAR(30) NOT NULL,
    size VARCHAR(30) NOT NULL,
    price VARCHAR(30) NOT NULL)''')
conn.commit 

c.execute('''CREATE TABLE "allOrder" (id INTEGER PRIMARY KEY AUTOINCREMENT,
    userid VARCHAR(30) NOT NULL,
    coffee VARCHAR(30) NOT NULL,
    shot VARCHAR(30) NOT NULL,
    type VARCHAR(30) NOT NULL,
    size VARCHAR(30) NOT NULL,
    price VARCHAR(30) NOT NULL)''')
conn.commit 
conn.close