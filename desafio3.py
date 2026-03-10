faturamento = [1000, 2000, 0, 3000, 1500, 0, 4000, 2500]

menor = float('inf')
maior = float('-inf')
soma = 0
dias_validos = 0

for valor in faturamento:
    if valor > 0:  
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor
        
        soma += valor
        dias_validos += 1

media = soma / dias_validos

dias_acima_media = 0
for valor in faturamento:
    if valor > media:
        dias_acima_media += 1

print("Menor faturamento:", menor)
print("Maior faturamento:", maior)
print("Dias acima da média:", dias_acima_media)
