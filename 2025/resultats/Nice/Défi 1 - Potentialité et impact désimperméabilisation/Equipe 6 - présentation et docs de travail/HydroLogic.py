import tkinter as tk
from tkinter import ttk, messagebox
import sys

class DesimpermeabilisationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HydroLogic")
        self.root.geometry("800x600")
        self.root.configure(bg='#f5f5f5')
        
        # Variables d'état
        self.answers = {}
        self.step = 1
        
        # Style
        self.setup_styles()
        
        # En-tête
        self.create_header()
        
        # Frame principal
        self.main_frame = tk.Frame(root, bg='#f5f5f5')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Démarrer
        self.show_question()
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Style pour les boutons
        style.configure('Custom.TButton',
                       font=('Segoe UI', 20, 'bold'),
                       padding=15,
                       background='white',
                       foreground='black')
        style.map('Custom.TButton',
                 background=[('active', '#5568d3')])
    
    def create_header(self):
        header = tk.Frame(self.root, bg='#667eea', height=200)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, 
                        text="HydroLogic",
                        font=('Segoe UI', 34, 'bold'),
                        bg='#667eea',
                        fg='white')
        title.pack(pady=15)
        
        subtitle = tk.Label(header,
                           text="Le chemin vers la perméabilité",
                           font=('Segoe UI', 22, 'bold'),
                           bg='#667eea',
                           fg='White')
        subtitle.pack()
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_question(self):
        self.clear_frame()
        
        # Frame pour la question
        question_frame = tk.Frame(self.main_frame, bg='white', relief=tk.RAISED, bd=2)
        question_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # Question selon l'étape
        if self.step == 1:
            self.ask_question(
                question_frame,
                "Le site est-il placé sur une ICPE, un captage ou une nappe peu profonde (<1m)?\n(Vous trouverez ces informations sur Géorisques ou InfoTerre)",
                [("Oui", lambda: self.answer(1, 'oui')),
                 ("Non", lambda: self.answer(1, 'non'))]
            )
        
        elif self.step == 2 and self.answers.get(1) == 'oui':
            self.ask_question(
                question_frame,
                "Est-ce que les eaux de ruissellement sont dirigées vers un réseau unitaire ? \n(Les plans de réseaux sont accessibles auprès des communes, régies, exploitants)",
                [("Oui", lambda: self.answer(2, 'oui')),
                 ("Non", lambda: self.answer(2, 'non'))]
            )
        
        elif self.step == 3 and self.answers.get(2) == 'non':
            self.ask_question(
                question_frame,
                "Souhaitez-vous tout de même implanter une solution de désimperméabilisation ?",
                [("Oui", lambda: self.answer(3, 'oui')),
                 ("Non", lambda: self.answer(3, 'non'))]
            )
        
        elif self.step == 2 and self.answers.get(1) == 'non':
            self.ask_question(
                question_frame,
                "Le site est-il soumis à des inondations dues à... ?\n(Vous trouverez cette information dans les \nPlans de Préventions des Risques Inondations (PPRI))" ,
                [("Crues", lambda: self.answer(4, 'crues')),
                 ("Ruissellement", lambda: self.answer(4, 'ruissellement'))]
            )
        
        elif self.step == 5 and self.answers.get(4) == 'ruissellement':
            self.ask_question(
                question_frame,
                "Est-ce que les eaux de ruissellement sont dirigées vers un réseau unitaire ? \n(Les plans de réseaux sont accessibles auprès des communes, régies, exploitants)",
                [("Oui", lambda: self.answer(5, 'oui')),
                 ("Non", lambda: self.answer(5, 'non'))]
            )
        
        elif self.step == 6:
            self.ask_question(
                question_frame,
                "Quelle est la géologie du sous-sol ?\n(Résultat de test de perméabilité (Porchet)",
                [("Perméable", lambda: self.answer(6, 'perméable')),
                 ("Imperméable", lambda: self.answer(6, 'imperméable'))]
            )
        
        elif self.step == 7 and self.answers.get(6) == 'imperméable':
            self.ask_question(
                question_frame,
                "Quelle est l'occupation du sol ? \n(Vous trouverez cette information sur les cartes IGN d'occupation du sol)",
                [("Bâti", lambda: self.answer(7, 'bâti')),
                 ("Non bâti", lambda: self.answer(7, 'non bâti'))]
            )
        
        elif self.step == 8 and self.answers.get(6) == 'perméable':
            self.ask_question(
                question_frame,
                "Existe-t-il des risques de mouvement de terrain ou des fortes pentes ? \n(Vous trouverez ces informations sur les \nModèles Numériques de Terrain accessiblent sur le site de l'IGN)",
                [("Oui", lambda: self.answer(8, 'oui')),
                 ("Non", lambda: self.answer(8, 'non'))]
            )
        
        elif self.step == 9:
            self.ask_question(
                question_frame,
                "Quelle est l'occupation du sol ? \n(Vous trouverez cette information sur les cartes IGN d'occupation du sol)",
                [("Bâti", lambda: self.answer(9, 'bâti')),
                 ("Non bâti", lambda: self.answer(9, 'non bâti'))]
            )
        
        elif self.step == 10 and self.answers.get(9) == 'bâti':
            self.ask_question(
                question_frame,
                "La surface utilisable pour réaliser la désimperméabilisation est... ?",
                [("Élevée", lambda: self.answer(10, 'élevée')),
                 ("Faible", lambda: self.answer(10, 'faible'))]
            )
        
        elif self.step == 11:
            self.ask_question(
                question_frame,
                "La profondeur utilisable pour réaliser la désimperméabilisation est... ?",
                [("Élevée", lambda: self.answer(11, 'élevée')),
                 ("Faible", lambda: self.answer(11, 'faible'))]
            )
        
        elif self.step == 12 and self.answers.get(9) == 'non bâti':
            self.ask_question(
                question_frame,
                "Quel est le type de surface ?",
                [("Parking", lambda: self.answer(12, 'parking')),
                 ("Routes", lambda: self.answer(12, 'routes')),
                 ("Espace public", lambda: self.answer(12, 'espace public'))]
            )
    
    def ask_question(self, parent, question_text, options):
        # Question
        question_label = tk.Label(parent,
                                  text=question_text,
                                  font=('Segoe UI', 16, 'bold'),
                                  bg='white',
                                  fg='black',
                                  justify=tk.CENTER)
        question_label.pack(pady=40)
        
        # Boutons
        button_frame = tk.Frame(parent, bg='white')
        button_frame.pack(pady=20)
        
        for text, command in options:
            btn = tk.Button(button_frame,
                          text=text,
                          command=command,
                          font=('Segoe UI', 14, 'bold'),
                          bg='white',
                          fg='black',
                          activebackground='#5568d3',
                          activeforeground='white',
                          relief=tk.FLAT,
                          padx=30,
                          pady=15,
                          cursor='hand2',
                          width=15)
            btn.pack(pady=10)
    
    def answer(self, question, value):
        self.answers[question] = value
        
        # Logique de navigation
        if question == 1 and value == 'oui':
            self.step = 2
            self.show_question()
        elif question == 2 and value == 'oui':
            self.show_result()
        elif question == 2 and value == 'non':
            self.step = 3
            self.show_question()
        elif question == 3:
            self.show_result()
        elif question == 1 and value == 'non':
            self.step = 2
            self.show_question()
        elif question == 4 and value == 'crues':
            self.show_result()
        elif question == 4 and value == 'ruissellement':
            self.step = 5
            self.show_question()
        elif question == 5 and value == 'non':
            self.show_result()
        elif question == 5 and value == 'oui':
            self.step = 6
            self.show_question()
        elif question == 6 and value == 'imperméable':
            self.step = 7
            self.show_question()
        elif question == 7:
            self.show_result()
        elif question == 6 and value == 'perméable':
            self.step = 8
            self.show_question()
        elif question == 8 and value == 'oui':
            self.show_result()
        elif question == 8 and value == 'non':
            self.step = 9
            self.show_question()
        elif question == 9 and value == 'bâti':
            self.step = 10
            self.show_question()
        elif question == 10:
            self.step = 11
            self.show_question()
        elif question == 11:
            self.show_result()
        elif question == 9 and value == 'non bâti':
            self.step = 12
            self.show_question()
        elif question == 12:
            self.show_result()
    
    def show_result(self):
        self.clear_frame()
        
        result_frame = tk.Frame(self.main_frame, bg='#e8f5e9', relief=tk.RAISED, bd=2)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # Titre
        title = tk.Label(result_frame,
                        text="✅ Résultat de l'analyse",
                        font=('Segoe UI', 24, 'bold'),
                        bg='#e8f5e9',
                        fg='#2e7d32')
        title.pack(pady=20)
        
        # Texte scrollable
        text_frame = tk.Frame(result_frame, bg='#e8f5e9')
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        result_text = tk.Text(text_frame,
                             font=('Segoe UI', 18),
                             bg='#e8f5e9',
                             fg='#333',
                             wrap=tk.WORD,
                             yscrollcommand=scrollbar.set,
                             relief=tk.FLAT,
                             padx=10,
                             pady=10)
        result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=result_text.yview)
        
        # Contenu du résultat
        result_content = self.get_result_text()
        result_text.insert('1.0', result_content)
        result_text.config(state=tk.DISABLED)
        
        # Bouton recommencer
        btn_reset = tk.Button(result_frame,
                             text="🔄 Nouvelle analyse",
                             command=self.reset,
                             font=('Segoe UI', 14, 'bold'),
                             bg='#667eea',
                             fg='white',
                             activebackground='#5568d3',
                             activeforeground='white',
                             relief=tk.FLAT,
                             padx=30,
                             pady=15,
                             cursor='hand2')
        btn_reset.pack(pady=20)
    
    def get_result_text(self):
        if self.answers.get(1) == 'oui' and self.answers.get(2) == 'oui':
            return """Il faut ralentir le débit de pointe de la station d'épuration par temps de pluie.

Solutions recommandées :
🌿 Toiture végétalisée;
💧 Bassin de rétention relié au réseau d'assainissement; 
🏗️ Revêtement perméable avec drain renvoyant les eaux dans le réseau d'assainissement """

        elif self.answers.get(1) == 'oui' and self.answers.get(2) == 'non' and self.answers.get(3) == 'oui':
            return """Les solutions envisageables ne doivent pas assurer une infiltration directe.

Solutions proposées :
🌿 Toiture végétalisée;
💧 Bassin de rétention relié au réseau pluvial; 
🏗️ Revêtement perméable avec drain renvoyant les eaux dans le réseau d'assainissement """

        elif self.answers.get(1) == 'oui' and self.answers.get(2) == 'non' and self.answers.get(3) == 'non':
            return """Le site choisi ne présente pas une priorité de désimperméabilisation.

Les eaux retournent ainsi dans le réseau pluvial."""

        elif self.answers.get(4) == 'crues':
            return """⚠️ Les méthodes de désimperméabilisation ne permettent pas de résoudre les inondations liées à des crues.

Nous n'avons pas de solutions à vous proposer pour limiter cet aléa."""

        elif self.answers.get(5) == 'non':
            return """Nous sommes en réseau séparatif, de ce fait la mise en place d'une technique de désimperméabilisation n'est pas prioritaire.

Cependant, la mise en place d'une solution reste envisageable."""

        elif self.answers.get(6) == 'imperméable' and self.answers.get(7) == 'bâti':
            return """Il faut limiter le débit de pointe par temps de pluie de la STEP. 

Solutions recommandées :
🌿 Toiture végétalisée;
💧 Bassin de rétention relié au réseau d'assainissement; 
🏗️ Revêtement perméable avec drain renvoyant les eaux dans le réseau d'assainissement """

        elif self.answers.get(6) == 'imperméable' and self.answers.get(7) == 'non bâti':
            return """Il faut limiter le débit de pointe par temps de pluie de la STEP.

Solutions recommandées :
💧 Bassin de rétention relié au réseau d'assainissement; 
🏗️ Revêtement perméable avec drain renvoyant les eaux dans le réseau d'assainissement """

        elif self.answers.get(8) == 'oui':
            return """⚠️ Il est déconseillé de mettre en place des méthodes de désimperméabilisation, car le ruissellement sera prédominant sur l'infiltration."""

        elif self.answers.get(10) == 'élevée' and self.answers.get(11) == 'élevée':
            return """Solutions envisageables :
Bassin de rétention, Étangs, Bassin d'infiltration, Puit perdu, Bandes filtrantes, Fossés d'infiltration, Puit d'infiltration, Tranchées d'infiltration, Jardin de pluie, Revêtement perméable

💡 Recommandations pour une recharge optimale :
1. Puit d'infiltration
2. Bassin d'infiltration
3. Puit perdu
4. Revêtements perméables

💡 Recommandations pour une recharge et une capacité de traitement optimale :
🏗️ Revêtement perméable 
💧 Bassin d'infiltration"""

        elif self.answers.get(10) == 'élevée' and self.answers.get(11) == 'faible':
            return """Solutions envisageables :
Étang, Bassin d'infiltration, Bassin de rétention

💡 Recommandations :
🌊 Pour la recharge de la nappe : Bassin d'infiltration
🔧 Pour une maintenance optimisée : Bassin de rétention"""

        elif self.answers.get(10) == 'faible' and self.answers.get(11) == 'élevée':
            return """Solutions envisageables :
Tranchées d'infiltration, Puit d'infiltration, Drain filtrant

💡 Recommandations :
🌊 Pour la recharge de la nappe : Puit d'infiltration
🔧 Pour le traitement et la maintenance : Tranchée d'infiltration ou Drain filtrant"""

        elif self.answers.get(10) == 'faible' and self.answers.get(11) == 'faible':
            return """Solutions envisageables :

🏗️ Revêtement perméable
🌸 Jardin de pluie

Ces deux solutions présentent les mêmes caractéristiques en termes de recharge de la nappe, capacité de traitement et besoin de maintenance."""

        elif self.answers.get(12) == 'parking':
            return """Solution pour les parking :

🏗️ Revêtement perméable

Cette solution permet de conserver l'usage du sol."""

        elif self.answers.get(12) == 'routes':
            return """⚠️ Il est déconseillé de mettre en place des méthodes de désimperméabilisation par infiltration directe, car il y a un risque de contamination de la nappe.

Solutions recommandées :
🏗️ Revêtement perméable avec drain renvoyant les eaux dans le réseau d'assainissement 
💧 Bassin de rétention relié au réseau d'assainissement"""

        elif self.answers.get(12) == 'espace public':
            return """Solutions multiples disponibles :

Bassin de rétention, Étangs, Bassin d'infiltration, Puit perdu, Bandes filtrantes, Fossés d'infiltration, Puit d'infiltration, Tranchées d'infiltration, Jardin de pluie, Revêtement perméable

Le choix sera à réaliser en fonction des besoins et de la volonté de la collectivité."""

        return "Résultat non disponible."
    
    def reset(self):
        self.answers = {}
        self.step = 1
        self.show_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = DesimpermeabilisationApp(root)
    root.mainloop()
