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

<<<<<<< HEAD
def readDataBuku():
    mycursor.execute("SELECT * FROM buku")
    result = mycursor.fetchall()
    return result       
=======
def getName(email):
  query = 'SELECT name FROM users WHERE email = %s'
  mycursor.execute(query, (email,))

  result = mycursor.fetchone()
  
  return result

def getAllBook():
  query = 'SELECT * FROM buku'
  mycursor.execute(query)

  result = mycursor.fetchall()

  return result
>>>>>>> 86daa3f8d72db01fc1ce4d303c52ab285d4ed157
