def main():
    name = input("What is your name? ")
    work(name)

def work(name):
    if name.strip().lower() == 'a':
        #strip() removes leading and trailing spaces
        #strip('mno') removes substring
        print("Hello old friend!")
    else:
        print(f"Nice to meet you {name}.")
        #print(f"") formats string
        print("My name is Python!")
        
main()
