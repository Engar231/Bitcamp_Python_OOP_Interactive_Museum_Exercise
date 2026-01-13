
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

Fase 5 - 🎓 Astraiamo! 
Voglio portarvi a riflettere su cosa tutte le opere d’arte dovrebbero obbligatoriamente fare. 
Non importa che siano dipinti, sculture o installazioni multimediali: 
ogni opera deve poter fornire una descrizione e deve poter essere interagita.

E come facciamo a “obbligare” tutte le sottoclassi a rispettare questo comportamento?
💡 Utilizziamo un’interfaccia astratta! 

🧩 Cosa cambia concretamente
Definiamo una nuova classe Interattiva, astratta, che fornisce l'interfaccia per il metodo esegui_interazione().
Allo stesso modo, potremmo avere anche un’interfaccia per la descrizione (Descrivibile), 
oppure rendere la nostra OperaDArte classe astratta, imponendo che chi la eredita debba implementare quei metodi.

Così facendo, se una sottoclasse si "dimentica" di implementare un metodo fondamentale… 
Python non glielo perdona: errore a runtime garantito!
'''
import json 
import tkinter as tk 
from tkinter import ttk, messagebox 
from abc import ABC, abstractmethod 
import functools
import logging 

class OperaDarte(ABC):
    def __init__(self,titolo,autore,anno,tipo):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.tipo = tipo

    @abstractmethod
    def info_base(self):
        pass
    @abstractmethod
    def esegui_interazione(self):
        pass
    @abstractmethod
    def descrizione(self):
        pass
    @abstractmethod
    def __str__(self):
        pass

# ctrl+ù per commentare tutto
# opera1 = OperaDarte("La Gioconda", "Leonardo da Vinci", 1503, "dipinto")
# opera2 = OperaDarte("David", "Michelangelo", 1504, "scultura")
# print(opera1.descrizione())
# print(opera2.descrizione())