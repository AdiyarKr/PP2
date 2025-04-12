import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database='phonebook',
    user='postgres',
    password='1234',
    port = '5433'
)
current = config.cursor()#Этот инструмент позволяет нам взаимодействовать с данными в базе данных

del_data=input("By what do you want to delete?: ")
del_data1=del_data
del_data=del_data.lower()

temp=input(f'Which {del_data} do you want to delete?: ')

if del_data=='name':
    sql='''
    DELETE FROM phone_number WHERE name = %s RETURNING *
'''
elif del_data=='surname':
    sql='''
    DELETE FROM phone_number WHERE surname = %s RETURNING *
'''
elif del_data=='number_value':
    sql='''
    DELETE FROM phone_number WHERE number_value = %s RETURNING *
'''
else:
    print(f'No row {del_data1}')
    exit()

current.execute(sql, (temp,))
config.commit()
current.close()
config.close()