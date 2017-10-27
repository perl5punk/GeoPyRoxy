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
 
    {
       "results" : [
          {
             "address_components" : [
                {
                   "long_name" : "1855",
                   "short_name" : "1855",
                   "types" : [ "street_number" ]
                },
                {
                   "long_name" : "Haight Street",
                   "short_name" : "Haight St",
                   "types" : [ "route" ]
                },
                {
                   "long_name" : "Haight-Ashbury",
                   "short_name" : "Haight-Ashbury",
                   "types" : [ "neighborhood", "political" ]
                },
                {
                   "long_name" : "San Francisco",
                   "short_name" : "SF",
                   "types" : [ "locality", "political" ]
                },
                {
                   "long_name" : "San Francisco County",
                   "short_name" : "San Francisco County",
                   "types" : [ "administrative_area_level_2", "political" ]
                },
                {
                   "long_name" : "California",
                   "short_name" : "CA",
                   "types" : [ "administrative_area_level_1", "political" ]
                },
                {
                   "long_name" : "United States",
                   "short_name" : "US",
                   "types" : [ "country", "political" ]
                },
                {
                   "long_name" : "94117",
                   "short_name" : "94117",
                   "types" : [ "postal_code" ]
                },
                {
                   "long_name" : "2711",
                   "short_name" : "2711",
                   "types" : [ "postal_code_suffix" ]
                }
             ],
             "formatted_address" : "1855 Haight St, San Francisco, CA 94117, USA",
             "geometry" : {
                "bounds" : {
                   "northeast" : {
                      "lat" : 37.7692264,
                      "lng" : -122.4523678
                   },
                   "southwest" : {
                      "lat" : 37.7686442,
                      "lng" : -122.4529183
                   }
                },
                "location" : {
                   "lat" : 37.7689353,
                   "lng" : -122.452643
                },
                "location_type" : "ROOFTOP",
                "viewport" : {
                   "northeast" : {
                      "lat" : 37.77028428029151,
                      "lng" : -122.4512940697085
                   },
                   "southwest" : {
                      "lat" : 37.76758631970851,
                      "lng" : -122.4539920302915
                   }
                }
             },
             "place_id" : "ChIJxwMQf1GHhYAR0jvdnmdzNBo",
             "types" : [ "premise" ]
          }
       ],
       "status" : "OK"
    }
    