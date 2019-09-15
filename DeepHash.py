__author__ = "Shubhadeep"
__version__ = 1.0
__company__ = "DeepLab"

'''MD5: Message digest algorithm producing a 128 bit hash value.
 This is widely used to check data integrity.
 It is not suitable for use in other fields due to the security vulnerabilities of MD5.'''

'''SHA: Group of algorithms designed by the U.S's NSA that are part of the U.S Federal Information processing standard. 
These algorithms are used widely in several cryptographic applications. 
The message length ranges from 160 bits to 512 bits.'''

print('''
                                                                    
    *******     **********  **********  *****      **       **   *****     ******    **       **
    **    **    **********  **********  **   **    **       **  **   **   **     **  **       **
    **     **   **          **          **   **    *** * * ***  **   **    **    **  *** * * ***
    **     **   *******     *******     *****      ***********  *******      **      ***********
    **     **   **          **          **         *** * * ***  *******  **    **    *** * * ***
    **    **    **********  **********  **         **       **  **   **  **    **    **       **
    ******      **********  **********  **         **       **  **   **   ******     **       **
      
''')

import hashlib as hl

def Hashing(hash):


    print('''
        [+] Chose a Hashing option for Encryption :
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
    hash_option = input(" : ")
    lenh = len(hash_option)
    if lenh == 0:
        print( " [-] You didn't enter any option")
        return main()

    elif hash_option == "1":
        print("Please wait .. .. .. .. .. .. .. .. . .. . .. .. . .")
        print()
        md5_hash = hl.md5(hash.encode()).hexdigest()
        return "md5 of {} = {}".format(hash,md5_hash)

    elif hash_option == "2":
        print("Please wait .. .. .. .. .. .. .. .. . .. . .. .. . .")
        print()
        sha1_hash = hl.sha1(hash.encode()).hexdigest()
        return "sha1 of {} = {}".format(hash,sha1_hash)

    elif hash_option == "3":
        print("Please wait .. .. .. .. .. .. .. .. . .. . .. .. . .")
        print()
        sha224_hash = hl.sha224(hash.encode()).hexdigest()
        return "sha224 of {} = {}".format(hash,sha224_hash)

    elif hash_option == "4":
        print("Please wait .. .. .. .. .. .. .. .. . .. . .. .. . .")
        print()
        sha256_hash = hl.sha256(hash.encode()).hexdigest()
        return "sha256 of {} = {}".format(hash,sha256_hash)

    elif hash_option == "5":
        print("Please wait .. .. .. .. .. .. .. .. . .. . .. .. . .")
        print()
        sha384_hash = hl.sha384(hash.encode()).hexdigest()
        return "sha384 of {} = {}".format(hash, sha384_hash)

    elif hash_option == "6":
        print("Please wait .. .. .. .. .. .. .. .. . .. . .. .. . .")
        print()
        sha512_hash = hl.sha512(hash.encode()).hexdigest()
        return "sha512 of {} = {}".format(hash, sha512_hash)
    else:
        return "[-] You entered a Wrong Value"

def main():
    print("{+} Enter Your Input For Encryption - ")
    hash_inp = input(" : ")
    lenhi = len(hash_inp)
    if lenhi == 0:
        print("[-] You didn't enter any Input")
        return main()
    else:
     print(Hashing(hash_inp))
if __name__ == '__main__':
    main()