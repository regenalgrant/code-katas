
"""Testing  Categorize_New_Member from Codewars."""
from Categorize_New_Member import Categorize_New_Member

def test_Categorize_New_Member():

test.assert_equals(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]),['Open', 'Senior', 'Open', 'Senior'])
test.assert_equals(openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]]),['Open', 'Open', 'Senior', 'Open'])