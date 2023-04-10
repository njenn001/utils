#!/bin/bash

# Defines the main function.  
main(){

    # Gathers CPU information
    (lscpu | head -19)
}

# Runs the main function. 
main