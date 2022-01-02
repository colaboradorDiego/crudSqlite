import sqlite3
import subprocess as sp

"""
database code
"""
dbFilePath = "trader.sqlite"


def create_table():
    conn = sqlite3.connect(dbFilePath)

    cursor = conn.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS securities(
            id INTEGER PRIMARY KEY,
            symbol varchar(50),
            securityType varchar(10),
            securitySubType varchar(10)
        )'''

    cursor.execute(query)

    conn.commit()
    conn.close()


def add_security(symbol, securitySubType, securityType):
    conn = sqlite3.connect(dbFilePath)

    cursor = conn.cursor()

    query = '''
        INSERT INTO securities(symbol, securitySubType, securityType)
            VALUES ( ?,?,? )'''

    cursor.execute(query, (symbol, securitySubType, securityType))

    conn.commit()
    conn.close()


def get_securities():
    conn = sqlite3.connect(dbFilePath)

    cursor = conn.cursor()

    query = '''
        SELECT symbol, securitySubType, securityType
        FROM securities'''

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


def get_security_by_symbol(symbol):
    conn = sqlite3.connect(dbFilePath)

    cursor = conn.cursor()

    cursor.execute("SELECT *  FROM securities WHERE symbol=?", (symbol,))
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


def update_especie(symbol, securityType, securitySubType):
    conn = sqlite3.connect(dbFilePath)

    cursor = conn.cursor()

    query = '''
        UPDATE securities
        SET symbol = ?, securityType = ?, securitySubType = ?
        WHERE symbol = ?'''

    cursor.execute(query, (symbol, securityType, securitySubType, symbol))

    conn.commit()
    conn.close()


def delete_especie(especie):
    conn = sqlite3.connect(dbFilePath)

    cursor = conn.cursor()

    query = '''
        DELETE
        FROM especie
        WHERE especie = {}'''.format(especie)

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


create_table()

"""
main code
"""


def add_data(symbol, securitySubType, securityType):
    add_security(symbol, securitySubType, securityType)


def get_data():
    return get_securities()


def show_data():
    securities = get_data()
    for security in securities:
        print(security)


def show_data_by_id(id_):
    security = get_security_by_symbol(id_)
    if not security:
        print("No data found at securities", id_)
    else:
        print(security)


def select():
    sp.call('clear', shell=True)
    sel = input("1. Add data\n2. Show Data\n3. Search\n4. Update\n5. Delete\n6. Exit\n\n")

    if sel == '1':
        sp.call('clear', shell=True)
        symbol = input('Symbol: ')
        securityType = input('Type: ')
        securitySubType = input('SubType: ')
        add_data(symbol, securitySubType, securityType)

    elif sel == '2':
        sp.call('clear', shell=True)
        show_data()
        input("\n\npress enter to back:")

    elif sel == '3':
        sp.call('clear', shell=True)
        id__ = input('Enter Symbol: ')
        show_data_by_id(id__)
        input("\n\npress enter to back:")

    elif sel == '4':
        sp.call('clear', shell=True)
        id__ = input('Enter Symbol: ')
        show_data_by_id(id__)
        print()
        symbol = input('Symbol: ')
        securityType = input('SecurityType: ')
        securitySubType = input('securitySubType: ')
        update_especie(symbol, securityType, securitySubType)
        input("\n\nYour data has been updated \npress enter to back:")

    elif sel == '5':
        sp.call('clear', shell=True)
        id__ = int(input('Enter Especie: '))
        show_data_by_id(id__)
        delete_especie(id__)
        input("\n\nYour data has been deleted \npress enter to back:")

    else:
        return 0

    return 1


while select():
    pass
