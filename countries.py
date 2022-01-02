import sqlite3
import json
import sys
import os

countriesDbPath = "countriesCodes.sqlite"

class PaisYMoneda:

    def __init__(self, ctryCd):
        self.ctryCd = ctryCd.upper()

    def toString(self):
        return 'ctrsCode: ' + self.ctryCd


def startApp(countries, currency):
    print('countries type:', type(countries))
    print('currency type:', type(currency))

    ctrsXcrcy = {ctry['Name'].upper():PaisYMoneda(ctry['Code']) for ctry in countries}


    print()
    print('-------------countries--------------')
    for k, v in ctrsXcrcy.items():
        print('ctry: ', k, ' ', v.toString())



def main(argv):
    ctry = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/', 'countries.json'))
    with open(ctry, 'r') as f:
        countries = json.load(f)

    ccy = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/', 'currency.json'))
    with open(ccy, 'r') as f:
        currency = json.load(f)

    startApp(countries, currency)


def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))


init()
