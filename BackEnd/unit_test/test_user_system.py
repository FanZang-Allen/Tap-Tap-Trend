"""
Unit test for user_system.py
"""
from unittest import TestCase
from BackEnd import user_system
from BackEnd.database import database


class TestUserSystem(TestCase):
    """
    Class containing all test about user_system
    """
    def test_add_user(self):
        """
        Test add user correctly add a user doc to database
        """
        before_user_count = database['User'].count_documents({})
        user_system.add_user('test_name', 'test_password')
        curr_user_count = database['User'].count_documents({})
        self.assertEqual(before_user_count + 1, curr_user_count)
        database['User'].delete_one({'user_name': 'test_name'})

    def test_check_user_exist(self):
        """
        Test check_user_exist correctly identify exist user
        """
        new_user_id = user_system.add_user('test_name', 'test_password')
        self.assertTrue(user_system.check_user_exist(new_user_id))
        database['User'].delete_one({'user_name': 'test_name'})

    def test_change_password(self):
        """
        Test change_password correctly change user password in database
        """
        new_user_id = user_system.add_user('test_name', 'test_password')
        query_cursor = database['User'].find({'user_name': 'test_name'}, {'password': 1})
        curr_password = list(query_cursor)[0]['password']
        self.assertEqual(curr_password, 'test_password')

        user_system.change_password(new_user_id, 'new_password')
        query_cursor = database['User'].find({'user_name': 'test_name'}, {'password': 1})
        curr_password = list(query_cursor)[0]['password']
        self.assertEqual(curr_password, 'new_password')
        database['User'].delete_one({'user_name': 'test_name'})

    def test_change_user_name(self):
        """
        Test change_user_name correctly change user name in database
        """
        new_user_id = user_system.add_user('test_name', 'test_password')
        query_cursor = database['User'].find({'id': new_user_id}, {'user_name': 1})
        curr_name = list(query_cursor)[0]['user_name']
        self.assertEqual(curr_name, 'test_name')

        user_system.change_user_name(new_user_id, 'new_name')
        query_cursor = database['User'].find({'id': new_user_id}, {'user_name': 1})
        curr_name = list(query_cursor)[0]['user_name']
        self.assertEqual(curr_name, 'new_name')
        database['User'].delete_one({'id': new_user_id})

    def test_add_favourite_game(self):
        """
        Test add_favourite_game correctly add a game to user favourite list
        """
        new_user_id = user_system.add_user('test_name', 'test_password')
        query_cursor = database['User'].find({'id': new_user_id}, {'favourite_list': 1})
        curr_list = list(query_cursor)[0]['favourite_list']
        self.assertEqual(len(curr_list), 0)

        user_system.add_favourite_game(new_user_id, '2')
        query_cursor = database['User'].find({'id': new_user_id}, {'favourite_list': 1})
        curr_list = list(query_cursor)[0]['favourite_list']
        self.assertTrue('2' in curr_list)
        database['User'].delete_one({'id': new_user_id})

    def test_remove_favourite_game(self):
        """
        Test add_favourite_game correctly add a game to user favourite list
        """
        new_user_id = user_system.add_user('test_name', 'test_password')
        user_system.add_favourite_game(new_user_id, '2')
        query_cursor = database['User'].find({'id': new_user_id}, {'favourite_list': 1})
        curr_list = list(query_cursor)[0]['favourite_list']
        self.assertEqual(len(curr_list), 1)

        user_system.remove_favourite_game(new_user_id, '2')
        query_cursor = database['User'].find({'id': new_user_id}, {'favourite_list': 1})
        curr_list = list(query_cursor)[0]['favourite_list']
        self.assertEqual(len(curr_list), 0)
        database['User'].delete_one({'id': new_user_id})
