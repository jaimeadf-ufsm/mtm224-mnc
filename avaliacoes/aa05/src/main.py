import argparse
import yaml
import numpy as np
import sys

from display import *

from questions.question_01 import question_01
from questions.question_02a import question_02a
from questions.question_02b import question_02b
from questions.question_03 import question_03

sys.setrecursionlimit(1000000)

def run(args):
    with open(args.values, "r") as values_file:
        values = yaml.safe_load(values_file)

        name = values["name"]
        date = values["date"]

        project = Project()
        project.add_element(Header(
            "AA05",
            "MTM224 - Métodos Numéricos Computacionais",
            name,
            date
        ))

        # t = np.matrix(values["questions"][2]["points"])

        # for i in range(0, len(t)):

        #     print(f"{np.exp(t[i, 0]):.4g} {np.exp(t[i, 1]):.4g};")


        # print(t)

        question_01(project, values["questions"]["q01"])
        question_02a(project, values["questions"]["q02a"])
        question_02b(project, values["questions"]["q02b"])
        question_03(project, values["questions"]["q03"])

        project.save(args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("values")
    parser.add_argument("-o", "--output")
    parser.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)