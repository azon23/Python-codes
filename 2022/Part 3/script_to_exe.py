from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Tic tac toe 3.0",
    version = "1.3",
    description = "Tic tac toe game with AI and player mode. Made by Junky",
    executables = [Executable(r"path\to\the\python\file\to\compile\in\exe")]
)

# naviguer jusqu'au répertoire et executer la ligne suivante :
# python script_to_exe.py build
# ou taper directement:
# python absolute\path\Part 3\script_to_exe.py build
