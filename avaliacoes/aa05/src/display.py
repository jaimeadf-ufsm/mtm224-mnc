import numpy as np

def format_number(n):
    if n == np.inf:
        return "\\infty"

    notation = f"{n:.6g}"
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
        document += "\\usepackage[paperheight=15in,paperwidth=9in,margin=1in]{geometry}\n"
        document += "\\usepackage[all]{xy}\n"
        document += "\\usepackage{amsmath,amsthm,amssymb,color,latexsym}\n"
        document += "\\usepackage{geometry}\n"
        document += "\\usepackage{graphicx}\n"
        document += "\\usepackage{booktabs}\n"
        document += "\\usepackage{caption}\n"
        document += "\\usepackage{subcaption}\n"
        document += "\\usepackage{float}\n"
        document += "\\usepackage[fleqn]{amsmath}\n"
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
        output += "\\\\ \n"

        return output

class Table:
    def __init__(self, title = None):
        self.title = title
        self.columns = 0
        self.rows = []
    
    def add_top_rule(self):
        self.rows.append("\\toprule")
    
    def add_mid_rule(self):
        self.rows.append("\\midrule")
    
    def add_bottom_rule(self):
        self.rows.append("\\bottomrule")
    
    def add_row(self, *args):
        cells = []

        for arg in args:
            if isinstance(arg, TableCell):
                cells.append(arg)
            elif isinstance(arg, list):
                cells.extend(arg)
            else:
                cells.append(TableCell(arg))

        self.rows.append(f"{' & '.join(map(str, cells))} \\\\")
        self.columns = max(self.columns, sum(cell.columns for cell in cells))

    def __str__(self):
        output = "\\begin{table}[htpb]\n"
        # output += "\\centering\n"
        
        if self.title:
            output += f"\\caption*{{{self.title}}}\n"

        output += f"\\begin{{tabular}}{{{'c' * self.columns}}}\n"

        output += "\\\\[-0.3cm] \n".join(map(str, self.rows))

        output += "\\end{tabular}\n"
        output += "\\end{table} \\\\\n"

        return output

class TableCell:
    def __init__(self, value, columns=1, style="r"):
        self.value = value
        self.columns = columns
        self.style = style
    
    def __str__(self):
        return f"\\multicolumn{{{self.columns}}}{{{self.style}}}{{{self.value}}}"