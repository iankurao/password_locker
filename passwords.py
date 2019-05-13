import random


class User:
    '''
    Class that generates new instances of a User
    '''
    user_list = []

    def __init__(self, username, account, password):
        self.username = username
        self.account = account
        self.password = password

    def save_user(self):
        '''
        save_user method saves user names into the user list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes the user info from user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
        '''
        Method takes in account name and displays user info for that particular account
        Args:
            Account name to search for
        Returns:
            User info for that account
        '''
        for details in cls.user_list:
            if details.account == account:
                return details
