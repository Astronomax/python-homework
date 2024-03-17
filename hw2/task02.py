import subprocess

from texlib import generate_latex_document


if __name__ == "__main__":
    table = [[f"{i}:{j}" for j in range(3)] for i in range(2)]
    latex_file = 'artifacts/task02/table.tex'
    try:
        with open(latex_file, 'w') as f:
            f.write(generate_latex_document(table=table, image="karich.png"))
        subprocess.run(["pdflatex", "-interaction=batchmode", "-output-directory=artifacts/task02/", latex_file], check=True)
    except Exception as e:
        print(f'An error has occurred: {e}')