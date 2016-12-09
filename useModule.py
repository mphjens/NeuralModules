#!/usr/bin/python
import sys
from NeuralModules import ModuleLoader, NeuralModule

"""Usage python useModule.py path_to_neural_module.zip"""
if(len(sys.argv) < 2):
    print("E: No module path given..")
else:
    modulePath = sys.argv[1]
    try:
        nm = ModuleLoader.loadModule(modulePath)
    except:
        print("E: Error loading module")
        exit()

    #main input loop
    while(True):
        rawcommand = raw_input()
        command = rawcommand.split(" ")
        # if exit command was read
        if(command[0] == "exit"):
            exit()

        if(len(command) > 1):
            #if predict single command was read
            if(command[0] == "ps"):
                print("O: " + nm.predictsingle_string(command[1]))

            # if predict batch command was read
            elif (command[0] == "pb"):
                print("O: " + nm.predictsingle_string(command[1].split(",")))
