# Define a dictionary that maps letters and numbers to Morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '
}

def text_to_morse_code(text):
    # Convert the text to uppercase to handle both uppercase and lowercase characters
    text = text.upper()
    
    morse_code = []
    
    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(char)  # Preserve characters not in the dictionary as is
    
    return ' '.join(morse_code)

# Get user input for the text to convert to Morse code
input_text = input("Enter the text you want to convert to Morse code: ")
morse_code_result = text_to_morse_code(input_text)

print("Morse Code:")
print(morse_code_result)
