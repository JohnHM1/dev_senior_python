class SinglentonCreacionInstancia:

    _instancia = None
    
    @classmethod
    def __new__(cls, args,**kwargs ):
        

        if  not cls._instancia:
            cls._instancia = super(SinglentonCreacionInstancia).__new__(cls)
        return cls._instancia