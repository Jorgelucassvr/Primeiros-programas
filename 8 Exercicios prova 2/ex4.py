biblioteca = {
    "978-3-16": ["Dom casmurro","machado de assis",3],
    "978-1-23": ["1984", "george orwell", 1]
}

def emprestar_livro(isbn):
    if biblioteca[isbn][2] > 0 :
        biblioteca[isbn][2] -= 1
        print(f"Livro '{biblioteca[isbn][0]}' emprestado! Estoque restante: {biblioteca[isbn][2]}")
    else:
        print(f"Livro '{biblioteca[isbn][0]}' sem estoque!")

def devolver_livro(isbn):
    biblioteca[isbn][2] += 1
    print(f"Livro '{biblioteca[isbn][0]}' devolvido! Estoque atual: {biblioteca[isbn][2]}")
