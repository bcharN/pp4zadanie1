

def appendToFile(file:str, line:str):
    with open(file,"at") as f:
        f.write(line)


if __name__=="__main__":
    appendToFile("testfile1.txt", "abc")
    appendToFile("testfile1.txt", "def")
    with open("testfile1.txt","rt") as f:
        print(f.read())
