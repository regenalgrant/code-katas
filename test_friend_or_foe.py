"""Testing friend_or_foe.py from Codewars."""
from friend_or_foe import friend_or_foe


def test_friend():
    """Test the main function from friend_or_foe.py."""
Test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])