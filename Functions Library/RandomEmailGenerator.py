# To generate random email IDs
import random
import string


def random_email(n):   # n is length of email id excluding domain

    # can use below line if want to accept domain name as input, then, email_id = email_id+domain
    #domain = input("Key in domain name [Ex: @gmail.com, @yahoo.com] :-")

    choice = string.ascii_lowercase + str("0123456789.")
    email_id = random.choice(string.ascii_lowercase)   # First character of email id should be a letter
    for x in range(n-1):                                # using n-1 because 1 character already added in line#9
        email_id = email_id+(random.choice(choice))
    email_id = email_id + "@gmail.com"
    return email_id

print(random_email(8))