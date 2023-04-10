#!/bin/bash

# Defines the main function.  
main(){

    # Checks internet connectivity. 
    if ping -c 1 google.com &> /dev/null; then 
        echo 'connected'
    else 
        echo 'disconnected'
    fi 
}

# Runs the main function. 
main