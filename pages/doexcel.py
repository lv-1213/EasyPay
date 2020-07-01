import xlwt
def readExcel(title,list_data,path):
    workBook = xlwt.Workbook()
    workSheet = workBook.add_sheet('Sheet1')
    for i in range(len(title)):

        workSheet.write(0, i, title[i])
    x = 1
    for data in list_data:
        for y in range(len(data)):
            workSheet.write(x, y, data[y])
        x += 1
    workBook.save(path)

