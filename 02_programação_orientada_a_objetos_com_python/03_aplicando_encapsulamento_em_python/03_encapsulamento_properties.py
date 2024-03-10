# Para que servem?

## Com o property() do Python, você
## pode criar atributos gerenciados
## em suas classes. Vocẽ pode usar
## atributos gerenciados, também 
## conhecidos como propriedades,
## quando precisar modificar sua
## implementação interna sem
## alterar a API pública da classe.

### Exemplo

class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self.x or 0
    
    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
    
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)