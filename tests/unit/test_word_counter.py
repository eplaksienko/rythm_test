from word_counter.word_counter import WordCounter

def test_2_longest_words():
    result = WordCounter.count_words("The cow jumped over the moon, woohoo.")
    assert result == {'length': 6, 'words': ['jumped', 'woohoo']}

def test_1_longest_words():
    result = WordCounter.count_words("The cow jumped over the moon.")
    assert result == {'length': 6, 'words': ['jumped']}

def test_1_word():
    result = WordCounter.count_words("The")
    assert result == {'length': 3, 'words': ['The']}

def test_empty_sentence():
    result = WordCounter.count_words("")
    assert result == None

def test_none_input():
    result = WordCounter.count_words("")
    assert result == None