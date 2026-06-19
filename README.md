# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose. 

   The game is a number guessing game where the player tries to guess a randomly generated secret number with three game modes easy, normal and hard. After each guess, the game provides a hint indicating whether the secret number is higher or lower than the player's guess.

- [ ] Detail which bugs you found.

   1. Point calculation sometimes increased when a wrong guess was entered.

   2. The history doesn't update current guess but previous guess or doesn't update when the guess is the first guess because there is no previous guess.

   3. Normal has a larger range than Hard difficulty.

   4. Hints are reversed (when i guess a number higher than the secret number the hint says to go higher not lower and when i guess a number lower than the secret number the hint says to go lower not higher).

   5. New game button does not work (the game thinks you are in the same state as the previous round (won/lost) so doesn't let you enter a guess and doesn't clear the history of the previous round but gives you a new number as the secret number).

- [ ] Explain what fixes you applied.

   1. Original update_score added points for an even attempt of a guess that is too high which is not consistent with the points calculation so this was changed so both wrong guess outcomes consistently subtract 5 points from the score.

   2. History was originally rendered before the guess was submitted by the user so it always showed the history before the current guess. This was fixed by moving the code for the Developer Debug Info to the bottom of the python script after the code for the submit button so the history shows the current guess.

   3. Original get_range_for_difficulty had mismatched ranges so that Hard had a smaller range and therefore was easier than Normal. This was fixed so that the ranges scale correctly to each difficulty: Easy's range 1–20, Normal's range 1–50, Hard's range = 1–100.

   4. Original check_guess returned "Go HIGHER!" when the guess was too high, and "Go LOWER!" when the guess was too low. Fixed by swapping the inequalities so guess > secret → "Too High", "📉 Go LOWER!" else the guess was too low "Too Low", "📈 Go HIGHER!" (The equal case was already checked).

   5. Originally, the new game button only generated a new secret number but left attempts, score, history, and status unchanged. So the game was still in a "won" or "lost" state did not let users enter any guesses. This was fixed by resetting all five session state values not just for secret number and calling st.rerun() to force a clean slate.
   

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Launch the Streamlit Application
2. User enters a guess of 50
3. Game returns a hint of "Too High"
4. User enters a guess of 10
4. Game returns a hint of "Too Low"
5. Score updates correctly after each guess
6. History is updated correctly after each guess
7. User clicks New Game
8. A new secret number is generated with the number of attempts reset and the previous game's history cleared
9. User is able to enter guesses and enters a guess of 25
10. Game returns a hint of "Too High"
11. Game ends with "You won!" after the correct guess or with "Out of attempts!" after user runs out of attempts

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results 

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

   collected 12 items                                                                                     

   test_game_logic.py::test_winning_guess PASSED                                                    [  8%]
   test_game_logic.py::test_guess_too_high PASSED                                                   [ 16%]
   test_game_logic.py::test_guess_too_low PASSED                                                    [ 25%]
   test_game_logic.py::test_difficulty_hard_range_is_larger_than_normal PASSED                      [ 33%]
   test_game_logic.py::test_difficulty_easy_range PASSED                                            [ 41%]
   test_game_logic.py::test_difficulty_normal_range PASSED                                          [ 50%]
   test_game_logic.py::test_difficulty_hard_range PASSED                                            [ 58%]
   test_game_logic.py::test_too_high_message_says_go_lower PASSED                                   [ 66%]
   test_game_logic.py::test_too_low_message_says_go_higher PASSED                                   [ 75%]
   test_game_logic.py::test_string_secret_too_low_numeric PASSED                                    [ 83%]
   test_game_logic.py::test_string_secret_too_high_numeric PASSED                                   [ 91%]
   test_game_logic.py::test_string_secret_win PASSED                                                [100%]

   ========================================= 12 passed in 0.09s ==========================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
