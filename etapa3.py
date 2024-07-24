class Restaurante:
    def __init__(self, nome, tipo_cozinha):
        self.nome = nome  # Atributo público
        self._tipo_cozinha = tipo_cozinha  # Atributo protegido
        self.__clientes = 0  # Atributo privado
    
    def adicionar_cliente(self):
        self.__clientes += 1
    
    def remover_cliente(self):
        if self.__clientes > 0:
            self.__clientes -= 1
    
    def get_clientes(self):
        return self.__clientes

    def set_clientes(self, numero):
        if numero >= 0:
            self.__clientes = numero
        else:
            print("O número de clientes não pode ser negativo.")
    
    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Tipo de Cozinha: {self._tipo_cozinha}, Clientes: {self.get_clientes()}"
    
class RestauranteItaliano(Restaurante):
    def __init__(self, nome):
        super().__init__(nome, "Italiana")
        self.pratos_especiais = ["Pizza", "Pasta"]  # Atributo público
    
    def adicionar_prato_especial(self, prato):
        self.pratos_especiais.append(prato)
    
    def exibir_informacoes(self):
        info_base = super().exibir_informacoes()
        pratos = ", ".join(self.pratos_especiais)
        return f"{info_base}, Pratos Especiais: {pratos}"
    
class RestauranteJapones(Restaurante):
    def __init__(self, nome):
        super().__init__(nome, "Japonesa")
        self._pratos_especiais = ["Sushi", "Tempura"]  # Atributo protegido
    
    def adicionar_prato_especial(self, prato):
        self._pratos_especiais.append(prato)
    
    def get_pratos_especiais(self):
        return self._pratos_especiais
    
    def exibir_informacoes(self):
        info_base = super().exibir_informacoes()
        pratos = ", ".join(self._pratos_especiais)
        return f"{info_base}, Pratos Especiais: {pratos}"

rest_italiano = RestauranteItaliano("La Bella Italia")
print(rest_italiano.exibir_informacoes())

rest_italiano.adicionar_cliente()
rest_italiano.adicionar_prato_especial("Risoto")
print(rest_italiano.exibir_informacoes())

rest_japones = RestauranteJapones("Sushi Master")
print(rest_japones.exibir_informacoes())

rest_japones.adicionar_cliente()
rest_japones.adicionar_cliente()
rest_japones.remover_cliente()
rest_japones.adicionar_prato_especial("Ramen")
print(rest_japones.exibir_informacoes())

rest_japones.set_clientes(10)
print(rest_japones.get_clientes())

print(rest_japones._pratos_especiais)