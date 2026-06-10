# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The history of guesses did not properly update (the first number inputted is not included then for every new number you input the previous guess was registered)

  New game button does not work (the game thinks you are in the same state as the previous round (won/lost) so doesn't let you enter a guess and doesn't clear the history of the previous round but gives you a new number as the secret number).

  Hints are backwards (when i guess a number higher than the secret number the hint says to go higher and vice verca).

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|guess of 100|Hint: go lower|hint: go higher|none|
|clicked button: new game |reset the secret number, the number of guessesto 8, clear history, and allow guesses to be inputted |doesn't clear history and doesn't let guesses to be inputted|none |
|first guess of 6 |history array: [6] |history of array: [] |none |
|choosing difficulty: normal |range: 0-50 |range: 0-100 |none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- Claude
- Claude suggested that the even attempts of too high guesses rewards points which doesn't make sense logically for this guessing game. And I tested this on the app noticing how the points are calculated and it was incorrect. I asked Claude to make these changes and tested the game again.
- Claude suggested that there is no else block to catch the too low guess for the check_guess function but there clearly was one so I didn't accept its suggestion.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
