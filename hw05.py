"""
Name: Marla Amarsaikhan
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """Asks until the user gives A, B, or C, then returns it. """
    # remove the default return and add your code
    while True:
        text = input("Give me a single uppercase letter: ")
        # needs to be exactly one character
        if len(text) != 1:
            print("Error: it needs to be a single character.")
            continue
        # needs to be A, B, or C
        if not (text == "A" or text == "B" or text == "C"):
            print("Error: You provided the wrong character.")
            continue
        # passed both checks
        return text
            
def get_digit():
    """Asks until the user gives 1, 2, or 3, then returns it as a string."""
    # remove the default return and add your code
    while True:
        text = input("Give me an single number character: ")
        # needs to be only digits
        if not text.isdigit():
            print("Error: your input should be only digits.")
            continue
        # needs to be exactly 1, 2, or 3
        if not (text == "1" or text == "2" or text == "3"):
            print("Error: a single digit needs to be in [1,3].")
            continue
        return text
        
def check_pattern(letter, digit, lst):
    """ """
    # remove the default pass and add your code
    pass


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()