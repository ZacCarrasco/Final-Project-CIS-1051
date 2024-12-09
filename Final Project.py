#Python Thursday you will get to see how to input and output a file to redact info, 
#But I can use the basis to help with the final project: 
#   I am going to do the idea I had with the final project but have it also redact phone numbers

#finding Phone numbers in text

#        \d\d\d-\d\d\d-\d\d\d\d

#----------------------------------------
def wingdings():
    dictionary = {}
#opens the text2 file to create a dictionary out of it
    with open('test2.txt', 'r', encoding='utf8') as dictionary_file:
        dictionary_lines = dictionary_file.readlines()

#reads each line in the file and splits it into a key and value, then adds it to
    for line in dictionary_lines:
        line = line.strip()
        line = line.split(',')
        if len(line) == 2:
            key = line[0].strip('"')
            value = line[1].strip('"')
            dictionary[key] = value

#opens the input file and reads it line by line
    input_file = open('input.txt', 'r', encoding='utf8')
    output_file = open('output.txt', 'w', encoding='utf8')

#reads each line in the file and splits it into words, then splits each word into letters
    for line in input_file:
        line = line.strip()  # Remove leading/trailing whitespace from the line
        sentence = line.split(",")  # Split the line by comma
        translated_words = []  # List to hold translated words

# iterates over each word in the sentence
        for word in sentence:
            letters = list(word.strip())  # Split the word into individual letters
            translated_letters = []  # List to hold translated letters

#iterates over each letter in the word
            for character in letters:
                character = character.strip()  # Strip whitespace from each letter
                if character in dictionary:
#                    print(f"Translating '{character}' to '{dictionary[character]}'")  # Debug output
                    translated_letters.append(dictionary[character])  # Replace with translation
                else:
#                    print(f"'{character}' not found in dictionary.")  # Debug output for missing letters
                    translated_letters.append(character)  # Keep the original letter if not found

# join the translated letters back into a word and add it to the list of translated words
            translated_word = ''.join(translated_letters)  # Combine translated letters into a word
            translated_words.append(translated_word)  # Add the translated word to the list


# join the translated words back into a sentence and write it to the output file
        line = ",".join(translated_words)  # Join the translated words back together
        output_file.write(line + "\n")  # Write to output file

    input_file.close()
    output_file.close()
    print("The file is translated. Why would you want this? This code was utterly pointless")

import re

def redact_phone_number(infile, outfile):
    # Open the input file with utf-8 encoding
    with open(infile, 'r', encoding='utf-8') as data:
        text = data.read()

    # Correct regex pattern to match phone numbers in the format XXX-XXX-XXXX
    pattern = r"\d{3}-\d{3}-\d{4}"
    redacted = re.sub(pattern, "[SHHH THIS IS PRIVATE]", text)

    # Open the output file with utf-8 encoding
    with open(outfile, 'w', encoding='utf-8') as writer:
        writer.write(redacted)

def redact_social(infile,outfile):
    # Open the input file with utf-8 encoding
    with open(infile, 'r', encoding='utf-8') as data:
        text = data.read()

    # Correct regex pattern to match phone numbers in the format XXX-XXX-XXXX
    pattern = r"\d{3}_\d{2}_\d{4}"
    redacted = re.sub(pattern, "[HEY DONT LOOK HERE]", text)

    # Open the output file with utf-8 encoding
    with open(outfile, 'w', encoding='utf-8') as writer:
        writer.write(redacted)


# Call the function with the appropriate file names
def main():
    wingdings()
    redact_phone_number('output.txt', 'output.txt')
    redact_social('output.txt', 'output.txt')

main()

print("so here we have the most pointless code that I have ever created \n"
      "I have no idea why I would ever do this again but hey here it is"
      )