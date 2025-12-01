
utilisateurs = []

def hacher_mdp(mdp):
    return mdp[::-1] #chat#


def ajouter_utilisateur():
    nom = input("Nom : ")
    email = input("Email : ")
    mdp = input("Mot de passe : ")
    utilisateur = {
        "nom": nom,
        "email": email,
        "mdp": hacher_mdp(mdp)
    }
    utilisateurs.append(utilisateur)
    print(" Utilisateur ajouté !")


def afficher_utilisateurs():
    if not utilisateurs:
        print(" Aucun utilisateur enregistré.")
    else:
        for i, u in enumerate(utilisateurs):
            print(f"{i+1}. Nom: {u['nom']}, Email: {u['email']}, MDP: {u['mdp']}")

