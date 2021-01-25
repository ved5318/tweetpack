import mysql.connector
from st2common.runners.base_action import Action

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="practice"
)
class insertdb(Action):

    def run(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO Info (e_name, e_id, e_add) VALUES (%s, %s, %s)"
        val = ("ved", 2, "Newtown")
        mycursor.execute(sql, val)
        mydb.commit()
        return True