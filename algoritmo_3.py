import tkinter as tk
from tkinter import simpledialog, messagebox

def columnar_transposition_cipher(message, n):
    # Eliminar espacios
    message = message.replace(" ", "")
    
    # comprobar que el mensaje sea menor o igual a n*n
    if len(message) > n * n:
        raise ValueError("The message length must be less than or equal to n * n")
    
    # Llenar espacios vacios con *
    while len(message) < n * n:
        message += '*'
    
    # Matirz de n x n
    matrix = []
    for i in range(n):
        row = list(message[i*n:(i+1)*n])
        matrix.append(row)
    print(matrix)
    # filas por columnas
    ciphered_message = ""
    for col in range(n):
        for row in range(n):
            ciphered_message += matrix[row][col]
    
    return message, ciphered_message

def get_input():
    root = tk.Tk()
    root.withdraw()  

    message = simpledialog.askstring("Mensaje", "Ingrese el mensaje:")
    n = simpledialog.askinteger("N", "Ingrese el tamaño de la matriz:")

    return message, n

def main():
    try:
    
        message, n = get_input()

        # Hacer la transposicion de columnas
        original_message, ciphered_message = columnar_transposition_cipher(message, n)

        # Muestra los resultados
        result_message = f"Mensaje original: {original_message}\nMensaje cifrado: {ciphered_message}"
        messagebox.showinfo("Resultado", result_message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    main()
