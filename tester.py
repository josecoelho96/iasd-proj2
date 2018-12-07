from main import solve

input_file_path = "inputs/example.txt"
output_file_path = "outputs/example.txt"

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w+")

solve(input_file, output_file)
