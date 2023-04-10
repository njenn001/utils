#!/bin/bash

# Defines the main function.  
main(){

    # Shows free memory space. 
    (free | awk '/^Mem/ { printf("Free Memory: %.2f %\n", $4/$2 * 100.0) }')

}

# Runs the main function. 
main