import time
import os


def print_banner(text):
    # Define a simple ASCII art banner
    banner = r"""
   ____                 
 |  _ \ __ _ _ __ __    __ _ ___ _ ____  ____
 | |_) / _ \| '_ \| |  | |  / _ \| '__|/ /   | |
 |  _ < (_| | |  | \_ / | ( (_| | |  | |   | |
 |_| \_\__,_|_|   \___/   \__,_|_|  |_|   |_|
                   | |
                   | |
    """
    print(banner)


def get_valid_input(prompt, validate=lambda x: True, error_message="Invalid input"):
    while True:
        user_input = input(prompt).strip()
        if validate(user_input):
            return user_input
        print(error_message)


def generate_wordlist():
    # Display the banner with your name
    print_banner("Rayan Keyword")

    # Record start time
    start_time = time.time()

    # Get basic user information
    first_name = get_valid_input("Enter your first name: ", lambda x: x.isalpha(), "Please enter a valid name.")
    last_name = get_valid_input("Enter your last name: ", lambda x: x.isalpha(), "Please enter a valid name.")
    nickname = get_valid_input("Enter your nickname: ")
    birth_year = get_valid_input("Enter your birth year: ", lambda x: x.isdigit() and len(x) == 4,
                                 "Please enter a valid year.")
    birth_month = get_valid_input("Enter your birth month (as a number): ", lambda x: x.isdigit() and 1 <= int(x) <= 12,
                                  "Please enter a valid month.")
    birth_day = get_valid_input("Enter your birth day: ", lambda x: x.isdigit() and 1 <= int(x) <= 31,
                                "Please enter a valid day.")
    favorite_color = get_valid_input("Enter your favorite color: ")

    # Get partner information
    partner_first_name = get_valid_input("Enter your partner's first name: ", lambda x: x.isalpha(),
                                         "Please enter a valid name.")
    partner_last_name = get_valid_input("Enter your partner's last name: ", lambda x: x.isalpha(),
                                        "Please enter a valid name.")
    partner_birth_year = get_valid_input("Enter your partner's birth year: ", lambda x: x.isdigit() and len(x) == 4,
                                         "Please enter a valid year.")
    partner_birth_month = get_valid_input("Enter your partner's birth month (as a number): ",
                                          lambda x: x.isdigit() and 1 <= int(x) <= 12, "Please enter a valid month.")
    partner_birth_day = get_valid_input("Enter your partner's birth day: ", lambda x: x.isdigit() and 1 <= int(x) <= 31,
                                        "Please enter a valid day.")

    # Get hobbies, games, sports, subjects, and movies
    hobbies = get_valid_input("Enter favorite hobbies separated by commas: ").split(',')
    games = get_valid_input("Enter favorite games separated by commas: ").split(',')
    sports = get_valid_input("Enter favorite sports separated by commas: ").split(',')
    subjects = get_valid_input("Enter favorite subjects separated by commas: ").split(',')
    movies = get_valid_input("Enter favorite movies separated by commas: ").split(',')

    # Get additional keywords
    additional_keywords = get_valid_input("Enter additional keywords separated by commas: ")
    keywords = [keyword.strip() for keyword in additional_keywords.split(',') if keyword.strip()]

    # Get minimum and maximum word length
    min_length = int(get_valid_input("Enter the minimum word length: ", lambda x: x.isdigit() and int(x) > 0,
                                     "Please enter a valid number."))
    max_length = int(get_valid_input("Enter the maximum word length: ", lambda x: x.isdigit() and int(x) > min_length,
                                     "Please enter a valid number."))

    # Base words list
    words = [
                first_name, last_name, nickname, favorite_color,
                partner_first_name, partner_last_name
            ] + keywords + hobbies + games + sports + subjects + movies

    # Remove any empty entries
    words = [word.strip() for word in words if word.strip()]

    # Generate combinations
    combinations = set()

    # Add base words
    combinations.update(words)

    # Add year, month, day for user and partner
    combinations.update([
        birth_year, birth_month, birth_day,
        partner_birth_year, partner_birth_month, partner_birth_day
    ])

    # Create basic combinations
    for word in words:
        combinations.add(word + birth_year)
        combinations.add(word + birth_month + birth_day)
        combinations.add(word + birth_day + birth_month)
        combinations.add(word + partner_birth_year)
        combinations.add(word + partner_birth_month + partner_birth_day)
        combinations.add(word + partner_birth_day + partner_birth_month)

    # Combine all possible pairs
    for word1 in words:
        for word2 in words:
            if word1 != word2:
                combinations.add(word1 + word2)
                combinations.add(word1 + birth_year + word2)
                combinations.add(word1 + word2 + birth_year)
                combinations.add(word1 + birth_month + birth_day + word2)
                combinations.add(word1 + partner_birth_year + word2)
                combinations.add(word1 + word2 + partner_birth_year)
                combinations.add(word1 + partner_birth_month + partner_birth_day + word2)

    # Generate variations with numbers
    for word in words:
        for number in range(100):
            combinations.add(word + str(number))
            combinations.add(str(number) + word)

    # Filter combinations by length
    filtered_combinations = {word for word in combinations if min_length <= len(word) <= max_length}

    # Sort combinations alphabetically
    wordlist = sorted(filtered_combinations)

    # Output the generated wordlist
    print("\nGenerated Wordlist:")
    for word in wordlist:
        print(word)

    # Optionally, write to a file
    save_to_file = get_valid_input("\nDo you want to save the wordlist to a file? (y/n): ", lambda x: x in ['y', 'n'],
                                   "Please enter 'y' or 'n'.")
    if save_to_file == 'y':
        filename = get_valid_input("Enter the filename: ")
        try:
            with open(filename, 'w') as file:
                for word in wordlist:
                    file.write(f"{word}\n")
            file_size = os.path.getsize(filename)
            # Record end time
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Wordlist saved to {filename}")
            print(f"Number of words generated: {len(wordlist)}")
            print(f"File size: {file_size} bytes")
            print(f"Time taken: {elapsed_time:.2f} seconds")
        except Exception as e:
            print(f"Error saving file: {e}")


if __name__ == "__main__":
    generate_wordlist()
