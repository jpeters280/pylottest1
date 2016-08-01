"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('UserModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('users.html')
    
    def create(self):   
        create_status = self.models['UserModel'].create_user(request.form)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
            session ['email'] = create_status['user']['email']
            session ['name'] = create_status['user']['name']
            return redirect ('/appointments')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    def login(self):
        create_status = self.models['UserModel'].login_user(request.form)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
            session ['email'] = create_status['user']['email']
            session ['name'] = create_status['user']['name']
            return redirect ('/appointments')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    def logout(self):
        email = session['email']
        session.clear()
        session['email'] = email
        return redirect ('/')

    def goback(self):
        return redirect ('/appointments')