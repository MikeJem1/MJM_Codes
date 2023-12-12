
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def navigation():
    print("ki direksyon wap pran a dwat '>' oubyn a goch '<' ")
    direksyon=input("dwat >, goch <")

    endis=input("nan ki let wap pozisyone")
    endis=endis.upper()

    numewo=alphabet.index(endis)
    pas=int(input("konbyen wap mache :" ))

    if direksyon=='<':

        nimweNewElaman=(numewo - pas) % len(alphabet)
        neweleman=alphabet[nimweNewElaman]
    elif direksyon=='>':

        nimweNewElaman=(numewo + pas) % len(alphabet)
        neweleman=alphabet[nimweNewElaman]
    else:
         print("ou sipoze mete < oubyn <")
    print(neweleman )
   

def ekriyonmo():
    

    kantiteLet = int(input("Konbyen lèt mo ou vle ekri a genyen? "))
    i = 0
    lis = []

    while i < kantiteLet:
        print("Ki direksyon wap pran: dwat '>' ou goch '<'")
        direksyon = input("dwat >, goch <: ")

        endis = input("Nan ki lèt wap pozisyone: ")
        endis = endis.upper()

        numewo = alphabet.index(endis)

        pas = int(input("Konbyen wap mache: "))
        
        if direksyon == '<':
                nimweNewElaman = (numewo - pas) % len(alphabet)
                neweleman = alphabet[nimweNewElaman]
        elif direksyon == '>':
                nimweNewElaman = (numewo + pas) % len(alphabet)
                neweleman = alphabet[nimweNewElaman]
        else:
            print("ou sipoze mete < oubyn <")
        i += 1
        lis.append(neweleman)

    print("Mo a se :", "".join(lis))


def main():
     print("******************************************")
     print("*************JWET MO**********************")
     print("******************************************")
     chwa=0
     while chwa !='1' and chwa !='2':
        print("Chwazi 1 pou'w teste jwet la....")
        print("chwazi 2 pou'w ka ekri yon mo")
        chwa=input("ki chwa'w")
    
     if chwa=='1':
          navigation()
     elif chwa=='2':
          ekriyonmo()


main()

     


     



