import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database='phonebook',
    user='postgres',
    password='1234',
    port='5433'
)
def adding(id, username, surname, number):
    current = config.cursor()#Этот инструмент позволяет нам взаимодействовать с данными в базе данных


    sql = '''
        INSERT INTO phone_number
        VALUES (%s, %s, %s, %s);
    '''
    current.execute(sql, (id, username, surname, number))#для заполнения(өзгерту)
    current.close()#завершает базы данных сеанс работы
    config.commit()#сохранить изменения, для подтверждения этих изменений
    config.close()#освободить ресурсы и завершить соединение
# вставляем данные в телефонную книгу вводя их с консоли

print("ID:")
id = int(input())
print("Name:")
username = input()
print('Surname:')
surname=input()
print("Phone number:")
number = input()

adding(id, username, surname, number)