#!/usr/bin/env python3.6
from passwords import User
import random
from passwords import Credentials
from getpass import getpass

def create_user(username, account,password):
    '''
    Function to create a new user
    '''
    new_user = User(username, account,password)
    return new_user


def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(account):
    '''
    Function that finds a user by account name and returns the  user
    '''
    return User.find_by_account(account)

def check_existing_user(account):
    '''
    Function that checks if a user exists with that account and returns Boolean
    '''
    return User.user_exists(account)

def display_users():
    '''
    Function that returns all saved users
    '''
    return User.display_users()

 
def save_password(credentials):
    '''
    Function that saves new password
    '''
    return credentials.save_password()

def generate_password():
    '''
    Function that generates a password for the user
    '''
    return Credentials.generatePassword()
   

