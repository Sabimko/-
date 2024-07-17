import sqlite3

connect = sqlite3.connect("kurs.db")
cursor = connect.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS kurs(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name VARCHAR (30) NOT NULL,
                    age INT DEFAULT NULL, 
                    direction VARCHAR (30) NOT NULL,
                    is_activ BOOLEAN NOT NULL DEFAULT FALSE
                )""")

def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    direction = input("Введите направление: ")
    is_activ = bool(input("Вы  раньше учились в курсе?: "))
    print("Успешно зарегистрированы!")
    
    
    cursor.execute(f"""INSERT INTO  kurs
                   (full_name,  age, direction, is_activ)
                   VALUES ('{full_name}',  '{age}',  '{direction}', '{is_activ}')""")
    
    connect.commit()
    
def all_studets():
    cursor.execute("SELECT * FROM kurs")
    student = cursor.fetchall()
    print(student)
    
register()