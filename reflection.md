# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The history of guesses did not properly update (the first number inputted is not included then for every new number you input the previous guess was registered).

  New game button does not work (the game thinks you are in the same state as the previous round (won/lost) so doesn't let you enter a guess and doesn't clear the history of the previous round but gives you a new number as the secret number).

  Hints are backwards (when i guess a number higher than the secret number the hint says to go higher and vice verca).

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output/ Error |
|Guess of 100|Hint: go lower|hint: go higher|None|
|Clicked button: new game |Reset the secret number, the number of guesses to 8, clear history, and allow guesses to be inputted |Doesn't clear history and doesn't let guesses to be inputted|None |
|First guess of 6 |History array: [6] | History of array: [] |None |
|Choosing difficulty: normal |Range: 0-50 |Range: 0-100 |None |
|Guesses: 2, 4| Points: -10| Points: 0| None|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  - I used Claude.

  - Claude suggested that the even attempts of too high guesses rewards points which doesn't make sense logically for this guessing game. And I tested this on the app noticing how the points are calculated and it was incorrect. I asked Claude to make these changes and tested the game again to check if the points were calculated correctly. After Claude made those changes the points system logically makes more sense.

  - Claude suggested that there is no else block to catch the too low guess in the check_guess function but there clearly was one so I didn't accept its suggestion. It's suggestion attempted to change the entire structure of the function which was very redundant and not the cause of the hints being incorrect.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  - I decided when the bug was really fixed after running through tests of my own by running the app and trying to reproduce the same bug and see if the bug shows up including testing edge cases. For some fixes I also asked claude to make pytests and verified each pytest and ran them and also tested them myself by running the app. 

  - One test I ran manually was to check whether the hints were correct or not. For that, after Claude made its changes, I ran the app and checked the secret number. I made guesses above and below the secret number to make sure the hints were correct. I also made sure to check edge cases like 1 and 50 for normal and 1 to 20 for easy and 1 to 100 for hard, numbers one under or over the secret number and the actual secret number to check if the winning condition was still working.

  - After I manually tested the hints, I also asked AI to help me design tests for the hints bug. I explained the fix again in a new session and asked it to write tests in a test_game_logic.py file which i reviewed and ran and verified they all passed.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  - Streamlit reruns starts the entire program from scratch whenever anything changes most memory from a previous run is cleared. The only exception is a session state which is never cleared and keeps data of anything you want between each session. Session states are useful for remembering things like user choices, progress or previous results.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  - One habit I would like to take away from this project is commiting more often in Github and testing before commits. Although I commited for every few fixes sometimes and not just one fix I want to work on updating Github more often and testing more often even if it feels redundant so I can keep my progress trackable.

  - I would like to be more organized with the AI tool I'm using for future projects by starting off broadly and understanding the code first before diving down on small details in the beginning. This is to have a deeper understanding of the code to catch more obvious bugs before I ask AI to debug harder ones because I ended up overlooking some bugs I could have fixed easily because I was too focused on the AI fixing a particular bug. 

  - I previously thought AI generating code and debugging is more advanced but now I believe AI generated code is very unreliable as of right now when making applications or debugging them so human input is needed. However, with a person veryifying the AI's changes and testing it frequently AI is a great tool for debugging.
