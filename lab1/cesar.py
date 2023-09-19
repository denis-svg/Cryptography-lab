import string
import argparse

class Cesar:
    @staticmethod
    def permutate(alphabet:dict, k2:str):
        computed_alphabet = {}
        # adding the key in the alfabet
        i = 0
        for letter in k2:
            if letter not in computed_alphabet:
                computed_alphabet[letter] = str(i)
                i += 1

        # adding the letters that are missing from the alfabet
        for key in alphabet.keys():
            if key not in computed_alphabet:
                computed_alphabet[key] =  str(i)
                i += 1
        return computed_alphabet

    @staticmethod
    def encrypt(sypher:str, alphabet:dict, k1:int, k2=None):
        """
            {key:value}
            key - letter
            value - range integer from 0..inf
        """
        if type(k1) is not int:
            raise Exception("Key must be a int")
        if k2 is not None:
            if type(k2) is not str:
                raise Exception("Key must be a string")  
            alphabet = Cesar.permutate(alphabet, k2)

        # Inverting value and key in the alphabet
        alphabet_inverted = {}
        for key in alphabet.keys():
            alphabet_inverted[alphabet[key]] = key

        encrypted_sypther = ""
        n = len(alphabet.keys())
        for letter in sypher:
            encrypted_sypther += alphabet_inverted[str(pow(int(alphabet[letter]) + k1, 1, n))]

        return encrypted_sypther

    @staticmethod
    def decrypt(sypher:str, alphabet:dict, k1, k2=None):
        return Cesar.encrypt(sypher, alphabet, -k1, k2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Caesar Cipher Encryption/Decryption')
    parser.add_argument('k1', type=int, help='Key for encryption/decryption')
    parser.add_argument('text', help='Text to encrypt/decrypt')
    parser.add_argument('--k2', help='Permutation key (optional)', default=None)
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the input text')
    parser.add_argument('--alf', action='store_true', help='Display alfabet', default=None)

    args = parser.parse_args()

    alfabet_dict = {}
    for index, letter in enumerate(string.ascii_lowercase):
        alfabet_dict[letter] = str(index)

    if args.alf:
        if args.k2 is not None:
            alf = Cesar.permutate(alfabet_dict, args.k2)
        else:
            alf = alfabet_dict
        for key in alfabet_dict.keys():
            print(key, end=" ")
        print()
    if args.decrypt:
        decrypted_text = Cesar.decrypt(args.text, alfabet_dict, int(args.k1), args.k2)
        print(f'Decrypted text: {decrypted_text}')
    else:
        encrypted_text = Cesar.encrypt(args.text, alfabet_dict, int(args.k1), args.k2)
        print(f'Encrypted text: {encrypted_text}')