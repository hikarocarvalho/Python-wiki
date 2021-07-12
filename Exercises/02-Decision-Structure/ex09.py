# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# declare all variables
# declarada todas as variaveis
first_number = float(input("Enter with the first number"))
second_number = float(input("Enter with the second number"))
third_number = float(input("Enter with the third number"))
ordered = ""
# compare all values
# compando todos valores
if first_number <second_number and first_number < third_number:
	ordered += str(first_number)
	if second_number < third_number:
		ordered += second_number
		ordered += third_number
	else
		ordered += third_number
		ordered += second_number
elif second_number < third_number:
	ordered += second_number
	ordered += third_number
	ordered += first_number
else: 
	orddered += third_number
	ordered += second_number
	ordered += first_number
# Show the ordered values
# mostra valores ordenados

print(ordered)