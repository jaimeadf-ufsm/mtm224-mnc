import argparse
import yaml

from display import *

from methods.divided_differences import divided_differences

def run(args):
    with open(args.values, "r") as values_file:
        values = yaml.safe_load(values_file)

        name = values["name"]
        date = values["date"]

        z = float(values["methods"]["divided_differences"]["z"])
        points = np.matrix(values["methods"]["divided_differences"]["points"])

        project = Project()
        project.add_element(Header(
            "AA03",
            "MTM224 - Métodos Numéricos Computacionais",
            name,
            date
        ))
            
        divided_differences(project, points, z)

        project.save(args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("values")
    parser.add_argument("-o", "--output")
    parser.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)
