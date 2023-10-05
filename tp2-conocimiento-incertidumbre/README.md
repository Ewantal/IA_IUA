## Trabajo Práctico 2 - Conocimiento e Incertidumbre

### Problem: MineSweeper

### Principle

The goal of this assignment is to implement an agent that solves the Minesweeper game which consists of finding all the mines on an NxN board. To achieve this, we will use informations from that cells that have already been uncovered through sets and IA.

### How to solve the problem

#### Initialization:
The game board is initialized, and the AI begins with no information about the location of mines or safe cells.

#### First move:
The AI makes its first move by clicking on an arbitrary cell, typically the center cell, as it has the highest probability of being safe.

#### Sentences and Knowledge base:
After the first move, the AI collects information from the revealed cell. If the cell contains a number, it indicates the count of neighboring mines.
The AI creates a "sentence" representing this information, which includes the set of neighboring cells and the count.
These sentences are added to the AI's "knowledge base."

#### Inference and Logic:
The AI uses logical inference rules to deduce new information from the existing sentences and knowledge base. For example:
    If a sentence indicates that all its cells are mines, mark them as mines.
    If a sentence indicates that all its cells are safe, mark them as safe.
The AI iteratively updates its knowledge base and makes inferences based on the new information.

#### Safe move:
The AI identifies cells that are known to be safe based on the logical deductions and marks them as safe moves. It avoids clicking on cells with mines or those that have already been revealed.

#### Random move:
If no safe moves can be determined based on the current knowledge, the AI makes random moves among unexplored cells that are not known to be mines.

#### Iterative Process:
Steps 3 to 6 are repeated iteratively as the AI collects more information, makes inferences, and identifies safe moves.

#### Winning or Loosing:
The AI continues until it either successfully uncovers all safe cells (winning the game) or mistakenly clicks on a mine (losing the game).

### What is needed ?

:warning: To run the agent, you must have at least Pygame 2.0.1 or higher installed.

:warning: To run the agent, you must have at least Python 3.10 or higher installed.

To run the agent, execute the following command:

```bash
python3 runner.py
```

### How does it looks ?

![game.png](assets%2Fimages%2Fgame.png)


### Conclusions

We can see that the AI is solving in the most efficient way the problem and hence works perfectly.
However it is not always posible to win, indeed the AI may loose due to bad random moves.
