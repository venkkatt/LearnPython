"""
Normal compiler process in c/c++ --[Compiled Language]
1) we type the code in the source file
2) c/c++ compiler compiles the file and check for any errors
3) the code we write will be in high level language.
4) compiler convert the high level to low level code where processor can understand
5) low level file in object file
6) when we run the program object file will be loaded into  ram
7) Address of obj file in ram is sent to processor
8) then the processor reads each file line one by one and process the request
9) obj file and source file will be stored in hard disk
10) whatever has to run it will run from the ram
11) source code file will be directly converted to obj file
12) these languages execution speed will be faster.
13) this is platform dependent.
14) code written in windows can be executed only in windows compiler
15)
"""


"""
Python - [Interpreted Language]
1) python interpreter code is loaded into ram
2) inside python interpreter --> python virtual machine and compiler
3) compiler will run the source code file line by line and convert to byte code
4) PVM can understand byte code
5) compiler process each line by line.
6) because of that bit slow
7) platform independent
8) dynamically typed language 
9) used cpython for this process
10) there are other python like jpython and other available.mostly same process.

python -m py_compile guessthenum.py
 --> Above command will create __pycache__ folder
--> inside that .pyc file created for that program (compiled python format.
--> we can double click that file and it will show the output

"""