print("Tere tulemast!")
kool=input("\tMis koolis sa õpid?: ") #str kool
kursus=int(input("\tMis kursusel?: ")) #int kursus

print("Tere tulemast kooli"+kool.upper()+"!\n0le hea "+str(kursus)+".kuursuse õpilaseks!") #kool="TTHK"

print("Tere tulemast kooli",kool.lower(),"!\n0le hea ",kursus,".kuursuse õpilaseks!")

print("Tere tulemast kooli {0}!\n0le hea {1}.kuursuse õpetajaks!".format(kool,kursus))
print(type(kool))
print(type(kursus))
arv1=float(input("Arv 1: "))
arv2=float(input("Arv 2: "))
print("{0} + {1} = {2}".format(arv1,arv2,arv1+arv2)) #summa 
print("{0} - {1} = {2}".format(arv1,arv2,arv1-arv2)) #lahutamine
print("{0} * {1} = {2}".format(arv1,arv2,arv1*arv2)) #korrutis
print("{0} / {1} = {2}".format(arv1,arv2,arv1/arv2)) #jagamine
print("{0} astmes {1} = {2}".format(arv1,arv2,arv1**arv2)) #asendamine
print("{0} ja {1} jääk = {2}".format(arv1,arv2,arv1%arv2)) #jagamisjääk
print("{0} ja {1} jagamise täis osa {2}".format(arv1,arv2,arv1//arv2))

