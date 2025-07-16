from remove_profanity import clean_comments
# import pdb
class TestRemoveProfanity:
    def setup_method(self):
        print("This is setup")

    def teardown_method(self):
        print("This is teardown")

    def setup_class(cls):
        print("This is setup_class")
    
    def teardown_class(cls):
        print("This is teardown_class")

    def test_clean_comments_unclean(self):
        # pdb.set_trace()
        assert clean_comments(["comment1","This is comment3"],["comment3","bad"])\
        ==["comment1","This is ********"]

    def test_clean_comments2_clean(self):
        assert clean_comments(["This is comment1","This is comment3"],["comment2","bad"])==\
            ["This is comment1","This is comment3"]
        