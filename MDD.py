from datetime import datetime
loop = 1
def Input(Extra):
    promt = "MDD:/"
    if Extra != "": promt = "MDD:/", Extra
    promt = str(promt)
    promt = promt.replace("'","").replace("(","").replace(")","").replace(",","").replace(" ","")
    return input(promt)

I1 = Input("")

if I1 != 'exit':
    now = datetime.now()
    now = now.replace(second=0, microsecond=0)
    now = str(now)
    now = now.replace(":","_")
    name = now + ".txt"
    f = open(name,"a")
    print(name, "was created")
    while loop == 1:
        I2 = Input(":</p>")
        if I2 == 'exit': loop = 0
        if I2 != 'exit': 
            f.write("\n")
            f.write(I2)
f.close
