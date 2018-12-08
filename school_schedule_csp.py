import csp

class Problem(csp.CSP):

    def __init__(self, fh):
        # Get all lines from file
        lines = fh.readlines()

        # Check each line
        for line in lines:
            # Remove '\n' and split on spaces
            l = line.strip().split(" ")
            if l[0] == "T":
                time_slots = set(l[1:])
            elif l[0] == "R":
                rooms = set(l[1:])
            elif l[0] == "S":
                student_classes = set(l[1:])
            elif l[0] == "W":
                weekly_classes = set(l[1:])
            elif l[0] == "A":
                associations = set(l[1:])

        # Create domain (same for all variables)
        domain = set()
        for t in time_slots:
            for r in rooms:
                domain.add("{} {}".format(t, r))

        domains = {}
        for var in weekly_classes:
            domains[var] = domain

        graph = {}
        for var in weekly_classes:
            new_vars = set(weekly_classes)
            new_vars.remove(var)
            graph[var] = new_vars

        def constraints_function(A, a, B, b):
            return True

        super().__init__(weekly_classes, domains, graph, constraints_function)

    def csp_backtracking_search(self):
        self.solution = csp.backtracking_search(self)

    def dump_solution(self, fh):
        # Place here your code to write solution to opened file object fh
        if self.solution == None:
            fh.write("None")
        else:
            for key, value in self.solution.items():
                fh.write("{} {}\n".format(key, value))

def solve(input_file, output_file):
    p = Problem(input_file)
    Problem.csp_backtracking_search(p)
    p.dump_solution(output_file)
