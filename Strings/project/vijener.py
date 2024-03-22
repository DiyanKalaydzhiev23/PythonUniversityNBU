class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def repeat_key(self, text):
        return (self.key * (len(text) // len(self.key)) + self.key[:len(text) % len(self.key)]).upper()

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        repeated_key = self.repeat_key(plaintext)
        ciphertext = ''

        for p, k in zip(plaintext, repeated_key):
            if p.isalpha():
                c = (ord(p) + ord(k) - 2 * ord('A')) % 26 + ord('A')
                ciphertext += chr(c)
            else:
                ciphertext += p

        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        repeated_key = self.repeat_key(ciphertext)
        plaintext = ''

        for c, k in zip(ciphertext, repeated_key):
            if c.isalpha():
                p = (ord(c) - ord(k)) % 26 + ord('A')
                plaintext += chr(p)
            else:
                plaintext += c

        return plaintext

