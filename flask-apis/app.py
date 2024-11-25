from server import create_app

#import blue print
from server.routes.server_test import api_test_bp

#create app instance
app = create_app()

#Blue print register
app.register_blueprint(api_test_bp)

if __name__ == "__main__":
    #add host as 0.0.0.0 to be accessible from outside when running as a #container
    #app.run(host='0.0.0.0')
    app.run(debug=True, port=5000, host='0.0.0.0')