import numpy as np

def format_number(n):
    if n == np.inf:
        return "\\infty"

    notation = f"{n:.10g}"
    pieces = notation.split("e")

    if len(pieces) >= 2:
        return f"{pieces[0]} \\times 10^{{{int(pieces[1])}}}"
    
    return notation

def format_matrix(matrix):
    text = "\\begin{pNiceMatrix}\n"

    for row in map(np.asarray, matrix):
        text += f"{' & '.join(map(format_number, row.flatten()))} \\\\\n"

    text += "\\end{pNiceMatrix}"

    return text

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
        text = "\\begin{table}[htpb]\n"
        text += "\\centering\n"
        
        if self.title:
            text += f"\\caption*{{{self.title}}}\n"

        text += f"\\begin{{tabularx}}{{\\textwidth}}{{{' '.join('>{\\centering\\arraybackslash}X' for _ in self.columns)}}}\n"

        text += "\\toprule\n"
        text += f"{' & '.join(map(lambda e : f'${e}$', self.columns))} \\\\\n"
        text += "\\midrule\n"

        for row in self.rows:
            text += f"{' & '.join(map(lambda e : f'${e}$', row))} \\\\\n"

        text += "\\bottomrule\n"

        text += "\\end{tabularx}\n"
        text += "\\end{table} \\\\\n"

        return text

class MatrixBlock:
    def __init__(self):
        self.matrices = []

    def add_matrix(self, matrix, variable=None):
        self.matrices.append((matrix.copy(), variable))
    
    def __str__(self):
        text = "\\begin{NiceMatrixBlock}\n"
        text += "\\begin{align*}\n"

        for matrix, variable in self.matrices:
            if variable != None:
                text += f"{variable} &= "

            text += f"{format_matrix(matrix)} \\\\\n"

        text += "\\end{align*}\n"
        text += "\\end{NiceMatrixBlock}\n"

        return text

class Section:
    def __init__(self):
        self.elements = []
    
    def add_title(self, title):
        self.elements.append(f"\\textbf{{{title}}}\n")
    
    def add_subtitle(self, subtitle):
        self.elements.append(f"{subtitle}\n")
    
    def add_table(self, table):
        self.elements.append(table)
    
    def add_matrix_block(self, matrix_block):
        self.elements.append(matrix_block)
    
    def add_statement(self, statement):
        self.elements.append(statement)
    
    def __str__(self):
        return "\n".join(map(str, self.elements))



