import os
from demo_app.app import create_app
app = create_app()
app.app_context().push()

app.test()
app.test_db()
