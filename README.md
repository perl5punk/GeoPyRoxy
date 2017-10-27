# GeoPyRoxy

This will help you interface with multiple GeoCoding Sources in one place, have fun.

## Installation / Running

1. Install Python
2. Fork and Clone the Repo
3. Obtain API Keys for Geocode services and add to __config.py__
    https://developer.here.com/documentation/geocoder/topics/quick-start-geocode.html
    https://developers.google.com/maps/documentation/geocoding/get-api-key
4. Start Server (Defaults to Port 8000)


    python entry.js
    
    
 ## RESTful Endpoints and Usage
 
 - GET /geocode/{address}
 - GET /reverse/{longitude}/{latitude}
 
 ##### Example
 
    http://localhost:8000/geocode/1855%20Haight%20St,%20San%20Francisco,%20CA%2094117
    
 ##### Output
 
    []
    