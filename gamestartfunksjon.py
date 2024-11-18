spiltfør = 0

def spiltFør():
    global spiltfør
    spiltfør = str(input("Kan du reglene for rafle? (Svar ja/nei) "))
    kanReglene()
    
def kanReglene():
    if spiltfør == "nei":
        print("\n------------Rafle Regler-------------\n\nMÅLET MED SPILLET:\n"
              "For å vinne i rafle må du være den siste personen som har igjen terninger. "
              "Hver spiller starter med 5 terninger og for hver runde mister taperen en terning."
              "\n\nSPILLETS GANG:\nHver runde så tipper hver spiller på antallet det "
              "vil være av en spesifikk terning. F.eks kan en spiller tippe at det er 5 3ere. "
              "Neste spiller kan da enten si at de ikke tror på hva den tidligere spilleren bydde "
              "eller så kan han høyne. For å høyne så må du tippe enten et høyere antall terninger"
              " som f.eks 6 2ere eller så kan du tippe samme antall av en større terning f.eks "
              "5 4ere.\n\nEKSEMPEL:\nHvis vi tar for oss en runde med Spiller 1 og Spiller 2 så "
              "fortsetter runden helt til en av spillerene ikke tror på det en annen spiller bøy."
              " F.eks så kan Spiller 1 ha bydd 5 6ere og Spiller 2 tror ikke på han. Da sjekkes alle sine "
              "terninger og hvis det er 5 eller flere 6ere totalt så mister Spiller 2 en terning fordi "
              "han trodde feil, men hvis det er færre enn 5 6ere vil Spiller 1 miste en terning fordi han trodde feil“\n\n"
              "VIKTIG:\n1ere er jokere og vil telle som alle typer terninger. Det vil si at når "
              "du teller f.eks antall 4ere så teller du antall 4ere og legger til antall 1ere "
              "og summen av det vil bli antall 4ere. Dette gjelder altså for alle terningtyper."
              " På grunn av dette er det ikke tillat å tippe på antall 1ere siden det vil bli "
              "to ganger så få 1ere som alle andre terninger.\n\nOPPSUMERING:\nHver runde går ved at "
              "når en spiller har sin tur kan han enten høyne eller ikke tro på den tidligere spilleren. "
              "Runden forstetter helt til noen ikke blir trodd på. Da telles terningene. Den spilleren "
              "som trodde feil mister en terning og så starter neste runde. Spilleren som har igjen "
              "terninger når de andre er tomme vinner.\n\n-----------------------------------"
              "\nNB: Bla opp for å lese alle reglene\n-----------------------------------\n\n\n"
              )
        spiltFør()
    elif spiltfør == "ja":
        print("Start")
    else:
        print("\nDet du skrev inn ble ikke akseptert. Venligst Svar ja eller nei.")
        spiltFør()
    

def gamestart():
    print("HEi velkommen til Rafle!")
    spiltFør()
    
    

gamestart()