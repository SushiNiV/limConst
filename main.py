from logic import limConst

def main():
    userInput = input("Enter a constant: ")  
    result = limConst(userInput)
    print(f"The limit is: {result}")

if __name__ == "__main__":
    main()