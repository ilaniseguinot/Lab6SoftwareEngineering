# ilani seguinot
def main():
    encoded_password = ""
    running = True
    # encode option
    while running:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        # print menu options
        user_option = int(input("Please enter an option: "))
        # ask for user input
        if user_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored")
        # decode option
        elif user_option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the decoded password is {decoded_password}.")
        # quit option
        else:
            quit()


def encode(password):
    password_list = []
    password_string = ""
    for i in password:
        password_list.append(int(i))
    for j in range(len(password_list)):
        password_list[j] = password_list[j] + 3
    for k in range(len(password_list)):
        password_string += str(password_list[k])
    return password_string


def decode(password):
    decoded_password = ''
    for digit in password:
        decoded_digit = str(int(digit) - 3)
        decoded_password = decoded_password + decoded_digit
    return decoded_password
# Brian Delaney decode function.
# Function uses a for loop to go character by character in the encoded password, convert it to a digit and subtracts
# 3 from it, then converts it back into a string and concatenates it to the full decoded password.


if __name__ == '__main__':
    main()
