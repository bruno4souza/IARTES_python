from abc import ABC, abstractmethod

class Smartphone(ABC):
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def set_ano(self, ano):
        self.ano = ano

    def get_ano(self):
        return self.ano
    """
    @abstractmethod
    def tirarfoto(self):
        pass

    @abstractmethod
    def liga(self, estado):
        pass

    @abstractmethod
    def desliga(self):
        pass
   
 """
class Samsung(Smartphone):
    #@abstractmethod
    #def logarAndroid(self):
        pass

class Iphone(Smartphone):
   @abstractmethod
   def logarIOS(self):
       pass

class Samsungfold(Samsung):
    def dobrar(self):
        modelo = Samsung.get_modelo()
        if(modelo == "Fold"):
            return True
        else:
            return False

#class Samsunggalaxy(Samsung):


#class Iphone14(Iphone):


#class Iphone14plus(Iphone):
