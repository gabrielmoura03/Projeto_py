CUSTO_FAB = float(input("digite o valor do carro na fábrica: R$"))

PORCENT_DISTRIBUIDOR = 0.12 * CUSTO_FAB
IMPOSTO = 0.3 * CUSTO_FAB

Custo_final = CUSTO_FAB + PORCENT_DISTRIBUIDOR + IMPOSTO


print(f"\nCusto da fábrica: R${CUSTO_FAB:.2f}")
print(f"Custo da distribuidora: R${PORCENT_DISTRIBUIDOR:.2f}")
print(f"Custo do imposto: R${IMPOSTO:.2f}")
print(f"Valor final do veículo: R${Custo_final:.2f}")