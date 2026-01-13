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

Fase 4: Il polimorfismo – Quando l'arte si fa camaleontica 🌀🎨

Ragazzi, eccoci a uno dei concetti più eleganti e – lasciatemelo dire – poetici della programmazione a oggetti: il polimorfismo.
Il termine viene dal greco "poli" (molti) e "morphé" (forme): cioè, un’unica interfaccia, tanti comportamenti. Come dire… una stessa parola detta da un pittore, uno scultore e un performer non suona mai allo stesso modo.
Ecco cosa voglio farvi notare: tutte le nostre classi (Dipinto, Scultura, InstallazioneMultimediale) derivano da OperaDArte, e tutte sovrascrivono il metodo descrizione().
Questo significa che possiamo trattare queste istanze come se fossero dello stesso tipo (una lista generica di opere), ma ognuna di loro si comporterà in modo unico quando le interroghiamo.

🎬 Cosa faremo in questa fase
In questa fase vi propongo di:

-Creare una collezione eterogenea di opere d'arte (alcuni dipinti, sculture, installazioni…).
-Iterare su questa collezione e stampare le descrizioni, usando solo riferimenti alla classe genitore.

Aggiungiamo anche un metodo esegui_interazione() alla superclasse, che ogni sottoclasse può sovrascrivere a modo suo. Tipo:

--Il dipinto può essere semplicemente osservato.
--La scultura può essere esposta con luce radente.
--L’installazione multimediale può attivarsi con un sensore.

Poi testiamo tutto in un modulo main.py: una lista, un ciclo, e il potere del polimorfismo esplode.
'''

class OperaDarte:
    def __init__(self,titolo,autore,anno,tipo):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.tipo = tipo
    
    def descrizione(self):
        return f"{self.titolo} è un {self.tipo} di {self.autore}, realizzato nell'anno {self.anno}"
    
    def esegui_interazione(self):
        return "L'opera d'Arte interagisce"

opera1 = OperaDarte("La Gioconda", "Leonardo da Vinci", 1503, "dipinto")
opera2 = OperaDarte("David", "Michelangelo", 1504, "scultura")
print(opera1.descrizione())
print(opera2.descrizione())
 