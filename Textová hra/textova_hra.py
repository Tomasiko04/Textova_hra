
import math
import random
from random import randint as nahoda
nahodne_cele_cislo=nahoda(0,10)

x=3
y=0
z=0
pocet_pokusu=0
pocet_kalkulacka=0

print("""Ocitli jste se v hořícím domě! Plameny zuří kolem vás a kouř vám ubírá viditelnost.
Musíte co nejrychleji najít cestu ven. Jakým směrem půjdete?""")


while x>y:                                                                              
    volba_1 = input(" Vyber si směr (doprava/doleva/rovně): ").lower()

    if volba_1 == "doprava":
         print("Našli jste okno, ale je příliš vysoko. Musíte zkusit jiný směr.") 
         

    elif volba_1 == "doleva":
         print("Vydali jste se doleva a dorazili jste do kuchyně. Vzduch je tu čistší, ale stále blízko u tebe hoří. Co budete dělat dál?")
         
        
         while x>y:           
            print(" 1. Hledat okno.")
            print(" 2. Hledat dveře.")
            print(" 3. Zkoušet hasit oheň v kuchyni.")

            volba_2 = input(" Zadej číslo možnosti (bez desetinné tečky): ")

            if volba_2 == "1":
                print("Žédné okno jste nenašli.\nZvolte jinou možnost.")
            elif volba_2 == "2":
                print("Našli jste zadní dveře s největší pravděpodobnistí ven, ale jsou zajištěné. Vedle nich si všimnete displeje s nápisem: Zadej náhodné čílso od 0 do 10 (máš jen 3 pukusy).")
                
                while x>pocet_pokusu:
                    
                    value=input(" Vaše myšlné číslo: ")
                    

                    try: #ověřování datového typu vstupu
                        zadane_c = int(value)
                        #print(f"Zadali jste celé číslo: {zadane_c}")
                        if zadane_c>=0 and zadane_c<=10:
                            if zadane_c == nahodne_cele_cislo:
                               
                                print("Blahopřeji, vstup povolen.")
                                print("Po vstupu do místnosti, zjišťuješ, že to nejsou dveře ven, ale do další místnosti") 
                                print("Na druhé straně vidíš mobilní telefon, bohužel ti cestu na druhou stranu blokuje mnoho překážek, které byly zasaženy ohněm.")
                                print("Co uděláš? Vrátíš se zpět do kuchyně nebo se pokusíš dostat rychle k telefonu a zavolat si pomoc.")
                                
                                while x>y:
                                    rozhodnuti=input(" Jaké je tvoje rozhodnutí (zpět/dál): ").lower()
                                    if rozhodnuti == "zpět":
                                            print("Jsi zpátky v kuchyni, nacházíš zde: ") 
                                            while x>y:
                                                
                                                print(" 1. Hrnec\n 2. Sekerku na maso\n 3. Ohnivzdorný rukáv")
                                                predmet=input(" Zadej číslo volby (bez desetinné tečky): ")  
                                                if predmet == "1":
                                                    print("Dobrá volba, hrnec naplníš vodou a zchladíš překážky zasažené ohněm a zavoláš si pomoc mobilním telefonem.")
                                                    y=4 
                                                    pocet_pokusu=3 
                                                elif predmet =="2":
                                                    print("Sekerkou na maso si odstrňaňuješ překážky, ale během toho tě zasáhnou planeny.")
                                                    y=3
                                                    pocet_pokusu=3
                                                elif predmet =="3":
                                                    print("Jakmile sis vzal ohnivzdorný rukáv, došlo ti, že to stačit nebude.")
                                                    while x>y:
                                                        
                                                        dalsi_vec=input(" Co si ještě vybereš hrnec/sekerku na maso?: ").lower()
                                                        if dalsi_vec=="hrnec":
                                                            print("Dobrá volba, hrnec naplníš vodou a zchladíš překážky zasažené ohněm a zavoláš si pomoc mobilním telefonem.")
                                                            y=4
                                                            pocet_pokusu=3
                                                        elif dalsi_vec=="sekerku":
                                                            print("Sekerkou na maso si odstrňaňuješ překážky, ale během toho tě zasáhnou planeny.")
                                                            y=3
                                                            pocet_pokusu=3
                                                        else:
                                                            print("Nerozumím tvé odpovědi. Zadej znovu.")
                                                else:
                                                    print("Nerozumím tvé odpovědi. Zadej znovu.")            
                                            


                                    elif rozhodnuti == "dál":
                                        print("Opravdu si věříš, během přecházení překážek z ničeho nic ztratíš rovnováhu a chytneš") 
                                        print("se oběma rukama rozžhavené železné trbky, protože máš spálené ruce nemůžeš si zavolat pomoc.")
                                        y=3
                                        pocet_pokusu=3
                                    else:
                                        print("Nerozumím tvé volbě. Zkus to znovu.")

                            else:
                                pocet_pokusu=pocet_pokusu+1 
                        else: 
                            print("Zadej celé číslo v rozmezí od 0 do 10.")

                    except ValueError:
                        # Pokud převod na int selže, zkusíme převést na desetinné číslo (float)
                        try:
                            zadane_c = float(value)
                            print(f"Zadali jste desetinné číslo: {zadane_c}. Zadejte pouze celé čílo od 0 do 10.")
                        except ValueError:
                            # Pokud ani převod na float nebyl úspěšný, předpokládáme, že se jedná o řetězec (str)
                            zadane_c = str(value)
                            if len(zadane_c) < 1:
                                print("Nic jste nezadali. Zkuste to znovu.")
                            else:
                                print(f"Zadali jste řetězec: {zadane_c}. Zadejte pouze celé čílo od 0 do 10.")

                    
                        
                          
                
                
                while x>y:
                    print("Na displeji se ti zobrazí nápis: Máš 2. šanci. Chceš ji využít?")
                    while x>y:
                        vyber_moznosti=input(" Zadej možnost (ano/ne): ").lower()
                        
                        if vyber_moznosti == "ano":
                                print("Jelikož majitel tohoto domu má velice rád matematiku, vypočítej objem válce, kde r=10 a v=3.")
                                print("Protože tato hodnota musí být přesná, zadáš tyto hodnoty do kalkulačky, kterou najdeš na stole.")
                                while x>pocet_kalkulacka:                            
                                    value_r = input(" Zadej hodnotu r: ")
                                    value_v = input(" Zadej hodnotu v: ")
                                    try:
                                        r = int(value_r)
                                        v = int(value_v)
                                        #print(f"První vstup je celé číslo: {r}")
                                        #print(f"Druhý vstup je celé číslo: {v}")
                                        kalkulacka=math.pi*math.pow(r,2)*v
                                        print(f"Výsledek na kalkulačce: {kalkulacka}")
                                        pocet_kalkulacka=pocet_kalkulacka+3

                                    except ValueError:
                                        
                                        try:
                                            r = float(value_r)
                                            v = float(value_v)
                                            print(f"Hodnotu r nebo hodnotu v jsi napsal jako řetězec nebo jako desetinné číslo. Zkus hodnotu zadat znovu jako celé číslo, které dosadíš podle výše uvedených hodnot.")
                                        
                                        except ValueError:
                                            r = str(value_r)
                                            v = str(value_v)
                                            if len(r) < 1:
                                                print("Nezadal jsi hodnotu r.")
                                            elif len(v) < 1:
                                                print("Nezadal jsi hodnotu v.")
                                            elif len(v) < 1 and len(r) < 1:
                                                print("Nezadal jsi hodnotu r a hodnotu v.")

                                            else:
                                                print(f"Hodnotu r nebo hodnotu v jsi napsal jako řetězec nebo jako desetinné číslo. Zkus hodnotu zadat znovu jako celé číslo, které dosadíš podle výše uvedených hodnot.")

                                while x>y:
                                    user_input = input(" Zadejte váš výsledek zaokrouhlený na celé číslo: ")
                                    try:
                                        výsledek = int(user_input)                            
                                        if výsledek == 942:
                                            
                                            print("Blahopřeji, vstup povolen.")
                                            print("Po vstupu do místnosti, zjišťuješ, že to nejsou dveře ven, ale do další místnosti.") 
                                            print("Na druhé straně vidíš mobilní telefon, bohužel ti cestu na druhou stranu blokuje mnoho překážek, které byly zasaženy ohněm.")
                                            print("Co uděláš? Vrátíš se zpět do kuchyně nebo se pokusíš dostat rychle k telefonu a zavolat si pomoc.")
                                            
                                            while x>y:
                                                rozhodnuti=input(" Jaké je tvoje rozhodnutí (zpět/dál): ").lower()
                                                if rozhodnuti == "zpět":
                                                        print("Jsi zpátky v kuchyni, nacházíš zde: ") 
                                                        while x>y:
                                                            
                                                            print(" 1. Hrnec\n 2. Sekerku na maso\n 3. Ohnivzdorný rukáv")
                                                            predmet=input(" Zadej číslo volby (bez desetinné tečky): ")  
                                                            if predmet == "1":
                                                                print("Dobrá volba, hrnec naplníš vodou a zchladíš překážky zasažené ohněm a zavoláš si pomoc mobilním telefonem.")
                                                                y=4 
                                                            elif predmet =="2":
                                                                print("Sekerkou na maso si odstrňaňuješ překážky, ale během toho tě zasáhnou planeny.")
                                                                y=3
                                                            elif predmet =="3":
                                                                print("Jakmile sis vzal ohnivzdorný rukáv, došlo ti, že to stačit nebude.")
                                                                while x>y:
                                                                    
                                                                    dalsi_vec=input(" Co si ještě vybereš hrnec/sekerku na maso?: ").lower()
                                                                    if dalsi_vec=="hrnec":
                                                                        print("Dobrá volba, hrnec naplníš vodou a zchladíš překážky zasažené ohněm a zavoláš si pomoc mobilním telefonem.")
                                                                        y=4
                                                                    elif dalsi_vec=="sekerku":
                                                                        print("Sekerkou na maso si odstrňaňuješ překážky, ale během toho tě zasáhnou planeny.")
                                                                        y=3
                                                                    else:
                                                                        print("Nerozumím tvé odpovědi. Zadej znovu.")
                                                            else:
                                                                print("Nerozumím tvé odpovědi. Zadej znovu.")            
                                                        
                                                elif rozhodnuti == "dál":
                                                    print("Opravdu si věříš, během přecházení překážek z ničeho nic ztratíš rovnováhu a chytneš") 
                                                    print("se oběma rukama rozžhavené železné trbky, protože máš spálené ruce nemůžeš si zavolat pomoc.")
                                                    y=3
                                                else:
                                                    print("Nerozumím tvé volbě. Zkus to znovu.")
                                        else:
                                            print("Vstup zamítnut.")
                                            print("Jelikož si zadal špatný výsledek, displej se vypnul. Chceš se vrátit zpět, ale dveřmi, kterými si přišel do kuchyně začaly hořet. ")
                                            y=3
                                            
                                    except ValueError:
                                    # Pokud převod na int selže, zkusíme převést na desetinné číslo (float)
                                        try:
                                            výsledek = float(user_input)
                                            print(f"Zadali jste desetinné číslo: {výsledek}")
                                        except ValueError:
                                            # Pokud ani převod na float nebyl úspěšný, předpokládáme, že se jedná o řetězec (str)
                                            výsledek = str(user_input)
                                            
                                            if len(výsledek) < 1:
                                                print("Nezadal jsi hodnotu.")
                                            else:
                                                print(f"Zadali jste řetězec: {výsledek}")


                        elif vyber_moznosti == "ne":
                            print(f"Jelikož si zadal {vyber_moznosti}, displej se vypnul. Chceš se vrátit zpět, ale dveřmi, kterými si přišel do kuchyně, začaly hořet.")
                            y=3
                        else:
                            print("Nerozumím tvé volbě. Zkus to znovu.")
                     
            elif volba_2 == "3":
                print("Pokusili jste se hasit oheň, ale nemáte dostatečné vybavení. Plameny se šíří rychleji.")
                print("Musíte najít jiný způsob, jak uniknout.")
            else:
                print("Nerozumím tvé volbě. Zkus to znovu.")
        
    elif volba_1 == "rovně":
        print("Rozběhli jste se kupředu a dorazili jste do obývacího pokoje. Jelikož plameny natolik postihly obývací pokoj, že odtud není žádná cesta zpět, vracíte se zpět.")
        print("Musíte zkusit jiný směr.")
    else:
        print("Nerozumím tvé volbě. Zkus to znovu.")

if y ==4:
    print("GRATULUJI, přežil jsi. :)))")
else:
    print("Umíráš v plamenech. :(((")
