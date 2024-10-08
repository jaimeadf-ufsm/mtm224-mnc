import math

def header(title, subtitle):
    return f"\\textbf{{{title}}}: {subtitle} \\\\"

def scientific(n):
    if n == math.inf:
        return "\\infty"

    notation = f"{n:.10g}"
    pieces = notation.split("e")

    if len(pieces) >= 2:
        return f"{pieces[0]} \\times 10^{{{int(pieces[1])}}}"
    
    return notation

class Table:
    def __init__(self, title = None):
        self.title = title
        self.columns = []
        self.rows = []
    
    def add_column(self, column):
        self.columns.append(column)
    
    def add_row(self, row):
        self.rows.append(row)

    def __str__(self):
        # table = "$$\n"
        # table += f"\\left("
        # table += f"\\begin{{array}}{{{" ".join("c" * len(self.columns))}}}\n"

        # table += f"{" & ".join(self.columns)} \\\\\n"

        # for row in self.rows:
        #     table += f"{" & ".join(row)} \\\\\n"

        # table += "\\end{array}"
        # table += f"\\right)"
        # table += "$$\n"

        # return table


        table = "\\begin{table}[htpb]\n"
        table += "\\centering\n"
        
        if self.title:
            table += f"\\caption*{{{self.title}}}\n"

        table += f"\\begin{{tabular}}{{{' '.join('c' * len(self.columns))}}}\n"

        table += "\\toprule\n"
        table += f"{' & '.join(map(lambda e : f'${e}$', self.columns))} \\\\\n"
        table += "\\midrule\n"

        for row in self.rows:
            table += f"{' & '.join(map(lambda e : f'${e}$', row))} \\\\\n"

        table += "\\bottomrule\n"

        table += "\\end{tabular}\n"
        table += "\\end{table} \\\\\n"

        return table

