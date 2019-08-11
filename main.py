from word_counter.word_counter import WordCounter

def main():
    print(WordCounter.count_words("The cow jumped over the moon, woohoo."))
    print(WordCounter.count_words(""))
    print(WordCounter.count_words(None))
    print(WordCounter.count_words("The"))
    print(WordCounter.count_words("The cow jumped over the moon."))

if __name__== "__main__":
    main()