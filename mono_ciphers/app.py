import caesar


def main_menu():
    print("\n===========================")
    print("   MONOALPHABETIC CIPHER")
    print("===========================\n")
    print("1. Encrypt - Shifted Caesar")
    print("2. Decrypt - Shifted Caesar")
    print("3. Encrypt from file - Shifted Caesar")
    print("0. Exit")
    print("===========================\n")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            caesar.process_from_input(mode=0)
            print("\n===========================")
        elif choice == "2":
            caesar.process_from_input(mode=1)
            print("\n===========================")
        elif choice == "3":
            caesar.process_from_file(mode=0)
            print("\n===========================")
        elif choice == "4":
            caesar.process_from_file(mode=1)
            print("\n===========================")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
