import ecdsa
from hashlib import sha256

random_number_for_private_key = 31334737451456268050498185842994455999554006395290392504114029053954839148697
private_key_hex = hex(random_number_for_private_key)[2:]
private_key_bytes = bytes.fromhex(private_key_hex)
private_key_object=ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1, hashfunc=sha256)

sig = private_key_object.sign(b"it is a message")

print(sig.hex())
