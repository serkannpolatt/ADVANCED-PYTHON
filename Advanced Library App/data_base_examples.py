from audioop import add
import sqlite3 as sql
from turtle import textinput





# def insert(name,lastname,age):
#     conn=sql.connect("ders.db")
#     cursor=conn.cursor()

#     ad_command="""INSERT INTO USERS VALUES {} """
#     data=(name,lastname,age)

#     cursor.execute(ad_command.format(data))
#     conn.commit()
#     conn.close()

# insert("batuhan","kemik",31)




conn=sql.connect("ders.db")
cursor=conn.cursor()
 
cursor.execute("UPDATE USERS SET lastname='SERKAN' WHERE name = 'mahmut' ")
print("başarılı")

conn.commit()
conn.close()




# conn=sql.connect("ders.db")
# cursor=conn.cursor()

# cursor.execute("DELETE from STUDENTS WHERE lastname='polat'")
# print("silme başarılı")

# conn.commit()
# conn.close()


# def delete_age(age):
#     conn=sql.connect('ders.db')
#     cursor=conn.cursor

#     delete_command="DELETE from STUDENTS WHERE age ={}"
#     conn.commit()
#     conn.close()
# delete_age(31)


# conn=sql.connect("ders.db")
# cursor=conn.cursor()

# cursor.execute("SELECT name,lastname from STUDENTS")
# list_all=cursor.fetchall() 
# for student in list_all:
#     print(student)

# conn.commit()
# conn.close()


# 




# conn= sql.connect("ders.db")
# cursor=conn.cursor()

# cursor.execute("""CREATE TABLE CALISANLAR(
# id integer PRIMARY KEY,
# ad text,
# soyad text,
# maas integer ) """ )

# conn.commit()
# conn.close()



# conn =sql.connect("ders.db")
# cursor=conn.cursor()

# datas = [("ahmet","yılmaz",3100),("memoli","önel",2300),
# ("serkan","polat",36000),("barış","yörük",10000)]

# add_command="INSERT INTO CALISANLAR (ad,soyad,maas) VALUES (?,?,?)"

# cursor.executemany(add_command,datas)
# print("başarılı")

# conn.commit()
# conn.close()




# conn =sql.connect("ders.db")
# cursor=conn.cursor()

# cursor.execute("SELECT * from CALISANLAR")
# list_all=cursor.fetchall()

# for calisan in list_all:
#     print(calisan)

# conn.commit()
# conn.close()

# conn =sql.connect("ders.db")
# cursor=conn.cursor()

# cursor.execute("SELECT * from sqlite_master WHERE type='table'")
# tables=cursor.fetchall()

# for table in tables:
#     print(table)


# conn.commit()
# conn.close()


# def create_table():
#     conn=sql.connect("ders.db")
#     cursor = conn.cursor()

#     cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
#     id integer PRIMARY KEY,
#     name text,
#     lastname text,
#     username text,
#     password text
#     )""")

#     conn.commit()
#     conn.close()

# def insert(name,lastname,username,password):
#     conn=sql.connect("ders.db")
#     cursor=conn.cursor()

#     add_command = """INSERT INTO USERS(name, lastname , username , password) VALUES {} """
#     data =(name,lastname,username,password)
    
#     cursor.execute(add_command.format(data))

#     conn.commit()
#     conn.close()

# def print_all():
#     conn=sql.connect("ders.db")
#     cursor=conn.cursor()

#     cursor.execute("SELECT * from USERS")
#     list_all=cursor.fetchall()

#     conn.close()

# def search_username(username):
#     conn=sql.connect("ders.db")
#     cursor=conn.cursor()
    
#     search_command="SELECT * from USERS WHERE username ='{}'"
#     cursor.execute(search_command.format(username))
    
#     user=cursor.fetchone()

#     conn.close()
#     return user



# def update_paswword(username,newPassword):
#     conn=sql.connect("ders.db")
#     cursor=conn.cursor()

#     upd_command ="UPDATE USERS SET password='{}' WHERE username ='{}'"
#     cursor.execute(upd_command.format(newPassword,username))

#     conn.commit()
#     conn.close()

# def delete_acoount(username):
#     conn=sql.connect("ders.db")
#     cursor=conn.cursor()

#     dlt_command="DELETE from USERS WHERE username = '{}'"
#     cursor.execute(dlt_command.format(username))

#     conn.commit()
#     conn.close()

# def delete_table():
#     conn=sql.connect("ders.db")
#     cursor=conn.cursor()
    
#     cursor.execute("DROP TABLE USERS")
#     conn.commit()