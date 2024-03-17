from texlib import generate_latex_document


if __name__ == "__main__":
    table = [[f"{i}:{j}" for j in range(3)] for i in range(2)]
    latex_file = 'artifacts/task01/table.tex'
    try:
        with open(latex_file, 'w') as f:
            f.write(generate_latex_document(table=table))
    except Exception as e:
        print(f'An error has occurred: {e}')