import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import random
from environment.setttings import PROCESSED_WORDLIST_PATH, COLORS, WORD_LENGTH
from gameplay.base_singleton import singleton
class game_process(singleton): 
    number_of_word = 0
    word_chosen = ""
    word_count = {}

    def __init__(self):
        return

    def random_word(self):
        f = open(PROCESSED_WORDLIST_PATH,"r")
        self.number_of_word = len(f.readlines())
        word_index = random.randint(0,self.number_of_word - 1)
        tmp = 0
        f.seek(0)
        for line in f:
            word = line.strip()
            if tmp == word_index:
                self.word_chosen = word
                break
            tmp+=1
        f.close()
        for i in self.word_chosen:
            self.word_count.update({i:0})
        for i in self.word_chosen:
            self.word_count[i] += 1
        print(self.word_chosen)

    def in_dictionary(self,user_input):
        if len(user_input) != WORD_LENGTH:
            return False
        f = open(PROCESSED_WORDLIST_PATH,"r")
        for line in f:
            word = line.strip()
            if(word == user_input):
                return True
        return False
    
    def getcolor(self,user_input):
        count_arr = {}
        color_list = []
        for i in user_input:
            count_arr.update({i:0})
        for i in range(0,WORD_LENGTH):
            count_arr[user_input[i]] += 1
            if user_input[i] == self.word_chosen[i]:
                color_list.append("green")
            else: 
                if(user_input[i] not in self.word_count or self.word_count[user_input[i]] < count_arr[user_input[i]]):
                    color_list.append("gray")
                else:
                    color_list.append("yellow")
        return color_list

