from subprocess import PIPE, run

def run_script(script, nmax,limit):
    command = [script, str(nmax), str(limit)]
    result = run(command,stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if result.returncode == -11:
        return 0
    return result.stdout.replace("\n","")

nmax = 10
limit = 9

script = "./lab2"

for _ in range(4):
    print("\nmatrix {}x{}".format(nmax,nmax))
    for _ in range(5):
        duration = run_script(script, nmax,limit)
        print("limit: {} \t{}".format(limit, duration))
        limit*=10
    nmax*=10
    limit = 4