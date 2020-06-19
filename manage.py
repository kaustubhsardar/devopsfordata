import os
from demo_app.app import create_app, test,test_db
app = create_app()
app.app_context().push()
test()
test_db()
