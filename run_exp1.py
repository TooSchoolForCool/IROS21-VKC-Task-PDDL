import requests
import sys
import os
import glob


def get_problem_files(root_dir):
    if os.path.isdir(root_dir) == False:
        print("[ERROR] Directory '{}' does NOT exist".format(root_dir))
        exit(1)

    # match number only
    files = glob.glob(root_dir + "/*.pddl")

    return files


def solve(domain_file, problem_file, output_file):
    data = {
        'domain': open(domain_file, 'r').read(),
        'problem': open(problem_file, 'r').read()
    }

    resp = requests.post(
        'http://solver.planning.domains/solve',
        verify=False, json=data
    ).json()
    
    if resp["status"] != "ok":
        print("Failed to solve problem: {} under domain {}".format(problem_file, domain_file))
        return
    
    with open(output_file, 'w') as fout:
        fout.write("{}\n".format(resp["result"]["length"]))
        fout.write("{}\n".format(resp["result"]["output"]))
    
    print("Result was saved at: `{}`".format(output_file))


def run_exp(domain_file, problem_dir, output_dir):
    os.system("mkdir -p {}".format(output_dir))

    problem_files = get_problem_files(problem_dir)

    for pf in problem_files:
        filename = pf.split('/')[-1].split('.')[0]
        output_file = "{}/{}.txt".format(output_dir, filename)

        print("Solving problem `{}` under domain `{}`".format(filename, domain_file))
        solve(domain_file, pf, output_file)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage:")
        print("\tpython run_exp1.py <domain-file> <problem-file-dir> <output-dir>")
        exit(0)
    
    run_exp(sys.argv[1], sys.argv[2], output_dir=sys.argv[3])
