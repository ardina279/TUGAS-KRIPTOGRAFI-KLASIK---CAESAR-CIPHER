def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = (ord(char) - ord('a') + shift) % 26
            encrypted_char = chr(shifted + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def display_alphabets(shift):
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = original_alphabet[shift:] + original_alphabet[:shift]
    original_alphabet_upper = original_alphabet.upper()
    shifted_alphabet_upper = shifted_alphabet.upper()
    return original_alphabet_upper, shifted_alphabet_upper

# Meminta input dari pengguna
plaintext = str(input("Masukkan Kata : "))
shift = int(input("Masukkan pergeseran : "))

# Memanggil fungsi caesar_cipher untuk mengenkripsi pesan
encrypted_text = caesar_cipher(plaintext, shift)
print(f"Pesan Terenkripsi: {encrypted_text}")

# Memanggil fungsi caesar_decipher untuk mendekripsi pesan
decrypted_text = caesar_decipher(encrypted_text, shift)
print(f"Pesan Terdekripsi: {decrypted_text}")

# Memanggil fungsi display_alphabets untuk menampilkan alfabet
original_alphabet, shifted_alphabet = display_alphabets(shift)

print(f"Original Alphabet: {original_alphabet}")
print(f"Shifted Alphabet: {shifted_alphabet}")