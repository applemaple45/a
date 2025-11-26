def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to my GitHub project."

def main():
    user = input("Enter your name: ")
    print(greet(user))

if __name__ == "__main__":
    main()
