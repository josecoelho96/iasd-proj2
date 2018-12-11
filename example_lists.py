import csp

class Problem(csp.CSP):

    def constraints_function(self, A, a, B, b):
        return a != b

    def __init__(self):
        variables = {"X", "Y", "Z", "T"}
        domains = {
            "X": [["Mon", 8], ["Mon", 9], ["Tue", 8], ["Tue", 9]],
            "Y": [["Mon", 8], ["Mon", 9], ["Tue", 8], ["Tue", 9]],
            "Z": [["Mon", 8], ["Mon", 9], ["Tue", 8], ["Tue", 9]],
            "T": [["Mon", 8], ["Mon", 9], ["Tue", 8], ["Tue", 9]]
        }
        graph = {
            "X": ["Y", "T", "Z"],
            "Y": ["X", "Z", "T"],
            "Z": ["Y", "T", "X"],
            "T": ["X", "Z", "Y"]
        }

        super().__init__(variables, domains, graph, self.constraints_function)

def solve():
    p = Problem()
    print(csp.backtracking_search(p))

if __name__ == "__main__":
    solve()