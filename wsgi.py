# Added to support deployment on Render.com
#  gunicon wsgi:app

from app import create_app

app = create_app()

