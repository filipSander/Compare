import xlrd
import xlwt



def checkFileStructure(path):
    
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)

    rows = []
    for i in range(0, 3):
        ceils = []
        for c in sheet.row(i):
            if c.ctype == 2:
                ceils.append(str(round(c.value, 2)))
            elif c.ctype != 0: 
                ceils.append(str(c.value))

        rows.append(ceils)
        
    return rows

def compare(files, params):
    books = []
    for path in files:
        books.append(xlrd.open_workbook(path))
    
    data = []
    for i in range(0, len(books)):
        for r in books[i].sheet_by_index(0).get_rows():
            if r[params[i].name].ctype == 1 and r[params[i].price].ctype == 2:

                docRow = Row()
                for j in range(0, len(r)):
                    if j == params[i].name and r[j].ctype == 1:
                        docRow.name = r[j].value
                    elif j == params[i].price and r[j].ctype == 2:
                        docRow.price = r[j].value
                    else:
                        docRow.our.append(r[j].value)
                data.append(docRow)
    
    while findDuplicate(data):
        pass

    return data


def findDuplicate(data):
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if data[i].name.strip().lower() == data[j].name.strip().lower() and i != j:
                if data[i].price >= data[j].price:
                    data.remove(data[i])
                    return True
    return False


def writeFile(data):
    workbook = xlwt.Workbook()
    #region -- Style --
    sheet = workbook.add_sheet('result')
    
    xlwt.add_palette_colour("custom_colour", 0x21)
    workbook.set_colour_RGB(0x21, 115, 181, 110)

    xlwt.add_palette_colour("custom_colour2", 0x22)
    workbook.set_colour_RGB(0x22, 181, 110, 161)

    style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
    style2 = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour2')
    sheet.col(0).width = 9000
    #endregion -- Style --

    for i in range(0, len(data)):
        sheet.write(i, 0, data[i].name, style)
        sheet.write(i, 1, data[i].price, style2)
        m = 2
        for j in data[i].our:
            sheet.write(i, m, j)
            m += 1
    workbook.save('output.xls')


class Row:
    name: str
    price: float
    our = []

    def __init__(self) -> None:
        self.our = []

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}, our"

