import creds, MySQLdb








def uploadDrops(stat, ro):
     ro.execute("""SELECT * FROM `drop_log` WHERE `username` in (SELECT Distinct(admin) FROM money_log) ORDER BY `drop_log`.`time` DESC LIMIT 50""")
     result = ro.fetchall()
     
     for ele in result:
         print ele 



def uploadAdmins(stat, ro):
     ro.execute("""SELECT Distinct(admin) FROM money_log ORDER BY admin ASC""")
     result = ro.fetchall()
     
     for ele in result:
          try:
               stat.execute("""INSERT INTO admins (adminName) Values (%s)""", ele[0])
          except:
               pass

if __name__ == "__main__":
     ro=MySQLdb.connect(host=creds.host,user=creds.drinkRoUser,
                       passwd=creds.drinkRoPass,db=creds.drinkRoDb)
     stats=MySQLdb.connect(host=creds.host,user=creds.drinkStatUser,
                       passwd=creds.drinkStatPass,db=creds.drinkStatDb)
     cursRo = ro.cursor()
     cursStat = stats.cursor()
     
     uploadAdmins(cursStat, cursRo)
     uploadDrops(cursStat, cursRo)



