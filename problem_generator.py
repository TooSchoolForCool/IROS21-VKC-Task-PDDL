import random
import os


LOC_BASE_TYPE = "loc_base"
LOC_OBJ_TYPE = "loc_object"
OBJ_TYPE = "block"

OBJ_LOC_NAME = "table"
BASE_LOC_NAME = "table_anchor"
OBJ_NAME = "ball"


class ProblemGenerator(object):

    def __init__(self, template_file):
        self.template_file_ = template_file


    def generate(self, n_object, n_samples=None, output_dir=None):
        if n_samples is None:
            n_samples = 1000
        
        if output_dir is None:
            output_dir = "problems"

        os.system("mkdir -p {}".format(output_dir))
        
        for i in range(n_samples):
            filename = "{}/o{}_p{}.pddl".format(output_dir, n_object, i)
            template = self.load_problem_template_()

            objects_def, objects, object_locs, base_locs = self.gen_object_def_(n_object, n_object + 1)
            init_config = self.gen_init_config_(objects, object_locs, base_locs)
            goal_config = self.gen_goal_config_(objects, object_locs)

            problem_def = template.format(objects_def, init_config, goal_config)

            self.dump_(problem_def, filename)

    
    def gen_object_def_(self, n_objects, n_locations):
        objects_def = ""
        objects = []
        object_locs = []
        base_locs = []


        # object locations
        for i in range(n_locations):
            name = "{}_{}".format(OBJ_LOC_NAME, i)
            object_locs.append(name)
            objects_def += name + " "
        objects_def += "- {}\n".format(LOC_OBJ_TYPE)

        # robot locations
        for i in range(n_locations):
            name = "{}_{}".format(BASE_LOC_NAME, i)
            base_locs.append(name)
            objects_def += name + " "
        objects_def += "- {}\n".format(LOC_BASE_TYPE)

        # objects
        for i in range(n_objects):
            name = "{}_{}".format(OBJ_NAME, i)
            objects.append(name)
            objects_def += name + " "
        objects_def += "- {}".format(OBJ_TYPE)

        return objects_def, objects, object_locs, base_locs

    
    def gen_init_config_(self, objects, object_locs, base_locs):
        config = ""

        objects_shuffled = self.shuffle_(objects)
        obj_locs_shuffled = self.shuffle_(object_locs)

        # set robot init location
        config += "(at_base {})\n".format(random.choice(base_locs))
        
        # set object initial locations
        for i in range(len(objects)):
            config += "(at_object {} {})\n".format(objects_shuffled[i], obj_locs_shuffled[i])
            config += "(occupied {})\n".format(obj_locs_shuffled[i])
        
        # set object location and anchor location pair
        for i in range(len(object_locs)):
            config += "(reachable {} {})\n".format(object_locs[i], base_locs[i])

        return config

    
    def gen_goal_config_(self, objects, object_locs):
        config = ""

        objects_shuffled = self.shuffle_(objects)
        obj_locs_shuffled = self.shuffle_(object_locs)

        for i in range(len(objects)):
            config += "(at_object {} {})\n".format(objects_shuffled[i], obj_locs_shuffled[i])
        
        return config


    def load_problem_template_(self):
        template = ""

        with open(self.template_file_, "r") as fin:
            for line in fin:
                template += line
        
        return template

    
    def dump_(self, prob_def, filename):
        with open(filename, "w") as fout:
            fout.write(prob_def)
        
        print("Problem defintion was saved at: `{}`".format(filename))

    
    def shuffle_(self, target):
        t_shuffled = target[:]
        random.shuffle(t_shuffled)

        return t_shuffled


if __name__ == "__main__":
    pg = ProblemGenerator("problem_template.pddl")

    pg.generate(10, 1)