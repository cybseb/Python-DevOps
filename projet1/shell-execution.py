import subprocess

# Exemple 4 : Exécuter une commande en vérifiant les erreurs
try:
	result = subprocess.run(['./Files/parm.sh', 'param1 param2 param3'], check=True, stdout=subprocess.PIPE, text=True)
	print(result.stdout)
	result = subprocess.run(['./Files/script.sh', ''], check=True, stdout=subprocess.PIPE, text=True)
	print(result.stdout)
except subprocess.CalledProcessError as e:
	print(f"Erreur : {e}")

import os
import subprocess
# Script execution without parameters
script_dir = os.path.dirname(__file__)
script_abosulte_path = os.path.join( script_dir, "Files/script.sh")
subprocess.call(['sh', script_abosulte_path])
# Script execution with parameters
param_script_abosulte_path = os.path.join( script_dir, "Files/parm.sh")
subprocess.call(['sh', param_script_abosulte_path, 'param1 param2'])
