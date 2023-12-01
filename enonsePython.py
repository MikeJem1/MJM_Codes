
#*************exo1******************
#nou pral chnje let yo an miniskil
FrazExo1="MWEN VLE GENYN "
fraz2=FrazExo1.lower() # pou chanje let yo an miniskil
print(fraz2)

#*************exo2******************

Frazexo2 = "Rantre yon fraz: "
fraz3 = Frazexo2.split(' ') # pou retire espas

print("Liste Eleman:", fraz3)#nouvo lis avek chak eleman apa

#******************exo3***************
#mwen pral chanje premye let l an majiskil
frazexo4="maignan est un type bien"
newfrazexo4=frazexo4.title()
print(newfrazexo4)


#******************exo4****************
#nou pral idantifye premye let nan chak mo
frazexo5="Anana Yol Isi Teren Itil"
newmo=[mo[0] for mo in frazexo5.split()]
newmoexo5="".join(newmo)
print(newmoexo5)

#*****************exo5****************
# nou pral ranplase tout "a" nan yon mo pa @
moexo6="Anana sa trop dous"
newmoexo6=moexo6.replace('a','@')
print(newmoexo6)

#***************exo 6*****************
#nou pral vire mo a devan deye
moexo7="Canada"
newmoexo7=moexo7[1:] + moexo7[0]
print(newmoexo7.upper())

#*********************exo 7***************
#nou pral chache endeks premye let nan chenn karakte "a"
frazexo8=" Anana sa pa bon tande"
endeks_la=frazexo8.find('a')
print(f"endeks premye 'a' se '{endeks_la}':")


#***************exo8************************
#nou pral afiche total endeks 'a' 
frazexo8=" Anana sa pa bon tande"
#nou itilize bouk pou nou pakouri chenn nan poul enumere chak kote linjwen 'a' yo
chanjman=[index for index, let in enumerate(frazexo8) if let=='a']
total=sum(chanjman)
print(f"total la se:{total}")

#***********************exo9****************************************
frazexo8=" Anana sa pa bon tande"
#nou itilize bouk pou nou pakouri chenn nan poul enumere chak kote linjwen 'a' yo
chanjman=[index for index, let in enumerate(frazexo8) if let=='a']
lis_endeks=chanjman
print(lis_endeks)


#*****************exo10*******************
frazexo10="fok nou leve bone si nou vle chanpyon"
newfrazexo10=frazexo10.replace(' ','')

print(newfrazexo10)