#import the xlrd module for working with xlsx extension files
import xlrd
traverseresult = list() #create an empty list to hold results of the data gotten from the file
#create a class that can make instances of xlsx file objects
class ReadXlsx(object):
	#Create a method to open the file and traverse it
	def traversefile(self, filepath):
		#Open the spreadsheet file
		workbook = xlrd.open_workbook(filepath)
		#Open the first sheet in the file
		worksheet = workbook.sheet_by_index(0)
		#Create a for loop to iterate through all the colums in the file diagonally
		#store them into an Array/List for further actions
		total_cols = worksheet.ncols
		for i in range(total_cols):
			traverseresult.append(worksheet.cell(i, i).value)
		return traverseresult	
	#Add a method to display the values stored in the list dynamically printed on one line	
	def displayTraverseValues(self):
		print(" ".join(str(x) for x in traverseresult))
		'''
		for i in traverseresult:
			print(i, end = " ")
		'''



def main():
	test = ReadXlsx()
	test.traversefile("qzAjJo.xlsx")
	test.displayTraverseValues()



if __name__ == '__main__':
	main()