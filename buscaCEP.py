#pip3 install 
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("--------------------")
print("----consulta CEP----")
print("--------------------")
print()

cep_input = str(input ("Digite o CEP: "))

if len(cep_input) != 8:
    print("Quantidade de digitos invalido!!!")
    exit()
    
url_result = "https://viacep.com.br/ws/{}/json/".format(cep_input)
r = requests.get(url_result)
endereco_data = r.json()
if 'erro'not in endereco_data:
    print("CEP digitado {}".format(cep_input))
    time.sleep(1)
    print("==>CEP encontrado<==")
    time.sleep(2)
    print("CEP: {}".format(endereco_data["cep"]))
    print("Logradouro: {}".format(endereco_data["logradouro"]))
    print("Complemento: {}".format(endereco_data["complemento"]))
    print("Bairro: {}".format(endereco_data["bairro"]))
    print("Localidade: {}".format(endereco_data["localidade"]))
    print("UF: {}".format(endereco_data["uf"]))
else:
    print("{} -> CEP invalido!!!!".format(cep_input))
    exit() 

################################################
########### MOSTRA NO GOGLE MAPS################
################################################

input("Presione Enter ,para olhar no mapa ")
url ='https://www.google.com.br/maps/'


navegador = webdriver.Chrome(executable_path="chromedriver.exe")
navegador.maximize_window()

navegador.get(url)

input_box = navegador.find_element_by_id("searchboxinput")
time.sleep(1)
input_box.send_keys(cep_input)
input_box.send_keys(Keys.ENTER)
time.sleep(1.5)
input_box1 = navegador.find_element_by_xpath("//*[@id='minimap']/div/div[2]/button").click()
input_box.submit()