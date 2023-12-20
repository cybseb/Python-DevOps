#!/bin/bash
import os

def install_apache():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y apache2')

def install_ssh():
    os.system('sudo apt-get update'
    os.system('sudo apt-get install -y openssh-server')

if __name__ == '__main__':
    install_apache()
    install_ssh()

