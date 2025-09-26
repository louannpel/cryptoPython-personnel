import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from rsagestion import RsaGestion

# Création d'une instance
rsa_obj = RsaGestion()

# Génération des clés (fichiers temporaires)
rsa_obj.generation_clef("public.pem", "prive.pem", 2048)

# Chargement des clés depuis les fichiers
rsa_obj.chargement_clefs("public.pem", "prive.pem")

# Message à chiffrer
message = "Bonjour RSA"

# Chiffrement
encrypted = rsa_obj.chiffrement_rsa(message)
print(f"Message chiffré : {encrypted}")

# Déchiffrement
decrypted = rsa_obj.dechiffrement_rsa(encrypted)
print(f"Message déchiffré : {decrypted}")
