import customtkinter as ctk
from tkinter import messagebox

def ouvrir_ajout_etudiant():
    # Création de la fenêtre de saisie
    fenetre_ajout = ctk.CTkToplevel()
    fenetre_ajout.title("Ajouter un étudiant")
    fenetre_ajout.geometry("450x500")
    fenetre_ajout.resizable(False, False)

    # Fonction d'enregistrement
    def enregistrer_etudiant():
        nom = entry_nom.get().strip()
        prenom = entry_prenom.get().strip()
        date_naissance = entry_date.get().strip()
        lieu_naissance = entry_lieu.get().strip()
        sexe = sexe_var.get().strip()
        nationalite = entry_nationalite.get().strip()
        classe = entry_classe.get().strip()
        serie = entry_serie.get().strip()

        if nom and prenom and date_naissance and lieu_naissance and sexe and nationalite and classe and serie:
            messagebox.showinfo("Succès", "Étudiant ajouté avec succès !")
            fenetre_ajout.destroy()  # Fermer la fenêtre après enregistrement
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs !")

    # Création des champs alignés
    def creer_champ(parent, label_text):
        frame = ctk.CTkFrame(parent)
        frame.pack(pady=5, padx=20, fill="x")

        label = ctk.CTkLabel(frame, text=label_text, font=("Arial", 14), width=120)
        label.pack(side="left", padx=10)

        entry = ctk.CTkEntry(frame, width=250, height=35)
        entry.pack(side="left")

        return entry

    # Champs d'inscription
    entry_nom = creer_champ(fenetre_ajout, "Nom :")
    entry_prenom = creer_champ(fenetre_ajout, "Prénom :")
    entry_date = creer_champ(fenetre_ajout, "Date de naissance :")
    entry_lieu = creer_champ(fenetre_ajout, "Lieu de naissance :")

    # Sélection du sexe
    frame_sexe = ctk.CTkFrame(fenetre_ajout)
    frame_sexe.pack(pady=5, padx=20, fill="x")
    label_sexe = ctk.CTkLabel(frame_sexe, text="Sexe :", font=("Arial", 14), width=120)
    label_sexe.pack(side="left", padx=10)
    sexe_options = ["M", "F"]
    sexe_var = ctk.StringVar(value=sexe_options[0])
    sexe_menu = ctk.CTkOptionMenu(frame_sexe, values=sexe_options, variable=sexe_var)
    sexe_menu.pack(side="left")

    entry_nationalite = creer_champ(fenetre_ajout, "Nationalité :")
    entry_classe = creer_champ(fenetre_ajout, "Classe :")
    entry_serie = creer_champ(fenetre_ajout, "Série :")

    # Bouton Enregistrer
    btn_enregistrer = ctk.CTkButton(fenetre_ajout, text="Enregistrer", command=enregistrer_etudiant)
    btn_enregistrer.pack(pady=20)

    fenetre_ajout.mainloop()
