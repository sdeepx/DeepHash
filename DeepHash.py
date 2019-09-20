import hashlib as hl
from Banner import banner
from Banner import process
import time as t


__author__ = "Shubhadeep"
__version__ = 1.1

banner.banner_hash()


def value(inp):
    len_inp = len(inp)
    if len_inp == 0:
        print("[-] Umm! I think you forgot to enter the value")
        return main()
   

def main():
    print("[+]  Enter the value for Encryption - ")
    inp = input(" : ")
    value(inp)

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
            t.sleep(0.5)
            return "md5 of {} = {}".format(inp, md5_hash)
        elif option == "2":
            process.process()
            print()
            sha1_hash = hl.sha1(inp.encode()).hexdigest()
            t.sleep(0.5)
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
            t.sleep(0.6)
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
            t.sleep(0.6)
            return "sha512 of {} = {}".format(inp, sha512_hash)
        else:
            print("[-] You chose a wrong value")
            return options()

    if __name__ == '__main__':
        process.box_1()
        print(options())
        process.box_1()


if __name__ == '__main__':
    main()
