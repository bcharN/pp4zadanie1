

def cenaNetto(cenaBrutto:int, stawkaPodatku:float):
    if stawkaPodatku != -1:
        return cenaBrutto/(1+stawkaPodatku)
    else: raise ZeroDivisionError


if __name__=="__main__":
    cenaBRUTTO = int(input("podaj wartosc ceny brutto: "))
    stawkaPodatku = float(input("podaj stawke podatku jako ulamek dziesietny: "))
    print(f"wartosc ceny NETTO to: {cenaNetto(cenaBRUTTO, stawkaPodatku)}")