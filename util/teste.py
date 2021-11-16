import requests

class CnpjApi:
    def __init__(self):
        self.url = 'https://www.receitaws.com.br/v1/cnpj/'

    def get_cnpj(self, cnpj):
        response = requests.get(self.url + cnpj)
        return response.json()
    
    def get_status(self, cnpj):
        return self.get_cnpj(cnpj)['status']

print(CnpjApi().get_cnpj('07.818.865/0001-00'))