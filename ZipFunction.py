"""
we can zip the items more than one list using zip function
converted data can be converted in tuple , list, dictionary
"""

item = {'car', 'bike', 'table', 'pen',}
price = {25000, 40000, 340, 2323}
stocks = {23, 34, 45 }
zipped = tuple(zip(item, price, stocks))
print(zipped)
