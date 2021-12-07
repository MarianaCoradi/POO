

class Cliente:

   def __init__(self, nome):
       self.__nome = nome

# O @property faz com que pareça q estou acessando diretamente o atributo, porém ele chama o método com o mesmo nome do atributo
#para getter:
   @property
   def nome(self):
       print("Chamndo @property nome()")
       return self.__nome.title()

   @nome.setter
   def nome(self, nome):
       print("Chamndo setter nome()")
       self.__nome = nome
