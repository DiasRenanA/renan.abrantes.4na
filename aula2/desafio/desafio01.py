# Dados: no eixo y temos a quantidade de guarda-chuvas vendidos em um dia de chuva e no eixo x temos a quantidade de horas que chuve em um dia

x_horasChuvas = [10, 20, 30, 40, 50, 60, 70, 80]
y_qtdGuardaChuva = [15, 30, 45, 50, 65, 75, 85, 100]

# Aqui vamos coletar a quantidade de alementos em x
qtd = len(x_horasChuvas)

# Aqui vamos realizar a somatoria necessaria para calcular coeficientes
soma_x = sum(x_horasChuvas)
soma_y = sum(y_qtdGuardaChuva)
soma_x2 = sum(x**2 for x in x_horasChuvas)
soma_xy = sum(x*y for x, y in zip(x_horasChuvas, y_qtdGuardaChuva))

# Calculando os coeficientes
a = (qtd * soma_xy - soma_x * soma_y) / (qtd * soma_x2 - soma_x**2)
b = (soma_y - a * soma_x) / qtd

# Exibindo os coeficientes
print(f'Coeficiente a: {a}')
print(f'Coeficiente b: {b}')

print(f"A equação da regressão linear é: y = {a:.2f}x + {b:.2f}")

# Fazer uma previsão para 55 clientes
horas_novas = 55
previsao = a * horas_novas + b
print(f"Se chover por {horas_novas} horas, a previsão de guarda-chuvas vendidos é {previsao:.2f}")
