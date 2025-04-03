import customtkinter as ctk
from tkinter import ttk
from AjouterEleve import ouvrir_ajout_etudiant

# Configuration de l'application
ctk.set_appearance_mode("dark")  # Mode sombre par défaut
ctk.set_default_color_theme("blue")

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Gestion des Inscriptions")
app.geometry("1000x600")
app.resizable(False, False)

# Fonction pour changer le thème
def switch_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

# --- SECTION : FILTRAGE ---
frame_filtre = ctk.CTkFrame(app)
frame_filtre.pack(fill='x', padx=10, pady=5)

ctk.CTkLabel(frame_filtre, text="Filtrer la liste par :").pack(side='left', padx=5)
entry_filtre_nom = ctk.CTkEntry(frame_filtre, placeholder_text="Nom et prénom")
entry_filtre_nom.pack(side='left', padx=5)

tk_filtre_classe = ttk.Combobox(frame_filtre, values=["6éme", "5éme", "4éme", "3éme", "1ère", "2nde", "Terminale"])
tk_filtre_classe.set("Classe")
tk_filtre_classe.pack(side='left', padx=5)

btn_rechercher = ctk.CTkButton(frame_filtre, text="Rechercher")
btn_rechercher.pack(side='left', padx=5)

btn_afficher_tout = ctk.CTkButton(frame_filtre, text="Afficher tout")
btn_afficher_tout.pack(side='left', padx=5)

btn_theme = ctk.CTkButton(frame_filtre, text="Changer le thème", command=switch_theme)
btn_theme.pack(side='left', padx=5)

# --- SECTION : TABLEAU DES ÉLÈVES ---
frame_table = ctk.CTkFrame(app)
frame_table.pack(fill='both', expand=True, padx=10, pady=5)

colonnes = ("ID", "Nom", "Prénom", "Date de naissance", "Sexe", "Nationalité", "Classe", "Série")
table = ttk.Treeview(frame_table, columns=colonnes, show='headings')

for col in colonnes:
    table.heading(col, text=col)
    table.column(col, width=100)

table.pack(fill='both', expand=True)

# --- SECTION : BOUTONS D'ACTION ---
frame_buttons = ctk.CTkFrame(app)
frame_buttons.pack(fill='x', padx=10, pady=5)

btn_ajouter = ctk.CTkButton(frame_buttons, text="Ajouter", command= ouvrir_ajout_etudiant)
btn_ajouter.pack(side='left', padx=5)

btn_modifier = ctk.CTkButton(frame_buttons, text="Modifier")
btn_modifier.pack(side='left', padx=5)

btn_supprimer = ctk.CTkButton(frame_buttons, text="Supprimer")
btn_supprimer.pack(side='left', padx=5)

btn_imprimer = ctk.CTkButton(frame_buttons, text="Imprimer")
btn_imprimer.pack(side='left', padx=5)

# Lancer l'application
app.mainloop()
