# Silverfun Backend Distance Calculator 
This repository stores the source code for the backend distance calculator. This Python Flask application runs as a RESTful API server for users to send input parameters containing a latitude and longitude value along with a geoJSON file. The server will subsequently return the nearest 5 locations from the geoJSON file as a output.

## Installation
1. Clone repository into empty folder
```
https://github.com/sktlim/silverfun-backend
```
2. Install python3 and pip
3. Install required dependencies for calculator
``` 
pip3 install -r requirements.txt
```
4. Run application
```
flask --app app run
```

The application is now running and can be used for distance calculations. 
