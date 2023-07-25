
def  database(command,getoutput=False):
    import mysql.connector
    con=mysql.connector.connect(host="localhost",user="root",password="pass",database="sarathi" )
    cur=con.cursor(buffered=True)
    cur.execute(command)
    con.commit()
    if getoutput==True:
        output=cur.fetchall()
        con.close()
        return output
    else:
        con.close()
