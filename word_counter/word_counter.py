import re

class WordCounter:
    @staticmethod
    def count_words(sentence):
        if sentence:
            words = re.findall(r"[\w']+", sentence)
            current_return = {
                "words": "",
                "length": 0,
            }
            for word in words:
                if current_return.get("length") < len(word):
                    current_return.update({
                        "words": [word],
                        "length": len(word),
                    })
                elif current_return.get("length") == len(word):
                    current_return.get("words").append(word)

            return current_return

