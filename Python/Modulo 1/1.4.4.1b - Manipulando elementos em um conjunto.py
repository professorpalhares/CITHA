turma_python = {"Ana", "Beto", "Carla", "Daniel"}
turma_logica = {"Carla", "Daniel", "Eva", "Fabio"}

# 1. União (|): Quem sao todos os alunos, sem repeticao?
todos_alunos = turma_python | turma_logica
print(f"Todos os alunos\n {todos_alunos} \n")

# 2. Interseção (&): Quais alunos estao em AMBAS as turmas?
alunos_em_ambas = turma_python & turma_logica
print(f"Alunos em ambas as turmas\n {alunos_em_ambas} \n")

# 3. Diferença (-): Quais alunos fazem Python, mas não fazem Lógica?
alunos_so_python = turma_python - turma_logica
print(f"Alunos que so fazem Python\n {alunos_so_python}")