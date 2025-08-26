nome = input("Digite o seu nome:")
nota1 = float(input("Digite primeira nota"))
peso1 = float(input("Digite o peso da nota"))

nota2 = float(input("Digite segunda nota" ))
peso2 = float(input("Digite o peso da nota"))

nota3 = float(input("Digite terceita nota"))
peso3 = float(input("Digite o peso da nota"))
      
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 ) / (peso1 + peso2 + peso3)

print(f"A média ponderadas das notas é:{media:.2f}")