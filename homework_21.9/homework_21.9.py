# morse dict from internet
morse_to_english = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '---...': ':',
    '-.-.-.': ';', '-....-': '-', '.-..-.': '"', '.-.-.': '+',
    '-..-.': '/', '.-.-..': '@', '-.--.': '(', '-.--.-': ')',
    '...-.-': 'SOS'
        }


def read_morse_file(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read().split("/")
    index = 0
    words_lst = ["" for i in range(len(file_contents))]
    for word in file_contents:
        for ch in word:
            if ch not in morse_to_english.keys():
                print("Error in Morse Code")
                return
            else:
                words_lst[index] += ch
        index += 1
    print(" ".join(words_lst))



read_morse_file("")





