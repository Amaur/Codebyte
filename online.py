import sys
import urllib.request,json

req = urllib.request.Request("http://www.developers.agenciaideias.com.br/loterias/loteriafederal/json")
response = urllib.request.urlopen(req)
t= response.read().decode()
obj= json.loads(t)

#str_response = test.readall().decode('utf-8')
#obj = json.loads(str_response)
#print(obj)
print('Local: ',obj['concurso']['local'])
print('Concurso num: ',obj['concurso']['numero'])
print('data: ',obj['concurso']['data'])
print('Cidade: ',obj['concurso']['cidade'])
print('Premio 1: ',obj['concurso']['premiacao']['premio_1']['valor_pago'])
print('Bilhete: ',obj['concurso']['premiacao']['premio_1']['bilhete'])
print('Premio 2: ',obj['concurso']['premiacao']['premio_2']['valor_pago'])
print('Bilhete: ',obj['concurso']['premiacao']['premio_2']['bilhete'])
print('Premio 3: ',obj['concurso']['premiacao']['premio_3']['valor_pago'])
print('Bilhete: ',obj['concurso']['premiacao']['premio_3']['bilhete'])
print('Premio 4: ',obj['concurso']['premiacao']['premio_4']['valor_pago'])
print('Bilhete: ',obj['concurso']['premiacao']['premio_4']['bilhete'])
print('Premio 5: ',obj['concurso']['premiacao']['premio_5']['valor_pago'])
print('Bilhete: ',obj['concurso']['premiacao']['premio_5']['bilhete'])

print('Cidade do ganhador: ',obj['concurso']['cidade_1_premio'])


