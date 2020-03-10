import sqlite3

con = sqlite3.connect('mycompany.db')
cursor_object = con.cursor()

cursor_object.execute("CREATE TABLE IF NOT  EXISTS employe(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)")
con.commit()

def insert_value(id,name,salary,department,position):
    cursor_object.execute("INSERT INTO employe VALUES(?,?,?,?,?)",(id,name,salary,department,position))
    con.commit()
    
def update_department(id,department):
    cursor_object.execute("UPDATE INTO employe VALUES(?,?)",(id,department))
    con.commit()

def sql_fetch():
    cursor_object.execute("SELECT * FROM employe")
    a = cursor_object.fetchall()
    for i in a:
        print(i)
        
def delete_all():
    cursor_object.execute("DELETE FROM employe")
    con.commit()
    
    
insert_value(1,'AQIB',80000,'Python','Developer')
                      
cursor_object.close()
con.close()
