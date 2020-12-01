from headers import *

################## Open csv file to stoare the data ########################
csvfile = open('dairyData_sample.csv','w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Title','Name','Diary No.','Case No.','Present/Last Listed On','Status/Stage','Disp.Type','Category','Act','Petitioner(s)','Respondent(s)','Pet. Advocate(s)','Resp. Advocate(s)','U/Section',])


################## write data into file ##############################
def write_into_file(data):
	csvwriter.writerow(data)



###################Get Data from URL ################################
def get_data():
	url="https://main.sci.gov.in/case-status"
	options = webdriver.ChromeOptions()
	options.add_argument("headless")
	driver = webdriver.Chrome(executable_path='./chromedriver')
	# ,options=options)
	for i in range(1,21):
		driver.get(url)
		time.sleep(5)
		input_value = driver.find_element_by_xpath('''//*[@id="CaseDiaryNumber"]''').send_keys(i)
		for j in range(1,21):
			try:
				captcha=None
				time.sleep(2)
				captcha = driver.find_element_by_xpath('''//*[@id="cap"]/font''').text
				time.sleep(2)
				driver.find_element_by_xpath('''//*[@id="ansCaptcha"]''').send_keys(captcha)
				open_drop_down = driver.find_element_by_xpath('''//*[@id="CaseDiaryYear"]''')
				time.sleep(1)
				open_drop_down.click()
				dropdown_year_value = open_drop_down.find_element_by_xpath('''//*[@id="CaseDiaryYear"]/option['''+str(22-j)+''']''')
				time.sleep(1)
				dropdown_year_value.click()
				time.sleep(1)
				driver.find_element_by_xpath('''//*[@id="getCaseDiary"]''').click()
				time.sleep(2)
				soup_file=driver.page_source
				soup = BeautifulSoup(soup_file,'lxml')
				time.sleep(2)
				table_div = soup.find('div',{"class":"panel-body table-responsive"})
				time.sleep(3)
				table_row = table_div.find_all('tr')
				time.sleep(1)
				case_title = driver.find_element_by_xpath('''//*[@id="DNdisplay"]/h5[1]''').text
				time.sleep(1)
				case_name  = driver.find_element_by_xpath('''//*[@id="DNdisplay"]/h5[2]''').text
				columns= []
				columns.append(case_title)
				columns.append(case_name)
				for k in range(0,len(table_row)):
					td_data = (table_row[k]).text
					td_data = td_data.strip('\n')
					if("Diary No." in td_data):
						td_data = td_data.replace('Diary No.','')
					if("Case No." in td_data):
						td_data = td_data.replace('Case No.','')
					if("Present/Last Listed On" in td_data):
						td_data = td_data.replace('Present/Last Listed On','')
					if("Status/Stage" in td_data):
						td_data = td_data.replace('Status/Stage','')
					if("Disp.Type" in td_data):
						td_data = td_data.replace('Disp.Type','')
					if("Act" in td_data):
						td_data = td_data.replace('Act','')
					if("Petitioner(s)" in td_data):
						td_data = td_data.replace('Petitioner(s)','')
					if("Respondent(s)" in td_data):
						td_data = td_data.replace('Respondent(s)','')
					if("Pet Advocate(s)" in td_data):
						td_data = td_data.replace('Pet Advocate(s)','')
					if("Resp. Advocate(s)" in td_data):
						td_data = td_data.replace('Resp. Advocate(s)','')
					if("U/Section" in td_data):
						td_data = td_data.replace('U/Section','')

					td_data = td_data.strip('\n')
					columns.append(td_data)
				write_into_file(columns)

			except:
				captcha=None
				print("No case found")

			finally:
				captcha=None

# main function i.e start point of program

if __name__=="__main__": 
    get_data()