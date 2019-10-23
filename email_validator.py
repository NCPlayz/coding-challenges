from tkinter import filedialog

def valid(email):
    print(email)
    if " " in email:
        print("There is a space in that email.")
        return False
    if not "@" in email:
        print("There is no @ in that email.")
        return False
    first, second = email.split("@")
    if "." not in second:
        print("There is no . after the @.")
        return False
    second, third = second.split(".")
    if not len(first):
        print("The part of the email before @ is blank.")
        return False
    elif not len(second):
        print("The part of the email between @ and . is blank.")
        return False
    elif not len(third):
        print("The part of the email after . is blank.")
        return False
    print("Valid email address.")
    return True

if __name__ == "__main__":
    singular = input("Singular or Multiple? :").lower() == "singular"
    if singular:
        email = input("What is the email address? :")
        valid(email)
    else:
        fp = filedialog.askopenfilename(title="Select .txt File", filetypes=(("Text Files","*.txt"),))
        with open(fp) as f:
            for line in f.readlines():
                valid(line)
