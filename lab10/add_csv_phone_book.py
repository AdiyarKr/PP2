import psycopg2, csv

config = psycopg2.connect(
    host = 'localhost',
    database='phonebook',
    user='postgres',
    password='1234',
    port = '5433'
)
def csv_add(name_csv):
    currnet=config.cursor()
    arr=[]

    with open (name_csv) as f:
        f_read=csv.reader(f, delimiter=',')
        
        for row in f_read:
            row[0]=int(row[0].strip(','))#бірінші тұрғандарды санға айналдырамыз
            arr.append(row)#массиқа қосамыз

    sql = '''
            INSERT INTO phone_number VALUES(%s, %s, %s, %s) RETURNING *;
    '''
    for i in arr:  
        currnet.execute(sql, i)

    #final = currnet.fetchall()
    #print(final)

    currnet.close()#завершает базы данных сеанс работы
    config.commit()#сохранить изменения, для подтверждения этих изменени
    config.close()#освободить ресурсы и завершить соединение

csv_add('info_phone.csv')