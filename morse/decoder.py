from morse.mapping import MORSE

REVERSE_MORSE = {value: key for key, value in MORSE.items()}
def decode_word(morse_letter):
    return REVERSE_MORSE[morse_letter]


def decode(morse_code):
    words = morse_code.split("|")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_letters = []

        for letter in letters:
            decoded_letters.append(decode_word(letter))

        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)


if __name__ == "__main__":
    text = "HELLO WORLD"
    from morse.encoder import encode

    morse = encode(text)
    print("Morse:", morse)
    print("Decoded:", decode(morse))
