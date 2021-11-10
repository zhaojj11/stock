import os
import time
import tushare as ts
import pandas as pd

column = ['股票号', '现价', '成本价', '持仓股数', '盈亏']
stock_list = [
    {
        'code': '002520',
        'name': '',
        'price': 0,
        'cost': 9.149,
        'hold': 800,
        'earnings': 0
    },
    {
        'code': '000678',
        'name': '',
        'price': 0,
        'cost': 4.403,
        'hold': 300,
        'earnings': 0
    }
]

table = {
    'name': [],
    'price': [],
    'cost': [],
    'hold': [],
    'earnings': []
}

def white(value):
    return '\33[37m{value}\33[0m'.format(value=value)

def red(value):
    return '\33[31m{value}\33[0m'.format(value=value)

def green(value):
    return '\33[32m{value}\33[0m'.format(value=value)

def generateData():
    table['name'].clear()
    table['price'].clear()
    table['cost'].clear()
    table['hold'].clear()
    table['earnings'].clear()

    for stock in stock_list:
        df = ts.get_realtime_quotes(stock['code'])

        stock['name'] = df['name'][0]
        stock['price'] = float(df['price'][0])
        stock['earnings'] = float(stock['price']-stock['cost']) * stock['hold']

        table['name'].append(stock['name'])
        table['price'].append(stock['price'])
        table['cost'].append(stock['cost'])
        table['hold'].append(stock['hold'])
        table['earnings'].append(stock['earnings'])

if __name__ == '__main__':
    while True:
        generateData()
        df = pd.DataFrame(table)
        os.system('cls')
        print(df)
        time.sleep(5)

