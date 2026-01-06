1. **AI Game Referee – Rock Paper Scissors Plus**



This project is a **minimal AI Game Referee chatbot** built for the  

**upliance.ai – AI Product Engineer (Conversational Agents)** assignment.



The referee runs a short game of **Rock–Paper–Scissors–Plus**, enforces rules,

tracks state, and announces results clearly.







**2. Game Rules**



\- Best of **3 rounds**

\- Valid moves:

&nbsp; - rock

&nbsp; - paper

&nbsp; - scissors

&nbsp; - bomb (can be used **once per game**)

\- Bomb beats all other moves

\- Bomb vs Bomb → draw

\- Invalid input **wastes the round**

\- Game ends automatically after 3 rounds







**3. Design (Google ADK Style)**



The solution follows **Google ADK (Agent Development Kit) principles**:



\- Persistent state stored outside the prompt

\- Explicit tools for validation and state updates

\- Clear separation of logic and response generation



**4. Agent Flow**



User Input

↓

Validation Tool

↓

Game Logic Tool

↓

State Update Tool

↓

Response to User





 **5. State Model**



The game state is stored using a Python data class and includes:



\- Current round number

\- User score

\- Bot score

\- Whether user bomb is used

\- Whether bot bomb is used



This ensures state persists correctly across turns.



 **Tools Used**



&nbsp;     Tool Name          |         Purpose 



&nbsp;validate move           |   Checks valid input and bomb usage 

&nbsp;resolve round           |   Decides winner based on rules 

&nbsp;update game state       |   Updates scores, rounds, and bomb usage 



All state changes happen only through tools.







&nbsp;**6**. **How to Run**



* &nbsp;**Option 1: Local Machine**



python rps-plus-adk-agent.py



* **Option 2: Google Colab**



Paste the code into a Colab notebook



Run the cell



Enter moves when prompted



Requirements



Python 3.8+



No external libraries required



**7.** **Sample Output**

--- Round 1 ---

You played: rock

Bot played: scissors

Result: User wins the round



--- Round 2 ---

You played: bomb

Bot played: paper

Result: User wins the round



--- Round 3 ---

Invalid input. Round wasted.



=== Final Result ===

You win the game!


**8. Tradeoffs**



* Bot move selection is random for simplicity



* Single-agent design to keep the solution minimal



* CLI-based interaction as required

  **9. Future Improvements**



* Smarter bot strategy



* Multi-agent separation (NLU vs game logic)



* Structured JSON outputs



* Unit tests

  **10.** **Author**



Built as part of the **upliance.ai AI Product Engineer (Conversational Agents)** assignment.




