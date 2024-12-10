f = open(".ipynb_checkpoints/prisoner.html", "r")
lines = f.readlines() 
f.close()
newList = []

for l in lines:
    newList.append("\\" + l[:len(l)-1] + "\\n\\\n")

f = open("project/fixedHTML.html", "a") 
f.writelines(newList)