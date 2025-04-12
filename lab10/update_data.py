import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database='phonebook',
    user='postgres',
    password='1234',
    port = '5433'
)
def update_table():
    current = config.cursor()
    #updating data in table 
    user_id = int(input("Enter ID: "))
    change = input("What do you want to change?: ")
    change = change.lower()#кіші әріпке ауыстырамыз
    data = input(f'To what value set the {change}?: ')

    if change == 'name':
        sql = '''
            UPDATE phone_number SET name = %s WHERE phone_number_id = %s;
        '''
    elif change == 'number':
        sql = '''
            UPDATE phone_number SET number_value = %s WHERE phone_number_id = %s;
        '''
    elif change == 'surname':
        sql = '''
            UPDATE phone_number SET surname = %s WHERE phone_number_id = %s;
        '''
    else:
        print(f'No row {change}')
        exit()

    current.execute(sql, (data, user_id))
    config.commit()
    current.close()
    config.close()

update_table()