def generate_latex_table(table):
    return """\\begin{{table}}[h!]
\\centering
\\begin{{tabular}}{{{0}}}
\\hline
{1}
\\hline
\\end{{tabular}}
\\caption{{Generated using texlib.py!}}
\\end{{table}}
""".format(
    f'|{"|".join(["c"] * len(table[0]))}|',
    "\n\\hline\n".join(map(lambda row: f'{" & ".join(map(str, row))} \\\\', table)))

def generate_image_latex(image):
    return """\\begin{{figure}}[h!]
\\centering
\\includegraphics[width=0.5\\textwidth]{{\"{0}\"}}
\\caption{{Generated using texlib.py!}}
\\end{{figure}}
""".format(image)

def generate_latex_document(table = None, image = None):
    return """\\documentclass{{article}}
\\usepackage{{graphicx}}

\\begin{{document}}

{0}

{1}

\\end{{document}}
""".format(
    "" if table is None else generate_latex_table(table),
    "" if image is None else generate_image_latex(image))
