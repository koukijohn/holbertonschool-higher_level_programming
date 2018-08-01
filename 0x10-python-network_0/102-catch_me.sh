#!/bin/bash
# This bash script makes request to 0.0.0.0:5000/catch_me with response.
curl -sX PUT -L -d "user_id=98" -H "Origin:HolbertonSchool" "0.0.0.0:5000/catch_me"
