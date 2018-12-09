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
                associations_list = set(l[1:])

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

        associations = dict()
        for association in associations_list:
            l = association.split(",")
            if l[1] in associations:
                associations[l[1]].add(l[0])
            else:
                associations[l[1]] = {l[0]}

        def constraints_function(A, a, B, b):

            # Split variables into more easier to recall names
            a_time = a.split(" ")[0]
            a_day = a_time.split(",")[0]
            a_hour = a_time.split(",")[1]
            a_room = a.split(" ")[1]
            b_time = b.split(" ")[0]
            b_day = b_time.split(",")[0]
            b_hour = b_time.split(",")[1]
            b_room = b.split(" ")[1]
            A_course = A.split(",")[0]
            A_class_kind = A.split(",")[1]
            B_course = B.split(",")[0]
            B_class_kind = B.split(",")[1]

            # "each room can only hold one class at a time"
            if a_time == b_time and a_room == b_room:
                return False

            # "no two weekly classes of the same course
            # and type may occur on the same weekday"
            if A_course == B_course and A_class_kind == B_class_kind and a_day == b_day:
                return False

            # "each student class can only attend one class at a time"
            if A_course == B_course and a_time == b_time:
                return False

            if associations[A_course].intersection(associations[B_course]) and a_time == b_time:
                return False

            return True

        super().__init__(weekly_classes, domains, graph, constraints_function)

    def csp_backtracking_search(self):
        self.solution = csp.backtracking_search(self)

    def dump_solution(self, fh):
        if self.solution == None:
            fh.write("None")
        else:
            for key, value in self.solution.items():
                # print("[DEBUG] : {} {}".format(key, value))
                fh.write("{} {}\n".format(key, value))

def solve(input_file, output_file):
    p = Problem(input_file)
    Problem.csp_backtracking_search(p)
    p.dump_solution(output_file)
