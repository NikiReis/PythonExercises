from datetime import datetime
data = datetime.now().year
dados = dict()
finaldata = []

dados['Nome'] = str(input("Digite o nome do trabalhador: "))
nascimento = int(input("Digite o seu ano de nascimento: "))
dados['Idade'] = data - nascimento
dados['CTPS'] = int(input("Digite a sua CTPS (Digite 0 para caso não tenha uma): "))
if dados['CTPS'] != 0:
    dados['Contrato'] = int(input("Digite o ano de contratação do atual serviço: "))
    dados['Salário'] = int(input("Digite o seu salário: "))
    dados['Anos trabalhados'] = int(input("Digite quantos anos trabalhados você\ntem com excessão do emprego atual: "))
    dados['Sexo'] = str(input("Digite seu sexo F para feminino e M para masculino: ")).upper()
    if dados['Sexo'] == 'F':
        dados['Aposentadoria Por Tempo de Trabalho'] = (30 - (dados['Anos trabalhados'] + (data - dados['Contrato'])))
    else:
        dados['Aposentadoria Por Tempo de Trabalho'] = (35 - (dados['Anos trabalhados'] + (data - dados['Contrato'])))
    if dados['Sexo'] == 'F':
        dados['Aposentadori por Idade'] = (62 - dados['Idade'])
    else:
        dados['Aposentadori por Idade'] = (65 - dados['Idade'])
print()
for k,v in dados.items():
    print(f"O/A {k} do indivíduo é: {v}")
