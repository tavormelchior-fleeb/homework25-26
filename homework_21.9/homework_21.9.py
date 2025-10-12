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
        # read the file and split it into words, removing "/n" from the end
        file_contents = f.read()[:-1].split(" / ")
    index = 0
    words_lst = ["" for i in range(len(file_contents))]
    for word in file_contents:
        for ch in word.split(" "):
            try:
                words_lst[index] += morse_to_english[ch]
            except KeyError:
                print("error in morse code")
                return

        index += 1
    print(" ".join(words_lst))


read_morse_file("morse1.txt")
read_morse_file("morse2.txt")
read_morse_file("morse-err1.txt")
read_morse_file("morse-err2.txt")





