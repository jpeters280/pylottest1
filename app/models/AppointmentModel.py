""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import time
from datetime import date 

class AppointmentModel(Model):
    def __init__(self):
        super(AppointmentModel, self).__init__()
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
    def show_appointments(self, id):
        query = 'SELECT * from appointments where appointments.user_id = :id and date>CURDATE()'
        data = {'id':id}
        return self.db.query_db(query, data)

    def show_appointments2(self, id):
        query = 'SELECT * from appointments where appointments.user_id = :id and date=CURDATE()'
        data = {'id':id}
        return self.db.query_db(query, data)

    def show_appointment(self, id):
        query = 'SELECT * from appointments where appointments.id = :id'
        data = {'id':id}
        return self.db.query_db(query, data)


    def create_appointment(self,info):
        # today = date.today()
        # errors = []
        # if info['date'] >= today:
        print info
        query = "INSERT into appointments (task, status, date, time, created_at, updated_at, user_id) values (:task, 'pending', :date, :time, NOW(), NOW(), :user_id)"
        data = { 'task':info['task'],'date':info['date'],'time':info['time'], "user_id":info['id']}
        print 'test'
        return self.db.query_db(query, data)
            # return { "status": True }
        # else:
        #     errors.append('Password and confirmation must match!')
        #     return { "status": False, "errors": errors }

    def delete_appointment(self,id):
        query = 'DELETE from appointments where appointments.id = :id'
        data = { 'id':id}
        return self.db.query_db(query, data)

    def update_appointment(self, info):
        query = 'UPDATE appointments set task =:task, status=:status, date=:date,time=:time, updated_at=NOW() where appointments.id=:id'
        data={ 'task':info['task'],'date':info['date'],'time':info['time'], "id":info['id'], 'status':info['status']}
        return self.db.query_db(query,data)

        