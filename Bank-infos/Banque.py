##########################################################################
###                                                                    ###
###                      CHOUKRY MOHAMED / TDD101                      ###
###             TP9: CLASSE COMPTE ET INTERFACE GRAPHIQUE              ###
###                                                                    ###
##########################################################################



#imprter Tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog



class Compte:
    def __init__(self, mot_de_passe, nom, prenom, solde):
        self.mot_de_passe = mot_de_passe
        self.nom = nom
        self.prenom = prenom
        self.solde = solde

class tkinterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bienvenue chez Mohamed Choukry banque 💸")
        self.root.configure(bg='#3d348b')
        self.root.geometry('400x300')
        self.comptes = self.charger_comptes()

        # Création des widgets
        self.label_mot_de_passe = tk.Label(self.root, bg="#3d348b", fg="#ffffff",font=("Arial", 10), text="Veuillez entrer votre mot de passe :")
        self.entry_mot_de_passe = tk.Entry(self.root, font=("Arial", 10), show="*")
        self.button_valider = tk.Button(self.root, text="Valider", bg="#7678ed", fg="#ffffff",font=("Arial", 10),  command=self.validation_pass)
        self.button_depot = tk.Button(self.root, text="Dépôt", bg="#7678ed", fg="#ffffff",font=("Arial", 10),  command=self.effectuer_depot)
        self.button_retrait = tk.Button(self.root, text="Retrait", bg="#7678ed", fg="#ffffff",font=("Arial", 10),  command=self.effectuer_retrait)
        self.button_transfert = tk.Button(self.root, text="Transfert", bg="#7678ed", fg="#ffffff",font=("Arial", 10),  command=self.effectuer_transfert)



        # Placement des widgets
        self.label_mot_de_passe.pack(anchor=tk.CENTER, pady=(10, 10))
        self.entry_mot_de_passe.pack(anchor=tk.CENTER, pady=(10, 10))
        self.button_valider.pack(anchor=tk.CENTER, pady=(10, 10))
        self.button_depot.pack(anchor=tk.CENTER, pady=(10, 10))
        self.button_retrait.pack(anchor=tk.CENTER, pady=(10, 10))
        self.button_transfert.pack(anchor=tk.CENTER, pady=(10, 10))

        self.root.mainloop()

    def charger_comptes(self):
        comptes = []
        try:
            with open("comptes.txt", "r") as fichier:
                for ligne in fichier:
                    mots = ligne.strip().split(",")
                    compte = {
                        "mot_de_passe": mots[0],
                        "nom": mots[1],
                        "prenom": mots[2],
                        "solde": float(mots[3])
                    }
                    comptes.append(compte)
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Fichier comptes.txt introuvable.")
        return comptes

    def validation_pass(self):
        mot_de_passe = self.entry_mot_de_passe.get()

        # Vérification du mot de passe dans la liste des comptes
        compte_trouve = False
        for compte in self.comptes:
            if compte["mot_de_passe"] == mot_de_passe:
                self.compte_actuel = compte  # Stocke le compte actuel
                self.afficher_informations_compte(compte)
                compte_trouve = True
                break

        if not compte_trouve:
            messagebox.showerror("Erreur", "Mot de passe incorrect.")

    def afficher_informations_compte(self, compte):
        messagebox.showinfo("Informations", f"Nom: {compte['nom']}\nPrénom: {compte['prenom']}\nSolde: {compte['solde']}")

    def effectuer_depot(self):
        montant = float(tk.simpledialog.askstring("Dépôt", "Montant à déposer :"))
        self.compte_actuel["solde"] += montant
        messagebox.showinfo("Dépôt", f"Dépôt effectué. Nouveau solde : {self.compte_actuel['solde']}")

    def effectuer_retrait(self):
        montant = float(tk.simpledialog.askstring("Retrait", "Montant à retirer :"))
        if self.compte_actuel["solde"] >= montant:
            self.compte_actuel["solde"] -= montant
            messagebox.showinfo("Retrait", f"Retrait effectué. Nouveau solde : {self.compte_actuel['solde']}")
        else:
            messagebox.showerror("Erreur", "Solde insuffisant.")

    def effectuer_transfert(self):
        destinataire = tk.simpledialog.askstring("Transfert", "Compte destinataire :")
        montant = float(tk.simpledialog.askstring("Transfert", "Montant à transférer :"))

        compte_destinataire = None
        for compte in self.comptes:
            if compte["nom"] == destinataire:
                compte_destinataire = compte
                break

        if compte_destinataire is not None:
            if self.compte_actuel["solde"] >= montant:
                self.compte_actuel["solde"] -= montant
                compte_destinataire["solde"] += montant
                messagebox.showinfo("Transfert", "Transfert effectué.")
            else:
                messagebox.showerror("Erreur", "Solde insuffisant.")
        else:
            messagebox.showerror("Erreur", "Compte destinataire introuvable.")

# Création de l'interface graphique
interface = tkinterface()

