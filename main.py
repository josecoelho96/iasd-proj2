import csp

class Problem(csp.CSP):

    def __init__(self, fh):
        # Place here your code to load problem from opened file object fh and
        # set variables, domains, graph, and constraint_function accordingly
        super().__init__(variables, domains, graph, constraints_function)
        
    def dump_solution(self, fh):
        # Place here your code to write solution to opened file object fh
        
def solve(input_file, output_file):
    p = Problem(input_file)
    # Place here your code that calls function csp.backtracking_search(self, ...)
    p.dump_solution(output_file)
