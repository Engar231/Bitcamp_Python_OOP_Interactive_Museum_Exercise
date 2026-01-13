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

🎨 LINEA GUIDA PER LA CLASSE OperaDArte

🧠 Obiettivo
Creare una classe OperaDArte che rappresenti un’opera esposta in un museo digitale.
Ogni opera sarà un oggetto, con attributi (caratteristiche) e metodi (comportamenti).

🧱 Attributi (dati interni all’opera)
Questi attributi andranno definiti nel costruttore __init__:

-titolo (stringa): il nome dell’opera
-autore (stringa): chi l'ha realizzata
-anno (intero): anno di realizzazione
-tipo (stringa): dipinto, scultura, installazione, ecc.

⚠️ Estensione opzionale (per chi vuole personalizzare di più):

-stile (es. Rinascimento, Barocco, Modernismo)
-materiale (per sculture: marmo, bronzo, ecc.)
-dimensioni (es. “77 cm x 53 cm”)

🛠️ Metodi (azioni dell’opera)
Definire almeno un metodo per:

-descrivere l’opera, ad esempio tramite un metodo descrizione() che restituisce una frase come:
“La Gioconda è un dipinto di Leonardo da Vinci, realizzato nel 1503.”
'''
import json 
import tkinter as tk 
from tkinter import ttk, messagebox 
from abc import ABC, abstractmethod 
import functools
import logging 

class OperaDarte:
    def __init__(self,titolo,autore,anno,tipo):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.tipo = tipo
    
    def esegui_interazione(self):
        return "L'opera d'Arte interagisce"
    
    def descrizione(self):
        return f"{self.titolo} è un {self.tipo} di {self.autore}, realizzato nell'anno {self.anno}"
opera1 = OperaDarte("La Gioconda", "Leonardo da Vinci", 1503, "dipinto")
opera2 = OperaDarte("David", "Michelangelo", 1504, "scultura")
print(opera1.descrizione())
print(opera2.descrizione())
 