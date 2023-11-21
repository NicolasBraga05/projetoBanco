import requests

cep = input('Informe seu CEP: ')
cep = cep.replace(' ', '').replace('.', '').replace('-', '')

def buscaCep(cep):
        try:
            if len(cep) == 8:
                link = f'https://viacep.com.br/ws/{cep}/json/'
                requisicao = requests.get(link)
                dic_requisicao = requisicao.json()
                uf = dic_requisicao['uf']
                bairro = dic_requisicao['bairro']
                localidade = dic_requisicao['localidade']
                logradouro = dic_requisicao['logradouro']
                print(uf)
                print(bairro)
                print(localidade)
                print(logradouro)
            else:
                print('CEP invalido')
        except ValueError:
            print('CEP invalido')

