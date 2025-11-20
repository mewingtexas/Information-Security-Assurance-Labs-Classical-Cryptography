def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key = key.lower()
    key_len = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_len]) - ord('a')
            if char.isupper():
                base = ord('A')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            else:
                base = ord('a')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted.append(decrypted_char)
            key_index += 1
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Ciphertext
ciphertext = """Ruy gpzwh xj afoz qt Tckrbd ou xuqt hz fwthitc uwx ucqiq ufptkez? W ejwop uskhdobr c 
pjys uy kcz oe vvf zgvkr uvce ycvqr co g iuco krff."""

# List of possible keys
keys = [
    "Vxpcijcdxhujc",
    "Kgcgolcobfob",
    "Qggvoqyghsf",
    "Oddzswgpshhsf",
    "Gjfwhfygtzsi",
    "Qmpsfohiq"
]

# Try each key
for key in keys:
    print(f"\n🔑 Trying key: {key}")
    print(vigenere_decrypt(ciphertext, key))
