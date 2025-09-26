import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from aesgestion import AesGestion

# Crée une instance
aes_obj = AesGestion()

# Génère une clé AES
aes_obj.generate_aes_key()

# Message à chiffrer
message = "Bonjour AES"

# Chiffrement
encrypted = aes_obj.encrypt_string_to_base64(message)
print(f"Message chiffré : {encrypted}")

# Déchiffrement
decrypted = aes_obj.decrypt_string_from_base64(encrypted)
print(f"Message déchiffré : {decrypted}")