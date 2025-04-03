import customtkinter as ctk
from tkinter import ttk, messagebox

# Configuration de l'application
ctk.set_appearance_mode("dark")  # Mode sombre par défaut
ctk.set_default_color_theme("blue")

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Gestion des Inscriptions")
app.geometry("1100x600")
app.resizable(False, False)


def switch_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


# --- SECTION : FILTRAGE ---
frame_filtre = ctk.CTkFrame(app)
frame_filtre.pack(fill='x', padx=10, pady=5)

ctk.CTkLabel(frame_filtre, text="Filtrer les éléve par:").pack(side='left', padx=5)
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

# --- SECTION : PRINCIPALE ---
frame_principal = ctk.CTkFrame(app)
frame_principal.pack(fill='both', expand=True, padx=10, pady=5)

# Section Tableau
frame_table = ctk.CTkFrame(frame_principal)
frame_table.pack(side="left", fill='both', expand=True, padx=5, pady=5)

colonnes = ("ID", "Nom", "Prénom", "Date de naissance", "Sexe", "Nationalité", "Classe", "Série")
table = ttk.Treeview(frame_table, columns=colonnes, show='headings')
for col in colonnes:
    table.heading(col, text=col)
    table.column(col, width=110)
table.pack(fill='both', expand=True)

# Section Formulaire d'ajout
frame_form = ctk.CTkFrame(frame_principal)
frame_form.pack(side="right", fill='y', padx=10, pady=10)

ctk.CTkLabel(frame_form, text="Ajouter un élève", font=("Arial", 16, "bold")).pack(pady=5)


def creer_champ(parent, label_text):
    frame = ctk.CTkFrame(parent)
    frame.pack(pady=5, padx=10, fill="x")
    label = ctk.CTkLabel(frame, text=label_text, font=("Arial", 14))
    label.pack(side="left", padx=5)
    entry = ctk.CTkEntry(frame, width=300)
    entry.pack(side="left")
    return entry


entry_nom = creer_champ(frame_form, "Nom :")
entry_prenom = creer_champ(frame_form, "Prénom :")
entry_date = creer_champ(frame_form, "Date de naissance :")
entry_lieu = creer_champ(frame_form, "Lieu de naissance :")

frame_sexe = ctk.CTkFrame(frame_form)
frame_sexe.pack(pady=5, padx=10, fill="x")
ctk.CTkLabel(frame_sexe, text="Sexe :", font=("Arial", 14)).pack(side="left", padx=5)
sexe_var = ctk.StringVar(value="M")
sexe_menu = ctk.CTkOptionMenu(frame_sexe, values=["M", "F"], variable=sexe_var)
sexe_menu.pack(side="left", padx=15)

entry_nationalite = creer_champ(frame_form, "Nationalité :")
entry_classe = creer_champ(frame_form, "Classe :")
entry_serie = creer_champ(frame_form, "Série :")


def enregistrer_etudiant():
    if all([entry_nom.get(), entry_prenom.get(), entry_date.get(), entry_lieu.get(), sexe_var.get(),
            entry_nationalite.get(), entry_classe.get(), entry_serie.get()]):
        messagebox.showinfo("Succès", "Étudiant ajouté avec succès !")
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs !")


# Boutons en bas du formulaire
frame_buttons = ctk.CTkFrame(frame_form)
frame_buttons.pack(pady=10, padx=10, fill="x")

btn_enregistrer = ctk.CTkButton(frame_buttons, text="Enregistrer", command=enregistrer_etudiant)
btn_enregistrer.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
btn_modifier = ctk.CTkButton(frame_buttons, text="Modifier")
btn_modifier.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
btn_supprimer = ctk.CTkButton(frame_buttons, text="Supprimer")
btn_supprimer.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
btn_imprimer = ctk.CTkButton(frame_buttons, text="Imprimer")
btn_imprimer.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

frame_buttons.columnconfigure((0, 1), weight=1)

app.mainloop()
