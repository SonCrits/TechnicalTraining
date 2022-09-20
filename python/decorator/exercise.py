import re
import list_email

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,})+')

def check_valid(func):
    def wraper(email_list):
        for email in email_list:
            func(email)
            print(f"{email}  is valid")
    return wraper

@check_valid
def isValid(email):
    list_email_valid = []
    if re.fullmatch(regex, email):
      list_email_valid.append(email)
    return list_email_valid

a = isValid(list_email.list_email)
