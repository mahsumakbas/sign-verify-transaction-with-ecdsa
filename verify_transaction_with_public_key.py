import ecdsa
from hashlib import sha256
message = b"it is a message"
public_key = '46454399998223bdb3771f08341844c485cd6b0e35383635cbc56940a755e5b6986ef0dbd1381267575bf290843540d3061f089fbab1b8f60cfe3d3d0d6aef52'
sig = '969f6829ed34f3fdc9333271f35b1abe4e70d21daa2ff62f5a4c2acd490cd0220fbecf7f87f14f35ed3547a9055decca4043eb9d820a8fc00626649199b17f68'

vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1, hashfunc=sha256)
vk.verify(bytes.fromhex(sig), message)