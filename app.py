from time import sleep
import logging

from project import create_app
from project.blueprints.board_game_geek import BoardGameGeek
from project.blueprints.fantazy_welt import FantazyWelt
from project.models.boardgame import Boardgame
from project.session import SQLiteSession

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("logFile.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Call the application factory function to construct a Flask application
# instance using the development configuration
# app = create_app("flask.cfg")

session = SQLiteSession()
fv = FantazyWelt(session, logger)
iterations = fv.get_total_pages()
for i in range(iterations):
    fv.check_store()
    sleep(10)

#bgg = BoardGameGeek(session, logger)
#iterations = bgg.get_total_pages()
#
#for i in range(iterations):
#    bgg.check_store()
#    sleep(10)
