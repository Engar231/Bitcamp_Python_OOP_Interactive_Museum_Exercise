
'''
Ragazzi, oggi vi propongo una sfida a tappe. 
Non un semplice esercizio. Ma un viaggio. 
Faremo un progetto in Python che crescerà insieme a voi, minuto dopo minuto, passo dopo passo, 
come una costruzione LEGO. Partiremo da un’idea semplice, e la faremo evolvere fino a ottenere 
un'applicazione completa, con classi intelligenti, una GUI, un database e persino la possibilità che il 
programma… parli! 

L’idea di fondo 
Immaginate di voler creare un Museo Interattivo digitale. Un’applicazione in cui ogni opera d’arte 
non è solo un'informazione, ma un oggetto che può parlare, reagire, interagire. Le opere saranno 
classificate, salvate su file json, visualizzate in un’interfaccia, e, se tutto va come deve… presentate 
con una voce digitale! 

Per arrivarci non useremo bacchette magiche, ma i principi cardine della programmazione 
orientata agli oggetti, e un bel po’ di skill concrete. 
Come lavoreremo? 

Vi passerò, uno alla volta, uno dei seguenti argomenti: 

 Partiremo con l’astrazione: cosa significa modellare una classe? Cos’è un oggetto? 
Cominceremo con una semplice OperaDArte. 

 Passeremo all’incapsulamento: impareremo a proteggere i dati, a controllare l’accesso agli 
attributi. 

 Poi esploreremo l’ereditarietà: un quadro, una scultura, un’installazione… hanno cose in 
comune, ma anche comportamenti unici. Qui arriverà anche il polimorfismo: lo stesso 
metodo, comportamenti diversi. 

 Introdurremo anche le interfacce astratte: quando voglio obbligare tutte le opere ad avere 
certi metodi fondamentali. 

 Scopriremo i decoratori, creando delle funzioni che aggiungono comportamento in modo 
“magico”. 

 Salveremo e caricheremo tutto in JSON, per rendere gli oggetti persistenti. Come se ogni 
opera avesse un bigliettino da viaggio. 

 E quando avremo contenuti… li mostreremo in una vera interfaccia grafica con tkinter. 
Un’app dove clicchi su un’opera e vedi tutti i dettagli. 

 E infine, come colpo di scena, integreremo una voce digitale. Ogni opera potrà raccontarsi da 
sola. Proprio così: useremo una libreria di sintesi vocale per far “parlare” Python. 

L’obiettivo 
Voglio che vi divertiate a costruire qualcosa di completo, in cui ogni pezzo serve al progetto finale. 
Alla fine, sarà chiaro che tutti questi concetti — OOP, JSON, GUI — non sono argomenti separati, 
ma strumenti che lavorano insieme, come una squadra. 
Siete pronti? 
Iniziamo con una semplice opera d’arte, che si chiama… OperaDArte… E vediamo dove ci porta.

🧬 FASE 3 – Ereditarietà: quando un'opera prende vita
"Ragazzi, fino adesso abbiamo creato una classe OperaDArte abbastanza generica.
Ma nella realtà ci sono opere molto diverse: un dipinto ha caratteristiche specifiche, così come una scultura o un’installazione multimediale.
Non possiamo trattarle tutte allo stesso modo, ma non vogliamo nemmeno riscrivere da capo tutto ogni volta.
Qui entra in gioco l’ereditarietà!"

📌 Cosa vi chiedo di fare in questa fase
In questa fase dovrete creare nuove classi che rappresentano tipi specifici di opere.
Queste classi devono ereditare dalla classe OperaDArte, cioè estenderla con nuove caratteristiche.

Ad esempio:
-Una classe Dipinto che ha in più l’attributo tecnica (olio su tela, acrilico, tempera…)
-Una classe Scultura che aggiunge materiale (marmo, bronzo, ferro…)
-Una classe InstallazioneMultimediale con attributi come formato_video, interattiva, ecc.

✏️ Linea guida
Create tre sottoclassi: Dipinto, Scultura, InstallazioneMultimediale.
Ogni sottoclasse deve:

-Ereditare da OperaDArte
-Aggiungere almeno uno o due attributi nuovi
-Sovrascrivere il metodo descrizione() per includere anche le nuove info

Fate almeno un esempio per ciascuna classe, poi stampate la descrizione.
'''

from abc import ABC, abstractmethod 
from OperaDarte_Fase5ABC import OperaDarte
#Fase 4 aggiunta della Polimorph, vedere altro file.ì

class Dipinto(OperaDarte):
    def __init__(self,titolo, autore, anno, tecnica):
        super().__init__(titolo,autore,anno,"Dipinto") #l'attributo tipo non serve, essendo Dipinto la classe
    #tra "" tipo verrà rimosso e messo dipinto e nella classe sopra mettiamo Tecnica
        self.tecnica=tecnica
    
    def info_base(self):
        return f"{self.titolo} di {self.autore}, realizzato nel {self.anno}"

    def descrizione(self):
        return f"{self.info_base()} con la tecnica {self.tecnica}"
    
    def __str__(self):
        return self.descrizione()

    
    def esegui_interazione(self):
        return "Possiamo ammirare il Dipinto"


class Scultura(OperaDarte):
    def __init__(self,titolo, autore, anno,materiale, altezzacm):
        super().__init__(titolo,autore,anno,"Scultura") #l'attributo tipo non serve, essendo Dipinto la classe
    #tra "" tipo verrà rimosso e messo dipinto e nella classe sopra mettiamo Tecnica
        self.materiale=materiale
        self.altezzacm=altezzacm

    def info_base(self):
        return f"{self.titolo} di {self.autore}, realizzato nel {self.anno}"

    def descrizione(self):
        return f"{self.info_base()} con materiali {self.materiale} ed alta {self.altezzacm}"
    
    def __str__(self):
        return self.descrizione()
    
    def esegui_interazione(self):
        return "Alzate lo sguardo e fatevi illuminare dalle nostre sculture!"
    
class InstallazioneMultimediale(OperaDarte):
    def __init__(self,titolo, autore, anno, formatovideo, interattiva):
        super().__init__(titolo,autore,anno,"InstallazioneMultimediale") #l'attributo tipo non serve, essendo Dipinto la classe
    #tra "" tipo verrà rimosso e messo dipinto e nella classe sopra mettiamo Tecnica
        self.formatovideo= formatovideo
        self.interattiva=interattiva
    
    def info_base(self):
        return f"{self.titolo} di {self.autore}, realizzato nel {self.anno}"

    def descrizione(self):
        inter="interattiva" if self.interattiva else "non interattiva"
        return f"L'Installazione Multimediale è {inter} con un formato video di {self.formatovideo}"
    
    def __str__(self):
        return self.descrizione()
    
    def esegui_interazione(self):
        return "Immergetevi nell'esperienza sensoriale"

# opera1 = Dipinto("La Gioconda", "Leonardo da Vinci", 1503, "Olio su Tavola")
# print(opera1.descrizione())
# opera2 = Scultura("David", "Michelangelo", 1504,"Marmo", 200)
# opera3 = Scultura("Il Pensatore", "Rodin", 1904, "Bronzo", 180)
# print(opera2.descrizione())
# print(opera3.descrizione())
# opera4=InstallazioneMultimediale("Rain Room", "Random International", 2012, "Full HD", True)
# print(opera4.descrizione())
#CTRL ù per hackerare tutto.

opere=[Dipinto("La Gioconda", "Leonardo da Vinci", 1503, "Olio su Tavola"),
    Scultura("David", "Michelangelo", 1504,"Marmo", 200),
    Scultura("Il Pensatore", "Rodin", 1904, "Bronzo", 180),
    InstallazioneMultimediale("Rain Room", "Random International", 2012, "Full HD", True)
            ]
for opera in opere:
    print(opera)
    print(opera.esegui_interazione())