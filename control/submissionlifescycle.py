from emailapi import EMAIL

class SubmissionControl:

    #sTEP 1 - save the data

    #step 2 - Do whaterever you need to do

    #Step 3 - send the notifications

    def __init__(self, json_data=[]):
        self.json_data = json_data
        self.id = json_data['id']
        self.emailAddr = json_data['email']

    def ProcessSubmission(self, command):
        if command == 'sub':
            # send to sub db 
            subject = "Submission Confirmation ID: " + str(self.id)
            content = "Your record has been submitted successfully and will be reviewed shortly."
        elif command == 'man':
            subject = "New Submission ID: " + str(self.id)
            content = "New record has been submitted."
            self.emailAddr = 'ryuichi1174@gmail.com'
        elif command == 'fabRej':
            # update sub db command
            subject = "ID: " + str(self.id) + " Rejected"
            content = "Your submission has been rejected."

        email = EMAIL()
        email.send_email(self.emailAddr, subject, content)