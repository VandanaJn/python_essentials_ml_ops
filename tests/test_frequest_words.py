from frequentword import get_words_count, get_top_words, get_top_words_v2
def test_get_words_count():
    assert get_words_count("freq_words.txt")=={ 'admire': 1, 'am': 1, 
                                           'are': 1, 'doing': 3, 'great': 2, 'hello': 1,
                                           'how': 1,   'i': 2, 'keep': 1, 'much': 1, 'so': 1,
                                           'you': 2} 
    
def test_get_top_words():
    w_count={ 'admire': 1, 'am': 1, 
                                           'are': 1, 'doing': 3, 'great': 2, 'hello': 1,
                                           'how': 1,   'i': 2, 'keep': 1, 'much': 1, 'so': 1,
                                           'you': 2} 
    top_words = get_top_words(w_count, 3)
    assert top_words==['doing','great','i']

def test_get_top_words_v2():
    w_count={ 'admire': 1, 'am': 1, 
                                           'are': 1, 'doing': 3, 'great': 2, 'hello': 1,
                                           'how': 1,   'i': 2, 'keep': 1, 'much': 1, 'so': 1,
                                           'you': 2} 
    top_words = get_top_words_v2(w_count, 3)
    assert top_words==[   ('doing', 3),('great', 2),  ('i', 2)]
    
