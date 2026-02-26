from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Tic tac toe 3.0",
    version = "1.3",
    description = "Tic tac toe game with AI and player mode. Made by Junky",
    executables = [Executable(r"C:\Users\HP\Documents\Files\scripts\Python codes\tic tac toe UI v2.py")]
)

# naviguer jusqu'au répertoire et executer la ligne suivante :
# python script_to_exe.py build
# ou taper directement:
# python C:\Users\HP\Documents\Files\scripts\Python codes\script_to_exe.py build
