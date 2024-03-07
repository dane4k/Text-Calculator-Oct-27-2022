dictones = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
            10: 'десять'}

dicteleventotwenty = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
                      16: 'шестнадцать', 17: 'семнадцать', 18: 'восемьнадцать', 19: 'девятнадцать', 20: 'двадцать'}

dictthirtytoninety = {30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
                      80: 'восемьдесят',
                      90: 'девяносто'}

dict100 = {100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот',
           800: 'восемьсот', 900: 'девятьсот'}

dict1000 = {1000: 'одна тысяча', 2000: 'две тысячи', 3000: 'три тысячи', 4000: 'четыре тысячи', 5000: 'пять тысяч',
            6000: 'шесть тысяч', 7000: 'семь тысяч', 8000: 'восемь тысяч', 9000: 'девять тысяч', 10000: 'десять тысяч'}

dictonesreversed = dict(zip(dictones.values(), dictones.keys()))  # перевернул для своего удобства
dicteleventotwentyreversed = dict(zip(dicteleventotwenty.values(), dicteleventotwenty.keys()))
dictthirtytoninetyreversed = dict(zip(dictthirtytoninety.values(), dictthirtytoninety.keys()))
dict100reversed = dict(zip(dict100.values(), dict100.keys()))
dict1000reversed = dict(zip(dict1000.values(), dict1000.keys()))

listfirstnumint = []  # заносим интовые числа или цифру
listsecondnumint = []  # заносим интовые числа или цифру

firstnumber = input()  # вводим число буквенной записью
operation = input()  # operacia
secondnumber = input()  # второе число
firstnumberlist = firstnumber.split()  # ['сто', 'тридцать']
secondnumberlist = secondnumber.split()

if firstnumber.count(' ') == 0:  # если цифра или десяток, сотня
    if firstnumber in dictonesreversed:
        listfirstnumint.append(dictonesreversed[firstnumber])
    if firstnumber in dicteleventotwentyreversed:
        listfirstnumint.append(dicteleventotwentyreversed[firstnumber])
    if firstnumber in dictthirtytoninetyreversed:
        listfirstnumint.append(dictthirtytoninetyreversed[firstnumber])
    if firstnumber in dict100reversed:
        listfirstnumint.append(dict100reversed[firstnumber])

if firstnumber.count(' ') == 1:  # если число
    if firstnumberlist[0] in dicteleventotwentyreversed:
        listfirstnumint.append(dicteleventotwentyreversed[firstnumberlist[0]])
    if firstnumberlist[0] in dictthirtytoninetyreversed:
        listfirstnumint.append(dictthirtytoninetyreversed[firstnumberlist[0]])
    if firstnumberlist[0] in dict100reversed:
        listfirstnumint.append(dict100reversed[firstnumberlist[0]])
    if firstnumberlist[1] in dictonesreversed:
        listfirstnumint.append(dictonesreversed[firstnumberlist[1]])
    if firstnumberlist[1] in dicteleventotwentyreversed:
        listfirstnumint.append(dicteleventotwentyreversed[firstnumberlist[1]])
    if firstnumberlist[1] in dictthirtytoninetyreversed:
        listfirstnumint.append(dictthirtytoninetyreversed[firstnumberlist[1]])
    if firstnumberlist[1] in dict100reversed:
        listfirstnumint.append(dict100reversed[firstnumberlist[1]])

firstnumintresult = sum(listfirstnumint)  # итоговое первое интовое число

if secondnumber.count(' ') == 0:  # если цифра
    if secondnumber in dictonesreversed:
        listsecondnumint.append(dictonesreversed[secondnumber])
    if secondnumber in dicteleventotwentyreversed:
        listsecondnumint.append(dicteleventotwentyreversed[secondnumber])
    if secondnumber in dictthirtytoninetyreversed:
        listsecondnumint.append(dictthirtytoninetyreversed[secondnumber])
    if secondnumber in dict100reversed:
        listsecondnumint.append(dict100reversed[secondnumber])

if secondnumber.count(' ') == 1:  # если число
    if secondnumberlist[0] in dicteleventotwentyreversed:
        listsecondnumint.append(dicteleventotwentyreversed[secondnumberlist[0]])
    if secondnumberlist[0] in dictthirtytoninetyreversed:
        listsecondnumint.append(dictthirtytoninetyreversed[secondnumberlist[0]])
    if secondnumberlist[0] in dict100reversed:
        listsecondnumint.append(dict100reversed[secondnumberlist[0]])
    if secondnumberlist[1] in dictonesreversed:
        listsecondnumint.append(dictonesreversed[secondnumberlist[1]])
    if secondnumberlist[1] in dicteleventotwentyreversed:
        listsecondnumint.append(dicteleventotwentyreversed[secondnumberlist[1]])
    if secondnumberlist[1] in dictthirtytoninetyreversed:
        listsecondnumint.append(dictthirtytoninetyreversed[secondnumberlist[1]])
    if secondnumberlist[1] in dict100reversed:
        listsecondnumint.append(dict100reversed[secondnumberlist[1]])

secondnumintresult = sum(listsecondnumint)  # итоговое интовое второе число

if operation == 'плюс':
    answer = firstnumintresult + secondnumintresult
if operation == 'минус':
    answer = firstnumintresult - secondnumintresult
if 'умножить' in operation:
    answer = firstnumintresult * secondnumintresult

answerinsymbstr = []  # список с ответом в виде строчек по символам
answerfinal = []  # финальный ответ, выводим это

for symbols in str(answer):  # добавляем ответ в виде строчки посимвольно в список
    answerinsymbstr.append(symbols)
answerinsymbint = [int(s) for s in answerinsymbstr]  # переводим все строковые символы(ответ) в инт
if len(answerinsymbstr) == 5:  # если ответ - 10000
    print(dict1000.get(10000))
if len(answerinsymbstr) == 4:  # если четырехзначное число
    answerfinal.append(dict1000[answerinsymbint[0] * 1000])
    if answerinsymbint[1] != 0:
        answerfinal.append(dict100[answerinsymbint[1] * 100])
    if answerinsymbint[2] != 0:
        if answerinsymbint[2] * 10 in dictones:
            answerfinal.append(dictones[answerinsymbint[2] * 10])
        elif answerinsymbint[2] * 10 in dicteleventotwenty:
            answerfinal.append(dicteleventotwenty[answerinsymbint[2] * 10])
        elif answerinsymbint[2] * 10 in dictthirtytoninety:
            answerfinal.append(dictthirtytoninety[answerinsymbint[2] * 10])
    if answerinsymbint[3] != 0:
        if answerinsymbint[3] in dictones:
            answerfinal.append(dictones[answerinsymbint[3]])
if len(answerinsymbstr) == 3:  # если 3хзначное число
    answerfinal.append(dict100[answerinsymbint[0] * 100])
    if answerinsymbint[1] != 0:
        if answerinsymbint[1] * 10 in dicteleventotwenty:
            answerfinal.append(dicteleventotwenty[answerinsymbint[1] * 10])
        elif answerinsymbint[1] * 10 in dictthirtytoninety:
            answerfinal.append(dictthirtytoninety[answerinsymbint[1] * 10])
    if answerinsymbint[2] != 0:
        if answerinsymbint[2] in dictones:
            answerfinal.append(dictones[answerinsymbint[2]])
if len(answerinsymbstr) == 2:  # если 2хзначное число
    if answerinsymbint[0] != 0:
        if answerinsymbint[0] * 10 in dicteleventotwenty:
            answerfinal.append(dicteleventotwenty[answerinsymbint[0] * 10])
        elif answerinsymbint[0] * 10 in dictthirtytoninety:
            answerfinal.append(dictthirtytoninety[answerinsymbint[0] * 10])
    if answerinsymbint[1] != 0:
        if answerinsymbint[1] in dictones:
            answerfinal.append(dictones[answerinsymbint[1]])
if len(answerinsymbstr) == 1:  # если ответ - цифра
    if answerinsymbint[0] != 0:
        if answerinsymbint[0] in dictones:
            answerfinal.append(dictones[answerinsymbint[0]])
                    
print(' '.join(answerfinal))  # выводим ответ с помощью джойна
