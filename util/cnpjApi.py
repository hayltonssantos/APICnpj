import requests


class CnpjApi:
    def __init__(self, cnpj):
        self.cnpj = cnpj
        url = "https://consulta-cnpj-gratis.p.rapidapi.com/companies/{}".format(
            self.cnpj)
        url2 = "https://www.receitaws.com.br/v1/cnpj/{}".format(self.cnpj)
        headers = {
            'x-rapidapi-host': "consulta-cnpj-gratis.p.rapidapi.com",
            'x-rapidapi-key': "0c918d40d3msh6949bbc4e5556aap11a103jsne0bcaf88400a"
        }

        self.response = requests.request("GET", url, headers=headers)
        self.response = self.response.json()

    def validate(self):
        cnpj = self.cnpj
        if len(cnpj) != 14:
            return False
        else:
            return True

    def getNome(self):
        self.nome = self.response["name"]
        return self.nome

    def getEmail(self):
        self.email = self.response["email"]
        return self.email

    def getAbertura(self):
        self.abertura = self.response["founded"]
        return self.abertura

    def getType(self):
        self.type = self.response["type"]
        return self.type

    def getSize(self):
        self.size = self.response["size"]
        return self.size

    def getAlias(self):
        self.alias = self.response['alias']
        return self.alias

    def getStatus(self):
        self.status = self.response["registration"]['status']
        return self.status

    def getJuridico(self):
        self.juridico = self.response["legal_nature"]['description']
        return self.juridico

    def getDescricao(self):
        self.descricao = self.response["primary_activity"]['description']
        return self.descricao

    def getEndereco(self):
        self.rua = self.response["address"]['street']
        self.numero = self.response["address"]['number']
        self.detalhes = self.response["address"]['details']
        self.cep = self.response["address"]['zip']
        self.bairro = self.response["address"]['neighborhood']
        self.cidade = self.response["address"]['city']
        self.estado = self.response["address"]['state']
        self.endereco = [self.rua, self.numero, self.detalhes,
                         self.cep, self.bairro, self.cidade, self.estado]
        return self.endereco

    def getSimei(self):
        self.simei = self.response['simples_nacional']['simei_optant']
        return self.simei

    def getJson(self):
        self.lista = self.getNome(), self.getEmail(), self.getAbertura(), self.getType(), self.getSize(), self.getAlias(
        ), self.getStatus(), self.getJuridico(), self.getDescricao(), self.getEndereco(), self.getSimei()
        return self.lista

    def getAll(self):
        print(self.response)
