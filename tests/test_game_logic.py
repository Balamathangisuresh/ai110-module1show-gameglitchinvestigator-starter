from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# FIX line 3: Hard difficulty should have a larger range than Normal
def test_difficulty_hard_range_is_larger_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_difficulty_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_difficulty_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_difficulty_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


# FIX line 34: hint messages should match the direction the player needs to go
def test_too_high_message_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# FIX line 44: string secret comparison should be numeric, not lexicographic
def test_string_secret_too_low_numeric():
    # 9 < 10 numerically, but "9" > "10" lexicographically — must use int comparison
    outcome, message = check_guess(9, "10")
    assert outcome == "Too Low"

def test_string_secret_too_high_numeric():
    # 11 > 10 both numerically and lexicographically — sanity check
    outcome, message = check_guess(11, "10")
    assert outcome == "Too High"

def test_string_secret_win():
    outcome, message = check_guess(10, "10")
    assert outcome == "Win"
