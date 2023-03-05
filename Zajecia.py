
class Zajecia:
    def __init__(self) -> None:
        self.listaStudentow = []

    def zapiszStudenta(self, student, maxLiczbaStudentow =10):
        if len(self.listaStudentow)<maxLiczbaStudentow:
            self.listaStudentow.append(student)
    def liczbaStudentow(self):
        return len(self.listaStudentow)
    def studenci(self):
        return self.listaStudentow

if __name__=="__main__":
    zaj = Zajecia()
    for i in range(1,15):
        zaj.zapiszStudenta(f"student{i}")
    
    print(zaj.studenci())
    print(zaj.liczbaStudentow())