import pymysql 

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='DariaBu2002!',                             
                             db='list',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    cursor.execute('show tables')
    print(cursor.fetchall())

with connection.cursor() as cursor:
    cursor.execute('desc tenants')
    print(cursor.fetchall())

with connection.cursor() as cursor:
    cursor.execute('select * from tenants;')
    print(cursor.fetchall())
    
with connection.cursor() as cursor:
    cursor.execute('''insert into tenants (`apartment number`,`Surname`,`Name`,`Second name`,`Payment`) values ('313','Никитина','Александра','Никитична','1730');''')
    cursor.execute('''insert into tenants (`apartment number`,`Surname`,`Name`,`Second name`,`Payment`) values ('270','Одинцов','Андрей','Никитич','1530');''')
    connection.commit()
    print(cursor.fetchall())

with connection.cursor() as cursor:
    cursor.execute('''update tenants set `Surname` = 'Федотова', `Name` = 'Диана', `Second name` = 'Дмитриевна',`Payment` = '2400' where (`apartment number`= '124') and (`Surname` = '1') and (`Name` = '1') and (`Second name` = '1') and (`Payment` = '1');''')
    connection.commit()
    print(cursor.fetchall())

with connection.cursor() as cursor:
    cursor.execute('select * from tenants;')
    print(cursor.fetchall())

connection.close()
