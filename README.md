# Morse Code Converter

This Python program converts regular text into Morse code. It utilizes a dictionary to map letters, numbers, and spaces to their Morse code equivalents. This is a simple and efficient tool for encoding text in Morse code.

## Usage

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/Kishanjaisoorya/Morse-code-convertor-python.git
   ```

2. Navigate to the project directory:

   ```
   cd morse-code-converter
   ```

3. Run the Python script:

   ```
   python morse_code_converter.py
   ```

4. Enter the text you want to convert to Morse code when prompted.

5. The program will display the Morse code representation of your input.

## Customization

You can customize the Morse code dictionary in the `morse_code_dict` variable within the `morse_code_converter.py` file to add support for additional characters or special symbols.

```python
# Define a dictionary that maps characters to Morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', ...,
    ' ': ' ',  # Add custom mappings here
}
```

## Example

```plaintext
Input: Hello, World!
Output: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.-- 
```

Feel free to modify and adapt this code for your projects as needed.

## License

This project is licensed under the MIT License.
```

Remember to replace `"Kishanjaisoorya"` in the clone command with your actual GitHub username and ensure you have a `LICENSE` file with the appropriate license text in your repository.