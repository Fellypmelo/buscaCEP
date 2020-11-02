import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("-----------------------------")
print("----consulta CEP Portugal----")
print("-----------------------------\n")

cep4 = str(input("Digite 4 digitos: "))
print(cep4)
cep3 = str(input("Digite 3 digitos: "))
print(cep3)
ceppt = cep4 + cep3

if len(ceppt) != 7:
     print("Quantidade de digitos invalido!!!")
     exit()

print(cep4+"-"+cep3)

url_result = 'https://www.codigo-postal.pt/?cp4={}&cp3={}'.format(cep4,cep3)

request = requests.get(url_result)

print("CEP digitado => "+(cep4+"-"+cep3))
time.sleep(1)

print("==>CEP encontrado<==")

soup = bs(request.content,'html.parser')

rua = soup.find_all( 'a',{'class':'search-title'} )
for rua_1  in rua:
    rua_1.next_element
print("Rua :"+ rua_1.next_element)
local = soup.find_all( 'span',{'class':'local'} )
print("|Bairro|Estado|")
for dados in local:
   print(dados.next_element)
#############################################
#############GOOGLE MAPS#####################
#############################################
input("Presione Enter ,para olhar no mapa ")

url_cosulta = 'https://www.google.com.br/maps/'

driver = webdriver.Firefox()

driver.maximize_window()

driver.get(url_cosulta)

input_box = driver.find_element_by_id("searchboxinput")
time.sleep(2)
input_box.send_keys(ceppt + " pt")
input_box.send_keys(Keys.ENTER)
input_box1 = driver.find_element_by_xpath("//*[@id='minimap']/div/div[2]/button").click()
input_box.submit()