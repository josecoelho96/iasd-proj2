import csp
import threading
import os


class Problem(csp.CSP):
    
    def __init__(self, fh):
        # Get all lines from file and check each line
        for line in fh.readlines():
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
                associations_list = set(l[1:])


        self.hour_lower_bound = 24
        self.hour_upper_bound = 0
        # Create domain (same for all variables) and get lower/upper hour bound
        domain_list = []
        for slot in time_slots:
            t = slot.split(",")
            day = t[0]
            hour = int(t[1])
            if hour > self.hour_upper_bound:
                self.hour_upper_bound = hour
            if hour < self.hour_lower_bound:
                self.hour_lower_bound = hour
            for r in rooms:
                domain_list.append([[day, hour], r])

        self.domain = sorted(domain_list, key = lambda x: x[0][1])
        domains = {var:self.domain for var in weekly_classes}

        # Speed up by not performing split() on constraints function
        self.formatted_variables = {var:var.split(",") for var in weekly_classes}

        graph = {}
        for var in weekly_classes:
            new_vars = set(weekly_classes)
            new_vars.remove(var)
            graph[var] = new_vars

        associations = dict()
        for association in associations_list:
            l = association.split(",")
            if l[1] in associations:
                associations[l[1]].add(l[0])
            else:
                associations[l[1]] = {l[0]}

        # Define current upper bound
        self.current_upper_bound = self.hour_upper_bound
        self.solution = None

        def constraints_function(A, a, B, b):
            # a - [['Mon', 8], 'EA1']
            # a[0] = ['Mon', 8] --- DAY/HOUR
            # a[0][0] = 'Mon' --- DAY
            # a[0][1] = 8 --- HOUR
            # a[1] = 'EA1' --- ROOM

            # Change to object variable and index it using the variable
            A_course = self.formatted_variables[A][0]
            A_class_kind = self.formatted_variables[A][1]
            B_course = self.formatted_variables[B][0]
            B_class_kind = self.formatted_variables[B][1]

            # "each room can only hold one class at a time"
            if a == b:
                # Same room at the same time
                return False

            # "no two weekly classes of the same course
            # and type may occur on the same weekday"
            if A_course == B_course and A_class_kind == B_class_kind and a[0][0] == b[0][0]:
                return False

            # "each student class can only attend one class at a time"
            if A_course == B_course and a[0] == b[0]:
                return False

            if associations[A_course].intersection(associations[B_course]) and a[0] == b[0]:
                return False

            return True

        super().__init__(weekly_classes, domains, graph, constraints_function)

    def csp_backtracking_search(self):
        new_solution = csp.backtracking_search(self,
            select_unassigned_variable = csp.mrv,
            inference = csp.forward_checking)
        print("[D] [{}] new solution : {}".format(self.current_upper_bound, new_solution))

        if new_solution != None:
            self.solution = new_solution
        return new_solution != None

    def reduce_domains(self):
        if self.current_upper_bound <= self.hour_lower_bound:
            return False

        self.current_upper_bound -= 1
        self.domain = [x for x in self.domain if x[0][1] <= self.current_upper_bound]
        self.domains = {var:self.domain for var in self.variables}
        self.curr_domains = None
        self.nassigns = 0
        return not self.domain == []

    def dump_solution(self, fh):
        if self.solution == None:
            fh.write("None")
            print("[DEBUG] : None")
        else:
            for key, value in self.solution.items():
                print("[DEBUG] : {} {},{} {}".format(key, value[0][0], value[0][1], value[1]))
                fh.write("{} {},{} {}\n".format(key, value[0][0], value[0][1], value[1]))

def solve(input_file, output_file):
    
    # Timeout of program if running for to long
    def timeout():
        print ("Timeout")
        p.dump_solution(output_file)
        os._exit(1)

    p = Problem(input_file)
    
    # Set timer and start it
    t = threading.Timer(150.0, timeout)
    t.start()
    
    while p.csp_backtracking_search():
        if not p.reduce_domains():
            break

    p.dump_solution(output_file)



