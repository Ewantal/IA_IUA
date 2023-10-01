import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    algo = ""
    while algo != "BFS" and algo != "DFS":
        algo = input("BFS or DFS: ")
    source = person_id_for_name(input("Nombre del actor 1: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Nombre del actor 2: "))
    if target is None:
        sys.exit("Person not found.")

    if algo == "BFS":
        path = shortest_path_BFS(source, target)
    else:
        path = shortest_path_DFS(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path_BFS(source, target):
    # Inicializa una frontera (frontier) utilizando una cola (QueueFrontier)
    frontier = QueueFrontier()

    # Inicializa un conjunto (set) para realizar un seguimiento de los nodos visitados
    visited = set()

    # Agrega el nodo de inicio (source) a la frontera
    frontier.add(Node(source, None, None))

    while not frontier.empty():
        # Obtén el nodo actual de la frontera
        node = frontier.remove()

        # Si el nodo actual es el objetivo (target), reconstruye el camino y devuélvelo
        if node.state == target:
            path = []
            while node.parent is not None:
                path.append((node.action, node.state))
                node = node.parent
            path.reverse()
            return path

        # Marca el nodo actual como visitado
        visited.add(node.state)

        # Genera nodos sucesores y agrégalos a la frontera si no han sido visitados
        for action, state in neighbors_for_person(node.state):
            if state not in visited and not frontier.contains_state(state):
                child = Node(state, node, action)
                frontier.add(child)

    # Si no se encuentra un camino, devuelve None
    return None
    raise NotImplementedError

def shortest_path_DFS(source, target):
    # Initialize a frontier using a stack (StackFrontier)
    frontier = StackFrontier()

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Add the starting node (source) to the frontier
    frontier.add(Node(source, None, None))

    while not frontier.empty():
        # Get the current node from the frontier (pop from the stack)
        node = frontier.remove()

        # If the current node is the target, reconstruct and return the path
        if node.state == target:
            path = []
            while node.parent is not None:
                path.append((node.action, node.state))
                node = node.parent
            path.reverse()
            return path

        # Mark the current node as visited
        visited.add(node.state)

        # Generate successor nodes and add them to the frontier if not visited
        for action, state in neighbors_for_person(node.state):
            if state not in visited and not frontier.contains_state(state):
                child = Node(state, node, action)
                frontier.add(child)

    # If no path is found, return None
    return None


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
