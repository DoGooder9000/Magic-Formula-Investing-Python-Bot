import requests

class Stock:
    def __init__(self, name: str, ey: float, roic: float):
        self.name = name
        self.ey = ey
        self.roic = roic
    
    def __repr__(self) -> str:
        return f"{self.name}:\n\tEY: {self.ey}\n\tROIC: {self.roic}\n"

def GetInfo(ticker_symbol = None):
    if ticker_symbol == None:
        ticker_symbol = input("Enter Ticker Symbol: ")

    url = f"https://stockanalysis.com/stocks/{ticker_symbol}/statistics/"

    ROIC_text = "return on invested capital"
    EY_text = "Earnings Yield"

    try:
        page = requests.get(url)

        EY_string = page.text[page.text.index(EY_text):]
        EY_string = EY_string[:EY_string.index('%')+1]
        EY_string = EY_string[EY_string.index('title'):]

        replace_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()% <>/=":    []'

        for char in replace_string:
            EY_string = EY_string.replace(char, '')

        ey = float(EY_string)
    
    except:
        ey = 0
    
    try:
        ROIC_string = page.text[page.text.index(ROIC_text):]
        ROIC_string = ROIC_string[:ROIC_string.index('%')+1].strip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()% ')

        #print ROIC
        roic = float(ROIC_string)

    except:
        roic = 0
    
    print(Stock(ticker_symbol, ey, roic))

    return Stock(ticker_symbol, ey, roic)

#ans = input()
'''
if ans:
    while True:
        GetInfo()
'''
#else:
with open("stocks.txt") as file:
    stocks = []
    for ticker in file.readlines():
        stocks.append(GetInfo(ticker.strip()))
    
    stocks = sorted(stocks, key=lambda x: x.ey + x.roic, reverse=True)

    print("---------------------------")
    for stock in stocks: print(stock, end='')