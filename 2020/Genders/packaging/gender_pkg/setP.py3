def store():
    pss = input("Enter mysql password: ")
    file_object = open('passW.txt', 'w')
    file_object.write(pss)
    file_object.close()

def main():
    store()


if __name__ == "__main__":
    main()

