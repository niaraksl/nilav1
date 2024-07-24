from etapa3 import Restaurante, RestauranteItaliano, RestauranteJapones

rest_italiano = RestauranteItaliano("La Bella Italia")
rest_italiano.adicionar_cliente()
rest_italiano.adicionar_prato_especial("Risoto")

print()
rest_japones = RestauranteJapones("Sushi Master")
rest_japones.adicionar_cliente()
rest_japones.adicionar_cliente()
rest_japones.remover_cliente()
rest_japones.adicionar_prato_especial("Ramen")
rest_japones.set_clientes(10)

print()
print("Pratos especiais do restaurante japonês:", rest_japones.get_pratos_especiais())