from Utilites import XLUtils

# path = r"D:\Product-Compare-Muti-Sites\Results\E-Commerce-data.xlsx\E-Commerce-data.xlsx"
# rows = XLUtils.getRowCout(path, 'Sheet1')


def write_result(flag,r):
    path = "D:\Product-Compare-Muti-Sites\Results\E-Commerce-data.xlsx"
    # rows = XLUtils.getRowCout(path, 'Sheet1')
    if flag:
        # print("Test Passed...")
        XLUtils.writeData(path, 'Sheet1', r, 2, 'Pass')

    else:
        # print("Failed...")
        XLUtils.writeData(path, 'Sheet1', r, 2, 'Fail')

def write_product_result(company_name,value):
    path = "D:\Product-Compare-Muti-Sites\Results\E-Commerce-data.xlsx"
    pass
    # rows = XLUtils.getRowCout(path, 'Sheet1')
        # print("Test Passed...")
        # XLUtils.writeData(path, 'Sheet1', r, 2, 'Pass')
