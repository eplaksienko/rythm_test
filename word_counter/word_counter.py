import re

class WordCounter:
    @staticmethod
    def count_words(sentence):
        #check if word is not empty (0 len) and input is not None
        if sentence:
            #use regular expression in order to get words only (commas, periods and etc are not part of the words)
            words = re.findall(r"[\w']+", sentence)
            #prepare structure (dictionary)
            current_return = {
                "words": "",
                "length": 0,
            }
            #iterate through the list of the words
            for word in words:
                #if find longer add to structure
                if current_return.get("length") < len(word):
                    current_return.update({
                        "words": [word],
                        "length": len(word),
                    })
                #if we have the word as long as the current longest just add it to the list of the words
                elif current_return.get("length") == len(word):
                    current_return.get("words").append(word)
            #return structure
            return current_return

