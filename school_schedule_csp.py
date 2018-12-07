import csp

class Problem(csp.CSP):

    def __init__(self, fh):
        # Place here your code to load problem from opened file object fh and
        # set variables, domains, graph, and constraint_function accordingly

        # Get all lines from file
        lines = fh.readlines()

        # Check each line
        for line in lines:
            # Remove '\n' and split on spaces
            l = line.strip().split(" ")
            if l[0] == "T":
                time_slots = set(l[1:])
                print("[DEBUG] Time slots set: '{}'.".format(time_slots))
            elif l[0] == "R":
                rooms = set(l[1:])
                print("[DEBUG] Rooms set: '{}'.".format(rooms))
            elif l[0] == "S":
                student_classes = set(l[1:])
                print("[DEBUG] Student classes set: '{}'.".format(student_classes))
            elif l[0] == "W":
                weekly_classes = set(l[1:])
                print("[DEBUG] Weekly classes set (variables): '{}'.".format(weekly_classes))
            elif l[0] == "A":
                associations = set(l[1:])
                print("[DEBUG] Assocations set: '{}'.".format(associations))

        # Create domain (same for all variables)
        domain = set()
        for t in time_slots:
            for r in rooms:
                domain.add("{} {}".format(t, r))

        domains = {}
        for var in weekly_classes:
            domains[var] = domain
        print("[DEBUG] Domains: {}".format(domains))

        graph = {}
        for var in weekly_classes:
            print("[DEBUG] var: {}".format(var))
            new_vars = set(weekly_classes)
            new_vars.remove(var)
            print("[DEBUG] new_vars: {}".format(new_vars))
            graph[var] = new_vars
        print("[DEBUG] Graph: {}".format(graph))


        def constraints_function(A, a, B, b):
            return True

        super().__init__(weekly_classes, domains, graph, constraints_function)

    def dump_solution(self, fh):
        # Place here your code to write solution to opened file object fh
        pass

def solve(input_file, output_file):
    p = Problem(input_file)
    print(csp.backtracking_search(p))
    # Place here your code that calls function csp.backtracking_search(self, ...)
    p.dump_solution(output_file)
