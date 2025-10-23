import string
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment.setttings import WORD_LENGTH, RAW_WORDLIST_PATH, PROCESSED_WORDLIST_PATH

f = open(RAW_WORDLIST_PATH,"r")
f2 = open(PROCESSED_WORDLIST_PATH,"w")
for line in f:
    word = line.strip()
    if(len(word) == WORD_LENGTH):
        f2.writelines(word.upper() + '\n')
f.close()
f2.close()
