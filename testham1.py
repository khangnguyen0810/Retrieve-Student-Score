import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pya
import pyperclip  # handy cross-platform clipboard text handler
import time
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)
list_diem = []
f = open("diemthiTHPTQG_v2.csv", 'a')
information_list = []
header = ['	 SBD','		Họ tên','Toán','Ngữ văn','Vật lí','Hóa học','Sinh học','KHTN','Lịch sử','Địa lí','GDCD','KHXH','Ngoại ngữ']
tong_mon_thi = ['Toán','Ngữ văn','Vật lí','Hóa học','Sinh học','KHTN','Lịch sử','Địa lí','GDCD','KHXH','Ngoại ngữ']
mon_ngoai_ngu = ['Tiếng Anh', 'Tiếng Nga', 'Tiếng Pháp', 'Tiếng Trung Quốc', 'Tiếng Đức','Tiếng Nhật','Tiếng Hàn']
empty_list_diem = ['','','','','','','','','','','']
khongtontai = 'Thí sinh không tồn tại'

def locmonthi(diemthi):
	mon_duoc_thi = []
	for i in tong_mon_thi:
		if i in diemthi:
			mon_duoc_thi.append(i)
	for j in mon_ngoai_ngu:
	    if j in diemthi:
	        mon_duoc_thi.append(j)
	return mon_duoc_thi

def locdiemthi(diemthi):
	for i in tong_mon_thi:
	    for j in mon_ngoai_ngu:
    		diemthi = diemthi.replace(i,'').strip()
    		diemthi = diemthi.replace(j,'').strip()
    		diemthi = diemthi.replace(':','')
    		diemthi = diemthi.replace('      ',' ')
    		diemthi = diemthi.replace('    ',' ')
	diemthi = diemthi.split(' ')
	return diemthi

def sapxepdiem(monthi, diemthi):
    count = 0
    index = []
    empty_list_diem = ['','','','','','','','','','','']

    for i in tong_mon_thi:
        for j in monthi:
            if j == i:
                index.append(tong_mon_thi.index(j))
    for i in mon_ngoai_ngu:
        for j in monthi:
            if j == i:
                index.append(10)
    print(index)
    for i in diemthi:
    	empty_list_diem[index[count]]= i
    	count += 1
    return empty_list_diem

def combine_3_info(i, ten, diemthi):
	diemthi.insert(0,ten)
	diemthi.insert(0,'0'+str(i))
	return diemthi

for i in range (2000139,2000140):
	personal_information = []
	driver.get('http://diemthi.hcm.edu.vn/')
	driver.find_element(By.NAME,'SoBaoDanh').send_keys('0'+ str(i))
	driver.find_element(By.XPATH, "//input[@value='Xem điểm'][@type='submit']").click()
	page_source = driver.page_source
	soup = BeautifulSoup(page_source, 'html.parser')
	reviews_selector = soup.find_all('tr')
	if reviews_selector:
		candidate_information = reviews_selector[1]
		ten = candidate_information.find_all('td')[0]
		ten = ten.get_text().strip()
		diemthi = candidate_information.find_all('td')[2]
		diemthi = diemthi.get_text().strip()
		# print(diemthi)
		# monthi = locmonthi(diemthi)
		# print(monthi)
		# diemthi = locdiemthi(diemthi)
		# print(diemthi)
		# diemthi = sapxepdiem(monthi, diemthi)
		# candidate_information = candidate_information.get_text()
		# list_diem.append(candidate_information)
		# personal_information = combine_3_info(i, ten, diemthi)
		information_list.append(personal_information)
		diem = str(ten) + str(diemthi) +'\n'
	else:
		information_list.append(['0'+str(i),khongtontai,'','','','','','','','','','',''])
	print('0'+ str(i))

writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
writer.writerow(header)
for x in information_list:
	writer.writerow(x)

for i in tong_mon_thi:
    for j in mon_ngoai_ngu:
    	diemthi = diemthi.replace(i,'').strip()
    	diemthi = diemthi.replace(j,'').strip()
    	diemthi = diemthi.replace(':','')
    	diemthi = diemthi.replace('      ',' ')
    	diemthi = diemthi.replace('    ',' ')
    	print(diemthi)
diemthi = diemthi.split(' ')
f.close()
input()




