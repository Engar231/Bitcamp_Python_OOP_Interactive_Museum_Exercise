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

🔐 FASE 2 – L’incapsulamento: proteggiamo le nostre opere
Ragazzi, ora che abbiamo imparato a creare oggetti e a descriverli, dobbiamo fare un passo avanti.
Vi siete accorti che possiamo modificare qualsiasi attributo dall’esterno? Tipo così:
opera1.anno = "banana"
Ecco… questo non va bene!
Immaginate se in un museo qualcuno potesse cambiare il nome o l’autore di un’opera a caso…
Serve protezione. Serve controllo. Serve incapsulamento!

🧱 Cosa facciamo in questa fase:
Rendiamo gli attributi "privati" (o meglio, “protetti” in stile Python).
-Usiamo getter e setter per controllare l’accesso.
-Introduciamo il decoratore @property per farlo con stile.

📌 Linea guida
Ora modifichiamo la nostra classe OperaDArte in modo che gli attributi non siano accessibili direttamente.
Useremo un meccanismo chiamato incapsulamento, che ci permette di proteggere i dati interni di un oggetto e accedervi solo tramite metodi controllati.

✅ Cosa deve contenere la nuova versione della classe
Gli attributi devono essere "protetti" usando il prefisso _ (es. _titolo, _autore…).
Per ogni attributo, ci sarà:

-un getter per leggerne il valore;
-un setter per modificarlo, ma solo se il dato è valido (es. l’anno dev’essere un intero > 0).
-Almeno un attributo (anno) dovrà verificare la validità del dato nel setter.
-L’accesso deve avvenire con la sintassi classica, grazie a @property.
'''
import json 
import tkinter as tk 
from tkinter import ttk, messagebox 
from abc import ABC, abstractmethod 
import functools
import logging 

class OperaDarte:
    def __init__(self,titolo,autore,anno,tipo):
        self._titolo = titolo
        self._autore = autore
        self._anno = anno
        self._tipo = tipo
#Protezione del dato       
    @property
    def titolo(self):
        return self._titolo
#definiamo la property e ritorniamo cosa deve mostrare
    @titolo.setter
    def titolo(self,titolo):
        self._titolo = titolo
#setter definiamo titolo, self_titolo = titolo
    @property
    def autore(self):
        return self._autore
    @autore.setter
    def autore(self,autore):
        self._autore = autore
    
    @property
    def anno(self):
        return self._anno
    @anno.setter
    def anno(self,anno):
        if self._anno >0: #Qui mettiamo un controllo per essere certi che sia un numero "valido"
            self._anno = anno
        else:
            print("Anno non valido") #Il controllo è qui

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo

    def descrizione(self):
        return f"{self.titolo} è un {self.tipo} di {self.autore}, realizzato nell'anno {self.anno}"
opera1 = OperaDarte("La Gioconda", "Leonardo da Vinci", 1503, "dipinto")
opera2 = OperaDarte("David", "Michelangelo", 1504, "scultura")
print(opera1.descrizione())
print(opera2.descrizione())
 