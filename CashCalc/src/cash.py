# -*- coding: utf-8 -*-

import os
import re
import sys

text = os.getenv('POPCLIP_TEXT')
currency = os.getenv('POPCLIP_OPTION_CURRENCY')
text = text.decode("utf-8")
pattern = "(?:)(([£$€]|USD|EUR|GBP)[ .]?(\d|[,.](?=\d{3}))+([,.]\d{1,2})?m?(bn)?(tn)?k?|(\d|,(?=\d{3})|\.(?=\d{2}))+(p|c| ?EUR| ?GBP| ?USD| ?pence| ?pound| ?dollar| ?cent| ?euro))"
pricesGroup = re.findall(pattern, text)
if currency == "GBP":
    priceList = []
    for price in pricesGroup:
        priceList += [price[0]]
  	pricetotal = 0
    for priceStr in priceList:
        pounds='0'
        pence='0'
        containsDecimal=False
        if '.' in priceStr:
            containsDecimal = True
        if 'p' in priceStr and containsDecimal==False:
            for char in priceStr:
                if char in '0123456789':
                    pence += char
        poundYes = False
        for char in priceStr:
            if char == '£':
                poundYes = True
        if poundYes == True or containsDecimal == True:
            reachedDecimalPoint = False 
            for char in priceStr:
                if reachedDecimalPoint == True and char in '0123456789':
                    pence += char
                elif char == '.':
                    reachedDecimalPoint = True
                elif char in '0123456789':
                    pounds += char
        pounds = int(pounds)
        pence = int(pence)/100
        price = pounds + pence
        pricetotal += price
        price = 0;
    totalString = '£'+str(pricetotal)+' total'
    print(totalString)
else:
    print("Currency not currently supported")
