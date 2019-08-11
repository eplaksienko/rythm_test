from word_counter.word_counter import WordCounter

#test situation when more then 1 longest word
def test_2_longest_words():
    result = WordCounter.count_words("The cow jumped over the moon, woohoo.")
    assert result == {'length': 6, 'words': ['jumped', 'woohoo']}

#test situation when 1 longest word
def test_1_longest_words():
    result = WordCounter.count_words("The cow jumped over the moon.")
    assert result == {'length': 6, 'words': ['jumped']}

#test situation when more only 1 word
def test_1_word():
    result = WordCounter.count_words("The")
    assert result == {'length': 3, 'words': ['The']}

#test situation with empty string
def test_empty_sentence():
    result = WordCounter.count_words("")
    assert result == None

#test situation with None input
def test_none_input():
    result = WordCounter.count_words(None)
    assert result == None