import sys
import crypt

def crack():

    if len(sys.argv) !=2 :
     print("Not valid")
     return(1)

    hash = sys.argv[1]
    salt = hash[0:2:1]
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for first in alphabets:
        for second in alphabets:
            for third in alphabets:
                for fourth in alphabets:
                    for fifth in alphabets:

                        candidate = f"{first}{second}{third}{fourth}{fifth}".strip()

                        if crypt.crypt(candidate,salt) == hash:
                            print(candidate)
                            return(0)


crack()