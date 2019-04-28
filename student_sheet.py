# create an application that will take a list of student names and open the list in excel 
import xlsxwriter

# Workbook takes one arguement which is the name of the xl file we want to create
workbook = xlsxwriter.Workbook("students.xlsx")

worksheet = workbook.add_worksheet()

worksheet.write("A1", "First Names")
worksheet.write("B1", "Last Names")

worksheet.write("A2", "Jordan")
worksheet.write("B2", "Rosas")

workbook.close()

