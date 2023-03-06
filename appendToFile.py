

def appendToFile(file:str, line:str):
    with open(file,"at") as f:
        f.write(line)



