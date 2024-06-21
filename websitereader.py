with open("Magic Formula Investing.html", "r", encoding='utf-8') as hmtlfile:
    contents = hmtlfile.read()
    contents = contents[contents.find("<td align"):contents.rfind("</td>")+len("</td>")]
    contents = contents.replace("</tr>", '').replace(" ", '').replace('<tdalign="left">', '').replace('</td>', '').replace('<tdalign="center">', '').replace('<trclass="altrow">', '').replace('<trclass="">', '')
    
lines = contents.split("\n")
tickers = []

for index, item in enumerate(lines):
    if ((index-1) % 7) == 0:
        tickers.append(item)

with open("stocks.txt", 'w') as stocksfile:
    for ticker in tickers:
        stocksfile.write(ticker+'\n')

print(tickers)