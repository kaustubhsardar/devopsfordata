import os
from demo_app import app.*
app = create_app()
app.app_context().push()
app.test()
app.test_db()
