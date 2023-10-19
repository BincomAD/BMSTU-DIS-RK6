import pymysql
from sql_provider import SQLProvider

provider = SQLProvider("./db/sql")

db = pymysql.connect(
    host='localhost',
    user='root',
    password='zxc123',
    db='supermarket',
    )

def getProduct():
    cursor = db.cursor()

    params = {'params':'*'}
    sql_code = provider.get_sql(
        'get.sql',
        params
    )

    cursor.execute(sql_code)
    results = cursor.fetchall()

    cursor.close()
    return results

def getByPrice(priceOt, priceDo):
    cursor = db.cursor()

    params = {'ot':priceOt, 'do':priceDo}
    sql_code = provider.get_sql(
        'getbyprice.sql',
        params
    )

    cursor.execute(sql_code)
    results = cursor.fetchall()

    cursor.close()
    return results

def getByCategory(category):
    cursor = db.cursor()

    params = {'category':category}
    sql_code = provider.get_sql(
        'getbycategory.sql',
        params
    )

    cursor.execute(sql_code)
    results = cursor.fetchall()

    cursor.close()
    return results
