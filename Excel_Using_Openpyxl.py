import openpyxl
wb =openpyxl.Workbook()
sh =wb.active
sh.title ="New Sheet"
print(sh.title)
rows =((1,2,3),(2,3,4),(4,5,6))
for row in rows:
    sh.append(row)
wb.save("C:\\Users\\PycharmProjects\\Automation\\configuration\\num.xlsx")   #enter your path here
