This was developed in python 3.7
The required modules are in the requirements.txt file
This project was developed using pycharm

The input file is in the following format:
3 -> Number of robots/number of starting points
5 5 -> Upper right co-ordinate
1 2 N -> Start point
LMLMLMLMM -> Moves
3 3 E
MMRMMRMRRM
5 5 N
M

Files:
inputs.txt -> The input arguments are in this file
outputs.txt -> The output gets written here
expected_outputs.txt -> The expected output is here to check with generated output
robot_navigation.py -> Runs the main function and contains all the functions. Running this file takes input from users manually
tests.py -> Runs 10 unittests to check for bugs. The test_main test in tests.py takes in the input file, writes the output file and then checks with expected_outputs

The code can be run by running the .py files from the command line or from an ide. Be mindful about installing the requirements. If the requirement is already installed, ignore after failing in pycharm and/or other ide

During development, a private git repo was used for version control
