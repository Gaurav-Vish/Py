def main():
    name = input("What is your name? ")
    work(name)


def work(name):
    if name.strip().lower() == 'a':
        print("Hello old friend!")
    else:
        print(f"Nice to meet you {name}.")
        print("My name is Python!")
        
main()
