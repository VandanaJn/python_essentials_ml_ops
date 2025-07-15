from password_checker import pwd_checker
import pytest
@pytest.mark.parametrize("pwd, expected",[("abc","too short")
                                          ,("abc12345","weak"),
                                          ("abc12345!","moderate"),
                                          ("aBc12345!","strong"),
                                          ("aBcd12345!","moderate"),
                                          ],
                                          ids=[1,2,3,4,5])
def test_pwd_checker(pwd,expected):
    assert(pwd_checker(pwd)==expected)

@pytest.mark.parametrize("chk_cmn_wrd, expected",[(True,"moderate"),(False,"strong"),])
def test_pwd_checker_flg(chk_cmn_wrd, expected):
    assert(pwd_checker("aBcd12345!",check_common_word=chk_cmn_wrd)==expected)