import os

var_string = []
for param in os.environ.keys():
    var_list = {param : os.environ[param]}
    var_string.append(var_list)
    #var_string.append("\n")
for i in var_string:
    print str(i)

    
        
 
