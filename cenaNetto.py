

def cenaNetto(cenaBrutto:int, stawkaPodatku:float):
    if stawkaPodatku != -1:
        return cenaBrutto/(1+stawkaPodatku)
    else: raise ZeroDivisionError

