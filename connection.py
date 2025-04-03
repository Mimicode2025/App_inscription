from tkinter import *
import customtkinter as ctk

# Configuration de l'application
ctk.set_appearance_mode("dark")  # Mode sombre par défaut
ctk.set_default_color_theme("blue")  # Thème bleu

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Connexion Administrateur")
app.geometry("500x400")
app.resizable(False, False)

# Fonction pour changer le thème
def switch_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

# Fonction de connexion (à améliorer avec une base de données)
def login():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    password = entry_password.get()
    try:
        if nom == "TRAORE" and prenom == "mimi" and password == "1234567":
            print(f"Connexion réussie pour {prenom} {nom} le mot de passe {password}")
            app.destroy()  # Fermer la fenêtre de connexion
            exec(open("gestionInscription.py").read())
    except:
            print("Veuillez remplir tous les champs.")

# Widgets
label_titre = ctk.CTkLabel(app, text="Connexion Administrateur", font=("Arial", 25, "bold"))
label_titre.pack(pady=10)

entry_nom = ctk.CTkEntry(app, placeholder_text="Saisir votre Nom", width=350, height=35)
entry_nom.pack(pady=10)

entry_prenom = ctk.CTkEntry(app, placeholder_text="saisir votre Prénom", width=350, height=35)
entry_prenom.pack(pady=10)

entry_password = ctk.CTkEntry(app, placeholder_text="saisir votre Mot de passe", show="*", width=350, height=35)
entry_password.pack(pady=10)

btn_login = ctk.CTkButton(app, text="Se connecter", command=login)
btn_login.pack(pady=10)

btn_theme = ctk.CTkButton(app, text="Changer le thème", command=switch_theme)
btn_theme.pack(pady=10)

# Lancer l'application
app.mainloop()
