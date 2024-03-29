import csp

class Problem(csp.CSP):

    def constraints_function(self, A, a, B, b):
        if A == "X" and B == "Y":
            return a < b
        elif A == "X" and B == "T":
            return a < b
        elif A == "Y" and B == "X":
            return a > b
        elif A == "Y" and B == "Z":
            return a == b
        elif A == "Z" and B == "Y":
            return a == b
        elif A == "Z" and B == "T":
            return a > b
        elif A == "T" and B == "Z":
            return a < b
        elif A == "T" and B == "X":
            return a > b

    def __init__(self):
        variables = {"X", "Y", "Z", "T"}
        domains = {
            "X": [1, 2, 3],
            "Y": [1, 2, 3],
            "Z": [1, 2, 3],
            "T": [1, 2, 3]
        }
        graph = {
            "X": ["Y", "T"],
            "Y": ["X", "Z"],
            "Z": ["Y", "T"],
            "T": ["X", "Z"]
        }

        super().__init__(variables, domains, graph, self.constraints_function)

def solve():
    p = Problem()
    print(csp.backtracking_search(p))

if __name__ == "__main__":
    solve()