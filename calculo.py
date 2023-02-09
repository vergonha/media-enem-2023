class ENEM:
    """
    Calcula sua média do ENEM baseada nas suas notas 
    (disponíveis no site do INEP desde 09/02/2023).

    => Utiliza as seguintes referências:
    - Linguagens: Peso 2.
    - Humanas: Peso 1.
    - Natureza: Peso 3.
    - Matemática: Peso 2.
    - Redação: Peso 1.
    
    Tanto sua média quanto os pesos podem variar dependendo da faculdade que escolher, 
    pois a maneira que as matérias são valorizadas variam conforme o curso desejado. 
    Ex: Ciências da Computação geralmente valoriza mais Matemática.
    """
    def __init__(self, linguagem: float, humanas: float, 
                        natureza: float, matematica: float, 
                        redacao: float) -> float:

        self.pesos = {

            "linguagem": 2,
            "humanas": 1,
            "natureza": 3,
            "matematica": 2,
            "redacao": 1
        }

        self.linguagem = linguagem
        self.humanas = humanas
        self.natureza = natureza
        self.matematica = matematica
        self.redacao = redacao

    def media(self):
        """ Função que calcula a sua média. """
        self.linguagem *= self.pesos['linguagem']
        self.humanas *= self.pesos['humanas']
        self.natureza *= self.pesos['natureza']
        self.matematica *= self.pesos['matematica']
        self.redacao *= self.pesos['redacao']

        peso_total = sum(self.pesos.values()) #A soma de todos os pesos.
        nota_total = self.linguagem + self.humanas + self.natureza + self.matematica + self.redacao
        media = nota_total/peso_total
        
        return round(media, 1) #Arredonda para manter o padrão de apenas 1 casa decimal.