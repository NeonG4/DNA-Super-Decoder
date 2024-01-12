import os, sys
dna_chars = ["a", "t", "c", "g"]

def check_data(stats):
    global dna_chars
    j = 0
    for i in stats:
        j += 1
        if dna_chars[0] != i and dna_chars[1] != i and dna_chars[2] != i and dna_chars[3] != i:
            return j
    return 0

def converttomrna():
    global dna
    global mrna 
    mrna = ""
    for i in dna:
        if i == "g":
            mrna += "c"
        if i == "c":
            mrna += "g"
        if i == "t":
            mrna += "a"
        if i == "a":
            mrna += "u"

def converttoprotein():
    global protein, mrna
    protein = ""
    tmp = ""
    for i in mrna:
        tmp += i
        if len(tmp) == 3:
            if tmp == "auu" or tmp == "auc" or tmp == "aua":
                protein += " \033[32mIsoleucine"
            elif tmp == "aug":
                protein += " \033[32mMethionine(start)"
            elif tmp == "acu" or tmp == "acc" or tmp == "aca" or tmp == "acg":
                protein += " \033[35mThreonine"
            elif tmp == "aau" or tmp == "aac":
                protein += " \033[35mAsparagine"
            elif tmp == "aaa" or tmp == "aag":
                protein += " \033[31mLysine"
            elif tmp == "agu" or tmp == "agc" or tmp == "ucu" or tmp == "ucc" or tmp == "uca" or tmp == "ucg":
                protein += " \033[35mSerine"
            elif tmp == "aga" or tmp == "agg" or tmp == "cgu" or tmp == "cgc" or tmp == "cga" or tmp == "cgg":
                protein += " \033[31mArginine"
            elif tmp == "guu" or tmp == "guc" or tmp == "gua" or tmp == "gug":
                protein += " \033[32mValine"
            elif tmp == "gcu" or tmp == "gcc" or tmp == "gca" or tmp == "gcg":
                protein += " \033[32mAlanine"
            elif tmp == "gau" or tmp == "gac":
                protein += " \033[34mAspartic_Acid"
            elif tmp == "gaa" or tmp == "gag":
                protein += " \033[34mGlutamic_Acid"
            elif tmp == "ggu" or tmp == "ggc" or tmp == "gga" or tmp == "ggg":
                protein += " \033[33mGlycine"
            elif tmp == "uuu" or tmp == "uuc":
                protein += " \033[32mPhenylalanine"
            elif tmp == "uua" or tmp == "uug" or tmp == "cuu" or tmp == "cuc" or tmp == "cua" or tmp == "cug":
                protein += " \033[32mLeucine"
            elif tmp == "uau" or tmp == "uac":
                protein += " \033[32mTyrosine"
            elif tmp == "uaa" or tmp == "uag" or tmp == "uga":
                protein += " \033[37mSTOP_PROTEIN_REACHED"
            elif tmp == "ugu" or tmp == "ugc":
                protein += " \033[33mCysteine"
            elif tmp == "ugg":
                protein += " \033[32mTryptophan"
            elif tmp == "ccu" or tmp == "ccc" or tmp == "cca" or tmp == "ccg":
                protein += " \033[33mProline"
            elif tmp == "cau" or tmp == "cac":
                protein += " \033[31mHistidine"
            elif tmp == "caa" or tmp == "cag":
                protein += " \033[35mGlutamine"
            else:
                protein += " \033[37mCOULDN'T_FIND_PROTEIN"
            tmp = ""


print("Hello World") # test thingies idk
os.system('CLS')
trials = 0
storeddna = []
storedrna = []
storedprotein = []

while True:
    trials += 1
    dna = input("What is your DNA data? ").lower()
    if len(dna)%3 != 0:
        print("Something ain't right... Your DNA strand doesn't have a number divisable by 3!")
    tmp = check_data(dna)
    if tmp != 0:
        print(f"Something ain't right... Your DNA strand has an invalid character at character {tmp}.")
    if tmp != 0 or len(dna)%3 != 0:
        sys.exit()


    print("Hi") #stupid thingy idk
    os.system('CLS')


    print("Converting into mRNA...")
    mrna = ""
    converttomrna()
    print(f"Your mRNA is:\n {mrna}")
    print("\n\nConverting to proteins!... ")
    protein = ""
    converttoprotein()
    print(f"The following sequence is your protein:\n{protein} \033[37m")
    print("\n\nThey are colored based on hydrophobic and hydrophilic as well as charge.")
    storeddna.append(dna)
    storedrna.append(mrna)
    storedprotein.append(protein)
    if trials > 1:
        action = input("Would you like to code for another protein(p), halt the program(h), or view previous data(d)? ").lower()
        os.system('CLS')
        if action == "d":
            j = 0
            for i in storeddna:
                j += 1
                print(f"\033[0mDNA of item {j}:\n{storeddna[j-1]}\nmRna of item {j}:\n{storedrna[j-1]}\nProtein(s) of item {j}:\n{storedprotein[j-1]}\n\n")
            print("\033[0m")
            input("\n\n\nType enter to exit...")
            os.system('CLS')
    else:  
        action = input("Would you like to code for another protein(p) or halt the program(h)? ").lower()
        os.system('CLS')
    if action == "h":
        sys.exit()
    elif action == "d":
        pass
    elif action != "p":
        print(f"Sorry. I'm a dumb computer and I didn't understand {action}. I'll pretend it was a p. ;)")
