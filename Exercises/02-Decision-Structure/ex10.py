# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino 
#ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
#"Valor Inválido!", conforme o caso.

# receve value
# recebendo valor
period = input("Enter with value M for matutine V to vespertine or N to night: \n").strip(" ").upper()
# compare value
# comparando valor
if period == "M":
	# In case the value was M
	# no caso do valor ser M
	print("Period Morning")

elif period == "V":
	# In case the value was V
	# no caso do valor ser M
	print("Period Afternon")

elif period == "N":
	# In case the value was N
	# no caso do valor ser M
	print("Period Night")
else:
	# In case the value was any preview value
	# no caso do valor nao ser nenhum valor anterior
	print("Incorrect Value")
