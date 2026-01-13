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

🎨 E adesso ci facciamo una GUI base Fase 7
Ragazzi, adesso portiamo tutto questo bel codice nel mondo visivo!
Costruiremo un’interfaccia grafica che ci permetterà di vedere le opere, 
aggiungerne di nuove, salvarle e ricaricarle da file.
Useremo tkinter, il toolkit grafico base di Python.
Non sarà solo per “bellezza”: la GUI ci permetterà anche di interagire 
con le opere come abbiamo fatto nella console.

🛠️ Cosa faremo nella GUI
-Mostrare la lista delle opere caricate da file
-Visualizzare la descrizione di ogni opera selezionata
-Eseguire l’interazione associata all’opera (via esegui_interazione)
-Aggiungere nuove opere tramite un form guidato
-Salvare e caricare la collezione da file JSON

💡 Architettura suggerita
La GUI vera e propria dovra contenere:
-l'importazione di tutte le classi e metodi necessari
-tkinter.Tk() per la finestra principale
-Listbox per selezionare un'opera
-Text o Label per mostrare la descrizione
-Button per interazione / aggiunta / salvataggio / caricamento
'''
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk  # Serve la libreria Pillow (pip install pillow)
from OperaDarte_Fase6Json import OperaDarte
from OperaDarte_Fase62Json import Dipinto, Scultura, InstallazioneMultimediale, salva_collezione, carica_collezione
import logging
import os
import winsound #questo serve epr il suono

 # Font e colori personalizzati
font_label = ("Segoe UI", 14)
font_btn = ("Segoe UI", 12, "bold")
font_sottotitolo = ("Gabriola", 12, "bold italic")
font_titolo = ("Gabriola", 28, "bold")
bg_colore = "#1e1e1e" # Sfondo scuro
fg_titolo = "green"
fg_sottotitolo = "white"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Luvre del Piede")  # Titolo finestra
        self.geometry("900x1000")       # Dimensione finestra
        self.configure(bg=bg_colore)   # Colore sfondo
        self.crea_widget()              # Chiama funzione che crea i widget
        self.opere = carica_collezione("collezione.json")  # Carica opere da file JSON


    def crea_widget(self):
          # Frame/cornice per il titolo e sottotitolo
        title_frame = tk.Frame(self, bg=bg_colore)
        title_frame.pack(pady=10)

        # Sottotitolo
        sottotitolo = tk.Label(title_frame, text="BitCamp Presenta:", bg=bg_colore, fg=fg_sottotitolo, font=font_sottotitolo)
        sottotitolo.pack()

        # Titolo principale
        titolo = tk.Label(title_frame, text="Luvre del Piede", bg=bg_colore, fg=fg_titolo, font=font_titolo)
        titolo.pack()

        # Frame per label e lista
        top_frame = tk.Frame(self, bg=bg_colore)
        top_frame.pack(fill=tk.X, pady=10)

        self.eti = tk.Label(top_frame, text="Opere",bg=bg_colore, font=font_sottotitolo,fg=fg_sottotitolo)
        self.eti.pack()
        self.listan = tk.Listbox(top_frame, height=10)
        self.listan.pack(pady=10, fill=tk.X) #si espande per tutta la larghezza della finestra (asse x)
        self.label_descrizione = tk.Label(self, text="Descrizione", bg=bg_colore, fg="white", font=font_label)
        self.label_descrizione.pack(pady=5)

        # Frame per i bottoni in orizzontale
        button_frame = tk.Frame(self, bg=bg_colore)
        button_frame.pack(fill=tk.X, pady=10)

        # Per centrare, crea un "container interno" che fa il wrap dei bottoni
        inner_frame = tk.Frame(button_frame, bg=bg_colore)
        inner_frame.pack()

        self.mostrabutton = tk.Button(inner_frame, text = "Mostra Opere",font=font_sottotitolo,bg=bg_colore,fg=fg_sottotitolo, command=self.mostra_opere)
        self.mostrabutton.pack(side=tk.LEFT, padx=5)
        self.visualbutton = tk.Button(inner_frame, text = "Visualizza Descrizione",font=font_sottotitolo,bg=bg_colore,fg=fg_sottotitolo, command = self.mostra_descrizione)
        self.visualbutton.pack(side=tk.LEFT, padx=5)
        self.intbutton = tk.Button(inner_frame, text="Esegui Interazione",font=font_sottotitolo,bg=bg_colore,fg=fg_sottotitolo, command=self.esegui_interazione)
        self.intbutton.pack(side=tk.LEFT, padx=5)
        self.aggbutton = tk.Button(inner_frame, text="Aggiungi Opera",font=font_sottotitolo,bg=bg_colore,fg=fg_sottotitolo, command=self.aggiungi_opera)
        self.aggbutton.pack(side=tk.LEFT, padx=5)
        self.savebutton = tk.Button(inner_frame, text="Salva",font=font_sottotitolo,bg=bg_colore,fg=fg_sottotitolo, command=self.salva_opere)
        self.savebutton.pack(side=tk.LEFT, padx=5)

        # self.listan.bind("<<ListboxSelect>>", self.visualizza_opera) serve solo se voglio visualizzarlo al click


    def mostra_opere(self):
        self.listan.delete(0, tk.END)  # Pulisco la lista
        for opera in self.opere:
            self.listan.insert(tk.END, opera.titolo)  # Inserisco i titoli nella lista

    
    def mostra_descrizione(self):
        selezione = self.listan.curselection()  # Prendo l'indice selezionato nella lista
        if selezione:
            indice = selezione[0]
            descrizione = self.opere[indice].descrizione()  # Chiedo la descrizione dell'opera selezionata
            winsound.PlaySound("magia.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)  # Suono asincrono
            messagebox.showinfo("Descrizione", descrizione)  # Mostro una finestra con la descrizione
            self.mostra_immagine(self.opere[indice])  # Mostro l'immagine associata all'opera

    
    def esegui_interazione(self):
        selezione = self.listan.curselection()
        if selezione:
            indice = selezione[0]
            messaggio = self.opere[indice].esegui_interazione()
            messagebox.showinfo("Interazione", messaggio)
    
    def salva_opere(self):
        salva_collezione(self.opere, "collezione.json")# Salva la lista di opere su file JSON
        messagebox.showinfo("Salvataggio", "Collezione salvata con successo!")
    
    def aggiungi_opera(self):
        finestra = tk.Toplevel(self) # Finestra pop-up
        finestra.title("Aggiungi nuova opera")
        finestra.geometry("400x400")
        finestra.configure(bg=bg_colore)

         # Etichette e campi
        tk.Label(finestra, text="Tipo (Dipinto, Scultura, InstallazioneMultimediale):", bg=bg_colore, fg=fg_sottotitolo, font=font_label).pack()
        tipo_entry = tk.Entry(finestra)
        tipo_entry.pack()

        tk.Label(finestra, text="Titolo:", bg=bg_colore, fg=fg_sottotitolo, font=font_label).pack()
        titolo_entry = tk.Entry(finestra)
        titolo_entry.pack()

        tk.Label(finestra, text="Autore:", bg=bg_colore, fg=fg_sottotitolo, font=font_label).pack()
        autore_entry = tk.Entry(finestra)
        autore_entry.pack()

        tk.Label(finestra, text="Anno:", bg=bg_colore, fg=fg_sottotitolo, font=font_label).pack()
        anno_entry = tk.Entry(finestra)
        anno_entry.pack()

        # Campi specifici variabili
        campo1_label = tk.Label(finestra, text="Campo 1 (es. tecnica, materiale, formato):", bg=bg_colore, fg=fg_sottotitolo, font=font_label)
        campo1_label.pack()
        campo1_entry = tk.Entry(finestra)
        campo1_entry.pack()

        campo2_label = tk.Label(finestra, text="Campo 2 (altezza cm o interattiva [True/False]):", bg=bg_colore, fg=fg_sottotitolo, font=font_label)
        campo2_label.pack()
        campo2_entry = tk.Entry(finestra)
        campo2_entry.pack()

        def salva():
            tipo = tipo_entry.get().strip()
            titolo = titolo_entry.get().strip()
            autore = autore_entry.get().strip()
            anno = int(anno_entry.get().strip())
            c1 = campo1_entry.get().strip()
            c2 = campo2_entry.get().strip()

            if tipo.lower() == "dipinto":
                nuova = Dipinto(titolo, autore, anno, c1)
            elif tipo.lower() == "scultura":
                nuova = Scultura(titolo, autore, anno, c1, int(c2))
            elif tipo.lower() == "installazionemultimediale":
                nuova = InstallazioneMultimediale(titolo, autore, anno, c1, c2.lower() == "true")
            else:
                messagebox.showerror("Errore", "Tipo non valido")
                return

            self.opere.append(nuova)
            self.mostra_opere()
            finestra.destroy()

        tk.Button(finestra, text="Salva Opera", command=salva, font=font_btn, bg="green", fg="white").pack(pady=10)
    
    def mostra_immagine(self,opera):
        selezione = self.listan.curselection()
        if selezione:
            opera = self.opere[selezione[0]]
            titolo = opera.titolo.lower().replace(" ", "_")  # es: "La Gioconda" -> "la_gioconda"
            base_dir = os.path.dirname(os.path.abspath(r"C:\Users\Calfi\Desktop\Python BitCamp\Python\Museo_Interattivo\immagini_opere))  # cartella dove c'è il tuo .py"))
    #R per far leggere la stringa del percorso file , sennò non andava.
            path_img = os.path.join(base_dir,"immagini_opere",f"{titolo}.jpg") #Solo file jpg  # Costruisce percorso immagine
            print(f"Sto cercando l'immagine in: {path_img}")  # Debug
            if os.path.exists(path_img):
                img_win = tk.Toplevel(self) #Mostra una finestra
                img = Image.open(path_img)
                img = img.resize((300, 400))  # Resize per sicurezza
                photo = ImageTk.PhotoImage(img)
                label_img = tk.Label(img_win, image=photo)
                label_img.image = photo  # importante: evita il garbage collector
                label_img.pack()
            else:
                messagebox.showwarning("Nessuna immagine", f"Nessuna immagine trovata per '{titolo}'.")
                
    def mostra_descrizione(self):
        selezione = self.listan.curselection()
        if selezione:
            indice = selezione[0]
            opera = self.opere[indice]
            descrizione = opera.descrizione()
            winsound.PlaySound("magia.wav", winsound.SND_FILENAME | winsound.SND_ASYNC) 
            messagebox.showinfo("Descrizione", descrizione)
            self.mostra_immagine(opera)  # <-- questa riga mostra l'immagine!


            
if __name__ == "__main__":
    app = App()
    app.mainloop()

