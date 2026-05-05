dic = {'Nome': 'Julia', 'Idade': 21, 'Cidade': 'Curitiba'}
valor = dic.get('email') 
if valor is not None:
  print('A chave "email" existe e seu valor é:', valor) 
else:
  print('A chave "email" não existe.')
  