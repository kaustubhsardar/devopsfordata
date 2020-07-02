import os


command1 = os.system("python manage.py db init")
command2=os.system("python manage.py db migrate")
command3=os.system("python manage.py db upgrade")
command4=os.system("python manage.py db downgrade")

print(command1+"\n"+command2+"\n"+command3+"\n"+command4)
