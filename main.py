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
            print("[DEBUG] Line containing set: {}.".format(l[0]))
            if l[0] == "T":
                print("[DEBUG] Line containing timetable slots set.")
            elif l[0] == "R":
                print("[DEBUG] Line containing rooms set.")
            elif l[0] == "S":
                print("[DEBUG] Line containing student classes set.")
            elif l[0] == "W":
                print("[DEBUG] Line containing weekly classes set.")
                for weekly_class in l[1:]:
                    print(weekly_class)
            elif l[0] == "A":
                print("[DEBUG] Line containing associations set.")

        # super().__init__(variables, domains, graph, constraints_function)

    def dump_solution(self, fh):
        # Place here your code to write solution to opened file object fh
        pass

def solve(input_file, output_file):
    p = Problem(input_file)
    # Place here your code that calls function csp.backtracking_search(self, ...)
    p.dump_solution(output_file)
