from school_schedule_csp import solve

# input_file_path = "inputs/example.txt"
# output_file_path = "outputs/example.txt"

# input_file_path = "inputs/public_test_1.txt"
# output_file_path = "outputs/public_test_1.txt"

# input_file_path = "inputs/public_test_2.txt"
# output_file_path = "outputs/public_test_2.txt"

input_file_path = "inputs/public_test_3.txt"
output_file_path = "outputs/public_test_3.txt"

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w+")

solve(input_file, output_file)
