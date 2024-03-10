def morse_encrypt(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

        ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'
    }

    encrypted_text = ' '.join(morse_code_dict.get(char.upper(), '') for char in text)
    return encrypted_text
def morse_decrypt(morse_code):
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z',

        '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',

        '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
        '-.--.': '(', '-.--.-': ')'
    }

    decrypted_text = ''.join(morse_code_dict.get(code, '') for code in morse_code.split())
    return decrypted_text


def main():

    text = "Hello World"
    encrypted_text = morse_encrypt(text)
    print("Encrypted:", encrypted_text)

    decrypted_text = morse_decrypt(encrypted_text)
    print("Decrypted:", decrypted_text)
if __name__=="__main__":
    main()