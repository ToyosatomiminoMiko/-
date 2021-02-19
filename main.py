import matplotlib.pyplot as plt
import xlrd
import numpy

x = []#时间轴
y = []#值

#打开文件
work_book = xlrd.open_workbook('1.xls')
#获取表
sheet_1 = work_book.sheet_by_name(work_book.sheet_names()[0])
#行数
row_sum = sheet_1.nrows
#列数
row_len = sheet_1.row_len(0)
#遍历
for i in range(1,row_sum):
    cell_0_value = sheet_1.cell_value(i,1)[0:-1]
    x.append(int(cell_0_value))
for i in range(1,row_sum):
    cell_0_value = sheet_1.cell_value(i,2)
    y.append(int(cell_0_value))
print(x,y,end='\n')
myline = numpy.linspace(2000, 2050, 100)
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

