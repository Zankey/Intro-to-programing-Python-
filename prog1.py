

inputs = int(input("Enter the number of inputs: "))


valid_inputs = inputs #variable used to not count invalid inputs in loop count. 

for num_inputs in range(inputs):

    
    while valid_inputs >= 1:

        pattern = str(input("Enter the pattern you want to draw (X or <): "))
           
        if pattern == "X" or pattern == "x": #X pattern input

                rows = int(input("Enter the number of rows (must be an odd number): "))
                if rows % 2 != 0: #if it is odd, continue

                    valid_inputs -= 1 #subtract 1 from loop count only when both inputs are valid
                    step = rows // 2 
                    down_space = rows

                    for r in range(step): ############ TOP HALF ###########

                        for c in range(r): #spacing before first sharp
                            print(" ", end="")
                        print("#", end="")

                        down_space -= 2 #spacing before second sharp

                        for c_2 in range(down_space):
                            print(" ", end="")
                        print("#")

                    #####################################
                    for r in range(step): #MIDDLE SHARP
                        print(" ", end="")
                    print("#")
                    #####################################

                    up_space = 1
                    for r in range(step-1,-1,-1): ########### BOTTOM HALF ##########

                        for c in range(r): #spacing before first sharp
                            print(" ", end="")
                        print("#", end="")

                        
                        for c_2 in range(up_space): #spacing before second sharp
                            print(" ", end="")
                        print("#")
                        up_space +=2                                                               
                
                else:   #if number wasn't odd
                    print("You must enter an odd number of rows")
                                              
       
            
        elif pattern == "<": # < Pattern input
        

                rows = int(input("Enter the number of rows (must be an odd number): "))
                if rows % 2 != 0: #if it is odd, continue

                    valid_inputs -= 1
                    step = rows // 2 
                    down_space = rows

                    for r in range(step,0,-1): ########## TOP HALF ############
                        for c in range(r):
                            print(" ", end="")
                        print("*")

                    #################################
                    print("*") #prints middle *
                    #################################
                    
                    up_space = 1
                    for r in range(step-1,-1,-1): ############BOTTOM HALF #############

                        for c in range(up_space): #spacing before second sharp
                            print(" ", end="")
                        print("*")
                        up_space += 1
                        
       
                    
                
                else:   #if number wasn't odd
                    print("You must enter an odd number of rows")
                    
            
            
        else:  #asks for new pattern input if invalid
            print("invalid input (must be X or <)")
            
             
