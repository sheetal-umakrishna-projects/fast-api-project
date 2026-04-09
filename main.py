import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)
    ## What above means: we want to use uvicorn(web server) which is already installed and we want to run the web-server

    ## For the webserver, we want to run an API on it. And the API we want to run is app.app (this is the app file inside the app folder), and the API (FastAPI) is inside the variable 'app' in app.py file in our 'app' folder
    # Host: this is the domain that we want to run the server on. 0.0.0.0 means = run it on any available domain (since we are using it for our local use) -> will run on 'local host' which is our own host which only we can access and our private IP address (i.e anyone on the network would be able to access it if they knew the private IP address of this machine)


