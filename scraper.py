
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import xlsxwriter 


def get_data(url):

	# opening the url
	url_client = urlopen(url)
	# getting the content of the url.
	url_content = url_client.read()
	url_client.close()

	# uncomment this to parse .html files. 
	# parser = soup(open("test.html"), "html.parser")

	# beautiful soup parser to parse the files in html. 
	parser = soup(url_content, "html.parser")

	content = parser.findAll('div', {'class': 'freebirdFormviewerViewItemsItemItemHeader'})
	# print(parser.name_of_tag) to print the first element of that particular tag. 

	return content


def store_excel(data):

	# Workbook() takes one, non-optional, argument  
	# which is the filename that we want to create. 
	workbook = xlsxwriter.Workbook('content.xlsx') 
	  
	# The workbook object is then used to add new  
	# worksheet via the add_worksheet() method. 
	worksheet = workbook.add_worksheet() 
	  
	# Use the worksheet object to write 
	# data via the write() method. 

	row = 0
	col = 0

	# parse the data and store it in the excel sheet. 
	for item in data:

		text = str(item.text)
		worksheet.write(row, col, text)
		row += 1
	# Finally, close the Excel file 
	# via the close() method. 
	workbook.close() 

if __name__ == '__main__':


	url = input('enter the url: ')

	data = get_data(url)

	print(data)

	store_excel(data)

