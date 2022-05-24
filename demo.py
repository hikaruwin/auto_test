import xlwings as xw

# app = xw.App(visible=False, add_book=False)
# wb = app.books.open('test.xlsx')
# sht = wb.sheets('Sheet1')
# data = sht.range('A1').value
# print(data)
# # input()
# time.sleep(3)
# wb.save()
# wb.close()

with xw.App(visible=False, add_book=False) as app:
    count = xw.apps.count
    wb = app.books.open(r'd:\auto_test\test.xlsx')
    sht = wb.sheets[0]
    key = sht['A1'].expand().value[0]
    value = sht['A1'].expand().value[1:]
    value1 = sht['A1'].expand('right').value
    data1 = []
    for i in range(len(value)):
        data = dict(zip(key, value[i]))
        data1.append(data)
    # print(data1)
    # print(sht['A1:A3'].value)
    # print(sht['A2'].expand().value)
    print(key, value, value1, data1, sep='\n')

