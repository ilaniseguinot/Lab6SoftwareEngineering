# ilani seguinot
def main():
    encoded_password = ""
    # print menu options
    print("Menu")
    print("------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    # ask for user input
    user_option = int(input("Please enter an option: "))
    running = True
    # encode option
    while running:
        if user_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored")
        # decode option
        elif user_option == 2:
            decode(encoded_password)
            print(f"The encoded password is ")
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



if __name__ == '__main__':
    main()



