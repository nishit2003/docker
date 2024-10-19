# Nishit Grover
# Project 3: Docker

import re
from collections import Counter
import socket
import os

# Input and Output Files
text_file_1 = "/home/data/IF.txt"
text_file_2 = "/home/data/AlwaysRememberUsThisWay.txt"
generated_text_file = "/home/data/output/result.txt"

# Reading both the text files
def read_text_files(file):
    with open(file, 'r') as file:
        return file.read().upper()

# Handling special characters
def special_characters(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Number of words counter
def counter(text):
    words = text.split()
    return len(words)

# Frequency of words
def word_occurrences(text):
    text = special_characters(text)
    words = text.upper().split()
    return Counter(words)

# Handling contractions and update using the for loop by replacing the contractions with the individual words
def extract_contractions(text):
    contractions = {
        "IT'S": "It is",
        "COULDN'T": "could not",
        "I'M": "I am",
        "CAN'T": "can not",
        "WON'T": "will not",
        "I'LL": "I will",
        "DON'T": "do not",
        "YOU'RE": "You are",
        "THAT'S": "that is"
    }
    for contraction, new_string in contractions.items():
        text = text.replace(contraction, new_string)
    return text

# IP Address
def IP_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Including all the functions in the main function
def main():
    # Requirements of the Project 3
    file_1 = read_text_files(text_file_1)
    file_2 = read_text_files(text_file_2)
    total_words_file_1 = counter(file_1)
    total_words_file_2 = counter(file_2)
    updated_file_2 = extract_contractions(file_2)
    updated_total_words_file_2 = counter(updated_file_2)
    grand_total = total_words_file_1 + total_words_file_2
    updated_grand_total = total_words_file_1 + updated_total_words_file_2
    frequent_words_and_counts = word_occurrences(file_1).most_common(3)
    updated_frequent_words_and_counts = word_occurrences(updated_file_2).most_common(3)
    ip_address = IP_address()

    # Open the file and write the contents
    with open(generated_text_file, 'w') as output_file:
        output_file.write(f"Total Number of Words in IF.txt: {total_words_file_1}\n")
        output_file.write(f"Total Number of Words in AlwaysRememberUsThisWay.txt: {total_words_file_2}\n")
        output_file.write(f"Grand Total of Words in both files: {grand_total}\n")
        output_file.write(f"Top 3 Most Frequent Words and Respective Counts in IF.txt: {frequent_words_and_counts}\n\n")
        output_file.write(f"'Splitting Contractions into Individual Words in AlwaysRememberUsThisWay.txt'\n\n")
        output_file.write(f"Updated Total Number of Words in AlwaysRememberUsThisWay.txt: {updated_total_words_file_2}\n")
        output_file.write(f"Updated Grand Total Number of Words in both files: {updated_grand_total}\n")
        output_file.write(f"Top 3 Most Frequent Words and Respective Counts in updated AlwaysRememberUsThisWay.txt: {updated_frequent_words_and_counts}\n")
        output_file.write(f"IP Address: {ip_address}")

    # Open the file and read the contents
    with open(generated_text_file, 'r') as file_with_contents:
        print(file_with_contents.read())

if __name__ == "__main__":
    # Create the output directory, if none already exists
    os.makedirs("/home/data/output", exist_ok=True)
    main()