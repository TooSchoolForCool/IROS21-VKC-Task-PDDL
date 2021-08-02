from problem_generator import ProblemGenerator

TEMPLATE_FILE = "picknplace/samples/problem_template.pddl"

def gen_exp1_problems(cases, n_samples, output_dir):
    pg = ProblemGenerator(TEMPLATE_FILE)

    for c in cases:
        pg.generate(c, n_samples, output_dir)


if __name__ == "__main__":
    # each example has n objects
    cases = [i for i in range(1, 17)]
    # number of samples for each case
    n_samples = 50
    # output dir
    output_dir = "picknplace/problems"

    gen_exp1_problems(cases, n_samples, output_dir)