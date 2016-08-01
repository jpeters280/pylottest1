"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import time
from datetime import date

class Appointments(Controller):
    def __init__(self, action):
        super(Appointments, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('AppointmentModel')
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
        
        # return self.load_view('index.html', messages=messages, user=user
        """
        appointments = self.models['AppointmentModel'].show_appointments(session['id'])
        appointments2 = self.models['AppointmentModel'].show_appointments2(session['id'])


        return self.load_view('appointments.html', appointments=appointments, appointments2=appointments2)

    def create(self):   
        print 'test'
        self.models['AppointmentModel'].create_appointment(request.form)
        print 'test'
        return redirect('/appointments')
        # if create_status['status'] == True:
        #     return redirect ('/appointments')
        # else:
        #     for message in create_status['errors']:
        #         flash(message, 'regis_errors')
        

    def delete(self,id):
        self.models['AppointmentModel'].delete_appointment(id)
        return redirect('/appointments')

    def edit(self,id):
        info = self.models['AppointmentModel'].show_appointment(id)
        print info
        return self.load_view('editappointment.html', info=info[0])

    def update(self):
        self.models['AppointmentModel'].update_appointment(request.form)
        return redirect ('/appointments')



        



