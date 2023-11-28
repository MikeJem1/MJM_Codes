print("***************************************")
print("******PROJE KALKILATRIS****************")
print("***************************************")

LisNot=[]
ValeNot=input("rantre note :")
ValeNot2=int(ValeNot)
i=0

while i<ValeNot2:
    note=int(input("rantre note ou yo :"))
    LisNot.append(note)
    i+=1
    
#kalkile mwayen elev la

mwayen=sum(LisNot)/len(LisNot)

print(mwayen)

# nou pral klase etidyan yo selon rezilta yo

if mwayen>=90:
    print(f"mwayen nan se :{mwayen} li fe yon :A")
elif mwayen>=80:
    print(f"mwayen nan se :{mwayen} li fe yon :B")
elif mwayen>=70:
    print(f"mwayen nan se :{mwayen} li fe yon :C")
elif mwayen>=60:
    print(f"mwayen nan se :{mwayen} li fe yon :D")
else:
    print(f"mwayen nan se :{mwayen} li fe yon :F")



