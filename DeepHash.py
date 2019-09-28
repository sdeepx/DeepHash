import hashlib as hl
from Banner import banner
from Banner import process
import time as t


__author__ = "Shubhadeep"
__version__ = 1.2

banner.banner_hash()


def value(inp):
    inp = inp

    def options():
        print('''
                                  [+] Choose a Hashing option for Encryption :
                                             ______________________________
                                                            |
                                                1) Md5      |   2) SHA1
                                                            |
                                                3) SHA224   |   4) SHA256
                                                            |
                                                5) SHA384   |   6) SHA512
                                                            |
                                             _______________|______________

                ''')

        option = input(" : ")
        len_opt = len(option)
        if len_opt == 0:
            print("[-] Umm! I think you forgot to enter the option")
            return options()
        elif option == "1":
            process.process()
            md5_hash = hl.md5(inp.encode()).hexdigest()
            t.sleep(0.4)
            return "md5 of {} = {}".format(inp, md5_hash)
        elif option == "2":
            process.process()
            print()
            sha1_hash = hl.sha1(inp.encode()).hexdigest()
            t.sleep(0.4)
            return "sha1 of {} = {}".format(inp, sha1_hash)
        elif option == "3":
            process.process()
            print()
            sha224_hash = hl.sha224(inp.encode()).hexdigest()
            t.sleep(0.5)
            return "sha224 of {} = {}".format(inp, sha224_hash)
        elif option == "4":
            process.process()
            print()
            sha256_hash = hl.sha256(inp.encode()).hexdigest()
            t.sleep(0.5)
            return "sha256 of {} = {}".format(inp, sha256_hash)
        elif option == "5":
            process.process()
            print()
            sha384_hash = hl.sha384(inp.encode()).hexdigest()
            t.sleep(0.6)
            return "sha384 of {} = {}".format(inp, sha384_hash)
        elif option == "6":
            process.process()
            print()
            sha512_hash = hl.sha512(inp.encode()).hexdigest()
            t.sleep(0.7)
            return "sha512 of {} = {}".format(inp, sha512_hash)
        else:
            print("[-] You chose a wrong value")
            return options()

    if __name__ == '__main__':
        process.box_1()
        print(options())
        process.box_1()


def main():
    print("[+]  Enter the value for Encryption - \n")
    inp = input(" : ")
    len_inp = len(inp)
    if len_inp == 0:
        print("[-] Umm! I think you forgot to enter the value\n")
        return main()
    else:
        value(inp)
    return again()


def again():
    _again_ = input("Hash again? y(yes) n(no) : ")
    if len(_again_) == 0:
        print("Ops! You didn't chose any option! Choose y or n : \n")
        return again()
    elif _again_ == "yes" or _again_ == "y" or _again_ == "Y":
        print("Ok then. \n")
        return main()
    elif _again_ == "no" or _again_ == "N" or _again_ == "n":
        print("Thanks to use DeepHash..")
        return None
    else:
        print("[-] You did something wrong. Do it right :p \n")
        return again()


if __name__ == '__main__':
    main()
