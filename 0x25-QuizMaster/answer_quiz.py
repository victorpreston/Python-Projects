import requests
import random
import html

def get_questions(amount: int, category: int) -> dict:
    """
    Retrieves trivia questions from the Open Trivia Database API.

    Args:
        amount (int): Number of questions to retrieve (maximum 50).
        category (int): Category ID of the questions.

    Returns:
        dict: Dictionary containing the retrieved trivia questions.
    """
    url = f'https://opentdb.com/api.php?amount={amount}&category={category}'
    response = requests.get(url).json()
    return response

def shuffle_choices(choices: list) -> list:
    """
    Shuffles the order of choices for a trivia question.

    Args:
        choices (list): List of choices for a trivia question.

    Returns:
        list: Shuffled list of choices.
    """
    random.shuffle(choices)
    return choices

def get_user_response(num_choices: int) -> int:
    while True:
        try:
            response = int(input('Enter your answer: '))
            if 1 <= response <= num_choices:
                return response
            else:
                print('Invalid input. Please enter a number between 1 and', num_choices)
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

def display_choices(choices: list) -> None:
    """
    Displays the choices for a trivia question with index numbers.

    Args:
        choices (list): List of choices for a trivia question.

    Returns:
        int: Index of the user's response.
    """
    num_choices = len(choices)
    for index, choice in enumerate(choices, start=1):
        formatted_choice = f"{index}. {html.unescape(choice)}"
        print(formatted_choice)
    return get_user_response(num_choices)

def get_user_input() -> int:
    """
    Gets the number of questions the user wants to attempt.

    Returns:
        int: Number of questions chosen by the user.
    """
    while True:
        try:
            user_input = int(input('How many questions would you like to attempt (1-50): '))
            if 1 <= user_input <= 50:
                return user_input
            else:
                print('Invalid input. Please enter a number between 1 and 50.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

def main():
    """
    Main function to run the trivia quiz application.
    """
    score = 0  # Initialize score
    try:
        num_questions = get_user_input()
        trivia_data = get_questions(num_questions, 18)  # Category ID 9 corresponds to General Knowledge
        questions = trivia_data.get('results')

        for question_data in questions:
            question = html.unescape(question_data.get('question'))
            correct_answer = html.unescape(question_data.get('correct_answer'))
            incorrect_answers = [html.unescape(answer) for answer in question_data.get('incorrect_answers')]
            incorrect_answers.append(correct_answer)
            shuffled_choices = shuffle_choices(incorrect_answers)

            print(question)
            user_response_index = display_choices(shuffled_choices) - 1 # Adjusting index to start from 0
            user_response = shuffled_choices[user_response_index]
            if user_response == correct_answer:
                score += 1  # Increment score for correct answer
                print('Congratulations! Your answer is correct.\n')
            else:
                print(f'Sorry, the correct answer is: {correct_answer}\n')

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}. Please check your internet connection.")
    finally:
        print(f'Your final score is: {score}/{num_questions}')  # Display final score

if __name__ == "__main__":
    main()
