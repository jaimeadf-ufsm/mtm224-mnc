import numpy as np

def format_number(n):
    if n == np.inf:
        return "\\infty"

    notation = f"{n:.10g}"
    pieces = notation.split("e")

    if len(pieces) >= 2:
        return f"{pieces[0]} \\times 10^{{{int(pieces[1])}}}"
    
    return notation

class Project:
    def __init__(self):
        self.elements = []
        self.files = []
    
    def add_element(self, element):
        self.elements.append(element)
    
    def add_file(self, name, content):
        self.files.append((name, content))
    
    def save(self, directory):
        document = "\\documentclass{article}\n"
        document += "\\usepackage[utf8]{inputenc}\n"
        document += "\\usepackage[paperheight=18in,paperwidth=13in,margin=1in]{geometry}\n"
        document += "\\usepackage[all]{xy}\n"
        document += "\\usepackage{amsmath,amsthm,amssymb,color,latexsym}\n"
        document += "\\usepackage{geometry}\n"
        document += "\\usepackage{graphicx}\n"
        document += "\\usepackage{booktabs}\n"
        document += "\\usepackage{caption}\n"
        document += "\\usepackage{subcaption}\n"
        document += "\\usepackage{float}\n"
        document += "\\begin{document}\n"
        document += "\n".join(map(str, self.elements))
        document += "\n\\end{document}\n"

        for name, content in self.files:
            with open(f"{directory}/{name}", "wb") as f:
                f.write(content)

        
        with open(f"{directory}/main.tex", "w") as f:
            f.write(document)

class Header:
    def __init__(self, title, subtitle, author, date):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date = date
    
    def __str__(self):
        output = f"\\noindent {self.title} \\hfill {self.subtitle} \\\\\n"
        output += self.author + f" ({self.date})\n\n"
        output += "\\noindent \\hrulefill\n"

        return output

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
        output = "\\begin{table}[htpb]\n"
        output += "\\centering\n"
        
        if self.title:
            output += f"\\caption*{{{self.title}}}\n"

        output += f"\\begin{{tabular}}{{{' '.join('c' * len(self.columns))}}}\n"

        output += "\\toprule\n"
        output += f"{' & '.join(map(lambda e : f'${e}$', self.columns))} \\\\\n"
        output += "\\midrule\n"

        for row in self.rows:
            output += f"{' & '.join(map(lambda e : f'${e}$', row))} \\\\\n"

        output += "\\bottomrule\n"

        output += "\\end{tabular}\n"
        output += "\\end{table} \\\\\n"

        return output