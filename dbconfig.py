import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pbo2"
)

mycursor = mydb.cursor()

def getEmailPass(email):
    query = 'SELECT email, password, admin FROM users WHERE email = %s'
    mycursor.execute(query, (email, ))

    result = mycursor.fetchone()

    return result

def getName(email):
  query = 'SELECT name FROM users WHERE email = %s'
  mycursor.execute(query, (email,))

  result = mycursor.fetchone()
  
  return result