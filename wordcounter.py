python
def word_count(input_text):
    """
    Function to count the number of words in the input text.

    Parameters:
    input_text (str): The input sentence or paragraph.

    Returns:
    int: The count of words in the input text.
    """
    words = input_text.split()
    return len(words)

def main():
    # Prompt the user for input
    user_input = input("Enter a sentence or paragraph: ")

    try:
        # Check for empty input
        if not user_input.strip():
            raise ValueError("Input is empty. Please enter a valid sentence or paragraph.")

        # Call the word_count function and display the result
        count = word_count(user_input)
        print(f"Word count: {count}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()


