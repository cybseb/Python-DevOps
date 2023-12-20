import subprocess
# Exemple 1 : Exécuter une commande et obtenir la sortie
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, text=True)
print(result.stdout)

