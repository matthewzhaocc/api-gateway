import mysql.connector

db = mysql.connector.connect(
    host = '<insert ip address of the mysql server>',
    user='<insert username>',
    passwd='<insert db password>',
    database='<insert db name>'
)

def new_user(name, apikey):    
    cursor = db.cursor()
    template = 'insert into apikeys (apikey, name) values (%s,%s)'
    value = (apikey, name)
    cursor.execute(template, value)
    db.commit()

def check_user(apikey):
    cursor = db.cursor()
    template = 'select name from apikeys where apikey = %s;'
    val = (apikey,)
    cursor.execute(template, val)
    result = cursor.fetchall()
    if result:
        return result[0][0]
    else:
        return None

