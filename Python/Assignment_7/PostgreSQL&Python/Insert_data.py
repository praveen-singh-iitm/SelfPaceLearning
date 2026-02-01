import psycopg2

def table():
    try:
        conn=psycopg2.connect(
            dbname="student",
            user="postgres",
            password="postgres",
            port="5432",
            host="localhost"
        )
        cur=conn.cursor()
        cur.execute('''create table students1(roll_no int, name text, age int);''')
        conn.commit()
        print("Table created")
    except psycopg2.Error as e:
        print(f"Database Error:{e}")
    finally:
        cur.close()
        conn.close()

def data():
    #inserting data one by one
    try:
        conn=psycopg2.connect(
            dbname="student",
            user="postgres",
            password="postgres",
            port="5432",
            host="localhost"
        )
        cur=conn.cursor()
        query='''insert into students1 (roll_no, name, age) values(%s,%s,%s)'''
        cur.execute(query,(211,'Rakesh',42))
        cur.execute(query,(21,'Suresh',31))
        cur.execute(query,(11,'Ramesh',26))
        cur.execute(query,(13,'Danny',21))
        conn.commit()
        print("Data Inserted")
    except psycopg2.Error as e:
        print(f"Database Error:{e}")
    finally:
        cur.close()
        conn.close()

def data_by_user():
    #inserting data one by one
    try:
        uname=input("Please enter your name : ")
        uage=input("Please enter your age : ")
        uroll=input("Please enter your roll no : ")
        conn=psycopg2.connect(
            dbname="student",
            user="postgres",
            password="postgres",
            port="5432",
            host="localhost"
        )
        cur=conn.cursor()
        query='''insert into students1 (roll_no, name, age) values(%s,%s,%s)'''
        cur.execute(query,(uroll,uname,uage))
        conn.commit()
        print("Data Inserted")
    except psycopg2.Error as e:
        print(f"Database Error:{e}")
    finally:
        cur.close()
        conn.close()

def data_many():
    #inserting multiple data
    try:
        conn=psycopg2.connect(
            dbname="student",
            user="postgres",
            password="postgres",
            port="5432",
            host="localhost"
        )
        cur=conn.cursor()
        query='''insert into students1 (roll_no, name, age) values(%s,%s,%s)'''
        cur.executemany(query,[(211,'Rakesh',42),(21,'Suresh',31),(11,'Ramesh',26),(13,'Danny',21)])
        conn.commit()
        print("Data Inserted")
    except psycopg2.Error as e:
        print(f"Database Error:{e}")
    finally:
        cur.close()
        conn.close()

def data_fetch():
    try:
        conn=psycopg2.connect(
            dbname="student",
            user="postgres",
            password="postgres",
            port="5432",
            host="localhost"
        )
        cur=conn.cursor()
        query='''select * from students1;'''
        cur.execute(query)
        rows=cur.fetchall()
        for row in rows:
            print(row[0],row[1],row[2])
    except psycopg2.Error as e:
        print(f"Database Error:{e}")
    finally:
        cur.close()
        conn.close()

if __name__=="__main__":
    # data_fetch()
    data_by_user()

