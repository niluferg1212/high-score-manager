import csv
file =  "high_score_manager.py"

def write_scores():
    scores = [] # Initialize an empty list to store score 
    try:
        # To read the data from the file in read mode
        with open(file, "r", newline="") as file:
            lines = file.readlines() # To read all lines from the file
            reader = [] # To initialize an empty list to store the processed lines
            for line in lines:
                # To strip the whitespace and split each line by comma 
                reader.append(line.strip().split(','))
            for row in reader:
                # If the row has exactly two elements (name and score)
                if len(row) == 2:
                    name = row[0] # The first element mayy be set as the name
                    score = row[1] # The second element may be set as the score
                    if score.isdigit(): # Check if score is a digit
                        scores.append((name, int(score))) # Append the name and score as a tuple
    except FileNotFoundError:
        pass # If the file is absent just pass
    return scores # Return the list of scores

def save_score(scores):
        # To open the file in the write mode
        with open(file, "w", newline="") as file:
            writer = csv.writer(file) # To create an object of CSV writer
            for name, score in scores:
                row = [name, score] # To create a row list
                writer.writerow(row) # To write the row to the file

def bubble_sort(scores):
    n = len(scores) # To obtain the number of scores
    # Use the bubble sort algorithm to sort scores in descending order
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if scores[j][1] < scores[j + 1][1]: # To compare the scores
                scores[j], scores[j + 1] = scores[j + 1], scores[j] # To swap if necessary

def add_or_update_score():
    name = input("Type the player's name: ") # To ask for the name of player 
    while not name:
        name = input("Error: Please proivde a name.") # To make sure that the name is not empty

    score_input = input("Enter the final score: ") # To ask for the score
    if not score_input.isdigit():
        print("Error: Enter a valid number for the score.") # To validate score input
        return
    
    score = int(score_input) # To convert score input to an integer

    score_list = write_scores() # To read existing scores
    score_dict = {player: scr for player, scr in score_list} # To create a dictionary of the scores

    # To check if the player's name exists in the dictionary
    if name in score_dict:
        if score > score_dict[name]: # To update the score if the new score is higher
            print(f"{name}'s previous score of {score_dict[name]} will be updated to {score}.")
            score_dict[name] = score
        else:
            print("{name}'s current score of {score_dict[name]}is already higher or equal. Update not applied.")
    else:
        score_dict[name] = score # To add the new player to the dictionary
        print("{name} is a new entry with a score of {score}.")

    # To sort the scores in descending order and save
    sorted_score = sorted(score_dict.items(), key =lambda x: x[1], reverse=True)
    save_score(sorted_score)

def search_score():
    name = input("Search for a player's name: ") # To prompt for a player's name
    scores = write_scores() # To read existing scores

    # To search for the player's score
    for player, score in scores:
        if player.lower() == name.lower(): # Search is case insensitive
            print("The score of {player} is {score}")
            return
    print("Player with that name does not exist.") # If found nothing

def read_file():
    try:
        # In read mode open a file
        with open("high_score_manager.py", "r") as file:
            content = file.read() # Get the entire contents of the file
            if content:
                print("\nThe roboot retrieved the following information:\n" + content)
            else: 
                print("\nThe file is currently empty.") # To check if the file was empty
    except FileNotFoundError:
        print("\nThe robot was unble to locate the file.") # To handle the file not found error

def write_sentence():
    sentence = input("\nPlease enter a sentence:\n") # To prompt the user for a sentence
    if isinstance(sentence, str) and sentence: # To check if the input is valid
        try: 
            # In append mode open a file
            with open("high_score_manager.py", "a") as file:
                file.write(sentence + "\n") # Write the sentence in the file
                print("Your sentence has been successfully saved!") # The confirmation message for the user
        except Exception as e: 
            print("\nAn error occured: {e}") # To handle exceptions
    else:
        print("\nInvalid input. Please provide a valid sentence.") # To handle invalid input

def clear_file():
    try:
        # To open the file in write mode to clear the content
        with open("high_score_manager.py", "w") as file:
            file.truncate() # To clear the file content
        print("\nThe robot has cleared all contents from the file.") # The confirmation message for the user
    except Exception as e:
        print("\nAn error occured: {e}") # To handle exceptions


def display_scores():
    scores = write_scores() # To read te scores that are existing

    print("\n-------------------------------------------")
    print("High Score Board: ")
    print("\n-------------------------------------------")

    if not scores:
        print("No scores available.") # To check the conditions where there are no scores
    else:
        rank = 1 # Initializing the counter for the rank
        for score_tuple in scores:
            name, score = score_tuple # Unpacking the score tuple
            print(f"{rank}. {name}: {score}") # Showing the rank, name and the score
            rank += 1 # Counting the rank up

def main():
    while True:
        print("\nHigh Score Manager")
        print("1. Add or update high score") # The option to add or update the score
        print("2. Search score by name") # The option to search for a score 
        print("3. View high scores") # The option to view scores
        print("4. Exit") # The program will exit

        choice = input("Enter your choice (1-4): ") # The user's choice is taken

        # The system responds to the user choice requests 
        if choice == '1':
            add_or_update_score() # The function is called to add/update the score
        elif choice == '2':
            search_score() # The function is called to search for the score
        elif choice == '3':
            display_scores() # The function is called to display the score
        elif choice == '4':
            print("Goodbye!") # Exit message
            break # Exit the loop
        else:
            print("Invalid choice. Please try again.") # The invalid choice is handled


if __name__ == "__main__":
    main()