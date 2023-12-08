class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input().split()
    if command[0] == 'Stop':
        break
    email = Email(command[0], command[1], command[2])
    emails.append(email)

send_mails = [int(x) for x in input().split(', ')]
for i in send_mails:
    emails[i].send()
for mail in emails:
    print(mail.get_info())