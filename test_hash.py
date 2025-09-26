import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from hashgestion import HashGestion  # nom exact de la classe

# Crée une instance
hash_obj = HashGestion()

# Test d'une chaîne
message = "Bonjour"
hash_value = hash_obj.calculate_sha256(message)

print(f"SHA256('{message}') = {hash_value}")