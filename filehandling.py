#basic file handling

f=open("myfirstfile.txt","w")
x="nandini joshi"
f.write(x)
y="cheshta khu"
f.write("\n"+y)
f.close()

f=open("myfirstfile.txt","r")
y=f.read()
print(y)
f.close()
