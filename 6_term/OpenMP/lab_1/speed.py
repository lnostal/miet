from subprocess import PIPE, run

def run_script(script, n,m):
    command = [script, str(n), str(m)]
    result = run(command,stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if result.returncode == -11:
        return 0
    return get_speed(result.stdout)


def get_speed(rows):
    output_rows = rows.split("\n")
    last_row = output_rows[len(output_rows)-2]
    speed = float(last_row.split(" ")[-1])

    return speed


def computing(script):
    num_of_runs = 5

    matrix_n = 10
    matrix_m = 100

    for i in range(5):
        
        parallel_speed = 0.0

        for _ in range(num_of_runs):
            parallel_speed += run_script(script, matrix_n, matrix_m)
        
        parallel_speed /=num_of_runs
        if i == 0:
            print("Matrix {}x{}, \t\tmean speed: {:.6f}".format(matrix_n, matrix_m, parallel_speed))
        else:
            print("Matrix {}x{}, \tmean speed: {:.6f}".format(matrix_n, matrix_m, parallel_speed))

        matrix_m *=10


parallel_script = "src/parallel"
nonparallel_script = "src/without_parallel"

print("\nParallel script\n\n")
computing(parallel_script)

print("\nNone-Parallel script\n\n")
computing(nonparallel_script)
