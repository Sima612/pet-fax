from flask import Flask

def create_app():

    app = Flask(__name__)
    from . import pet
    from . import fact
    
    @app.route('/')
    def home():
        return 'Hello, PetFax!'
    
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app