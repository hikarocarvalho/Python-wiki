# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
# contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste 
# segundo o seguinte critérios, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
# ---------------------------------------------------#
# declare variables
# declara variaveis
salary = float(input("Enter with your salary value: \n"))
# verify with conditions
# verifica condições
if salary <= 280:
	print(f'The initial value is: {salary} and apply with 20%')
	print(f'The value result from 20% is: {(salary*0.20):.2f}')
	print(f'The final value is: {((salary*0.20)+salary):.2f}')
elif salary <= 700 and salary > 280:
	print(f'The initial value is: {salary} and apply with 15%')
	print(f'The value result from 15% is: {(salary*0.15):.2f}')
	print(f'The final value is: {((salary*0.15)+salary):.2f}')
elif salary < 1500 and salary > 700:
	print(f'The initial value is: {salary} and apply with 10%')
	print(f'The value result from 10% is: {(salary*0.10):.2f}')
	print(f'The final value is: {((salary*0.10)+salary)}')
else:
	print(f'The initial value is: {salary} and apply with 5%')
	print(f'The value result from 5% is: {(salary*0.05):.2f}')
	print(f'The final value is: {((salary*0.05)+salary):.2f}')