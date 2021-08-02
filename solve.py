import requests
import sys


def solve(domain_file, problem_file):
    data = {
        'domain': open(domain_file, 'r').read(),
        'problem': open(problem_file, 'r').read()
    }

    resp = requests.post(
        'http://solver.planning.domains/solve',
        verify=False, json=data
    ).json()

    result = '\n'.join([act['name'] for act in resp['result']['plan']])
    
    print(result)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("\tpython planner.py <domain-file> <problem-file>")
        exit(0)
    
    solve(sys.argv[1], sys.argv[2])