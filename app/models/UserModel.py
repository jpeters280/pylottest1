""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class UserModel(Model):
    def __init__(self):
        super(UserModel, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        query = 'SELECT * from users where email = :email limit 1'
        data= {'email':info['email']}
        email=self.db.query_db(query, data)
        print info
        if email:
            errors.append('email is already in system please use log in')
        else:
            if not info['name']:
                errors.append('Name cannot be blank!')
            elif len(info['name']) < 2:
                errors.append('Name must be at least 2 characters long!')
            if not info['email']:
                errors.append('Email cannot be blank!')
            elif not EMAIL_REGEX.match(info['email']):
                errors.append('Email format must be valid!')
            if not info['password']:
                errors.append('Password cannot be blank!')
            else:
                if len(info['password']) < 8:
                    errors.append('Password must be at least 8 characters long!')
                if not re.search(r'\d',info['password']):
                    errors.append('Password must contain at least one digit!')
                if not re.search(r'[A-Z]',info['password']):
                    errors.append('Password must contain at least one uppercase letter!')
                if not re.search(r'[a-z]',info['password']):
                    errors.append('Password must contain at least one lowercase letter!')
                if not re.search(r'\W', info['password']):
                    errors.append('Password must contain at least one symbol!')
            if info['password'] != info['confirm']:
                errors.append('Password and confirmation must match!')
        if errors:
            return {"status": False, "errors": errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])
            data2 =  {'name':info['name'], 'birthday':info['birthday'], 'email':info['email'],'pw_hash':pw_hash}
            query_insert = "INSERT into users (name, birthday, email, pw_hash, created_at, updated_at) Values (:name, :birthday, :email, :pw_hash, NOW(), NOW())"
            self.db.query_db(query_insert, data2)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

    def login_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not info['email']:
            errors.append('Email cannot be blank!')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        else:
            query = 'SELECT * from users where email = :email limit 1'
            data = { "email" :info['email'] }
            email = self.db.query_db(query, data)
            if not email:
                errors.append('Email not on file please register')
            elif not self.bcrypt.check_password_hash(email[0]['pw_hash'], info['password']):
                errors.append('password does not match the one on file')
        if errors:
            return { "status": False, "errors": errors }
        else:
            return { "status": True, "user": email[0] }