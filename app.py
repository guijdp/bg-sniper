from time import sleep

from project import create_app
from project.blueprints.fantazy_welt import FantazyWelt
from project.session import SQLiteSession

# Call the application factory function to construct a Flask application
# instance using the development configuration
# app = create_app("flask.cfg")

session = SQLiteSession()
fv = FantazyWelt(session)
iterations = fv.get_total_pages()

for i in range(iterations):
    fv.check_prices()
    sleep(10)
