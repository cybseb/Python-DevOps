import subprocess

# Exemple 4 : Exécuter une commande en vérifiant les erreurs
try:
	result = subprocess.run(['./Files/parm.sh', 'param1 param2 param3'], check=True, stdout=subprocess.PIPE, text=True)
	print(result.stdout)
	result = subprocess.run(['./Files/script.sh', ''], check=True, stdout=subprocess.PIPE, text=True)
	print(result.stdout)
except subprocess.CalledProcessError as e:
	print(f"Erreur : {e}")
