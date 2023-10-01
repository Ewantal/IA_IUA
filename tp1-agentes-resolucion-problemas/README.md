## Trabajo Práctico 1 - Agentes y Resolución de Problemas - Grados de Separación

#### Purpose of the practical:

The purpose of the practical is to implement an agent to solve the problem of grades of separations between each actors. The problem consists in finding the smallest amount of movies that connect two actores. To do this, we posses a database made of movies and actors from which we extracts our datas.

>Here is an example: We want to find the shortest path between Tom Hanks and Jennifer Lawrence. The answer is 2 as Tom Hanks is connected to Kevin Bacon through the movie Apollo 13 and Kevin Bacon is connected to Jennifer Lawrence through the movie X-Men: First Class.


#### Solution:

To do this, I implemented two types of algorithms of reasearch:

For each algorithm, the agent receives as parameter the number of actors and uses the database of movies and actores to get the required informations in order to solve the problem.
For each implementation, the desired node is found, the path up to the root is computed and sent back.

- Breadth First Search (BFS)

>This algorithm starts from an inicial node (the rootà and explore all the neighbours-nodes. It then explores the neighbours nodes of the neighbours nodes in a succesive way until encountering the desired one or until there is nothing left to explore.

- Depth First Search (DFS)

>This algorithm starts from an inicial node (the root) and explore all the neighbours-nodes in a recursive way until it finds the desired node or until there is nothing left to explore. If it doesn't find the desired node, it goes back and explore another way.

#### How to execute:

-You must use at least Python 3.8 to execute the program.

To launch the script, you must use the following command:

```bash
python3 degrees.py large|small
```

Here 'large' and 'small' define the database used.

The program will then ask you which algorithm use and tgen which person you want to choose as the actors. If two actors in time have the same names, it will ask you to decide between them using their IDs.

#### examples

We chose the BFS program.
We then chose as the starting node Tom Holland for the ID 4043618
We chose as the destination Ewan McGregor

Here is the result:

![RESULT.png](assets%2FRESULT.png)

#### Conclusion

We can observe that the BFS algorithm is the one that finds the shortest path as it explores all the posibilities. However, the DFS algorithm is faster. We could improve those algorithm by adding a limit to this BFS to fasten its execution.

#### Aplications in the real life

This problem can be applied in the real life through multiples areas such as finding the shortest path between routers in telecomunications or path finding in video games.

#### Slides

THe slides can be found in the asset folder: [IA - TP1 - TALEC.pdf](assets%2FIA%20-%20TP1%20-%20TALEC.pdf) 
