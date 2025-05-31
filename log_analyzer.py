from colorama import Fore, Style, init
init()
def analyser_logs(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()

    erreur = sum(1 for ligne in lignes if "ERROR" in ligne)
    warning = sum(1 for ligne in lignes if "WARNING" in ligne)
    info = sum(1 for ligne in lignes if "INFO" in ligne)

    print("📊 Statistiques des logs :")
    print(f"ERROR   : {erreur}")
    print(f"WARNING : {warning}")
    print(f"INFO    : {info}")

    with open("rapport.txt", "w") as rapport:
        rapport.write("Résumé des logs :\n")
        rapport.write(f"ERROR   : {erreur}\n")
        rapport.write(f"WARNING : {warning}\n")
        rapport.write(f"INFO    : {info}\n")

if __name__ == "__main__":
    analyser_logs("log.txt")


print("📊 Statistiques des logs :")
print(Fore.RED + f"ERROR   : {erreur}" + Style.RESET_ALL)
print(Fore.YELLOW + f"WARNING : {warning}" + Style.RESET_ALL)
print(Fore.CYAN + f"INFO    : {info}" + Style.RESET_ALL)