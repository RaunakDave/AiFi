#! /bin/bash

curl -X POST -d "{\"customer\": {\"FirstName\": \"Raunak\", \"LastName\": \"Dave\", \"Age\": \"31\", \"Email\": \"raunak_dave@icloud.com\", \"case\": [{\"Number\": \"1\", \"StartTimeStamp\": \"0\", \"EndTimeStamp\": \"1\", \"store\": {\"Name\": \"BLR\", \"Address\": \"Bangalore\"}}, {\"Number\": \"2\", \"StartTimeStamp\": \"2\", \"EndTimeStamp\": \"3\", \"store\": {\"Name\": \"NM\", \"Address\": \"New Mexico\"}}]}}" http://localhost:5000/customer
curl -X POST -d "{\"customer\": {\"FirstName\": \"Brian\", \"LastName\": \"Bates\", \"Age\": \"32\", \"Email\": \"brian_bates@icloud.com\", \"case\": [{\"Number\": \"1\", \"StartTimeStamp\": \"0\", \"EndTimeStamp\": \"1\", \"store\": {\"Name\": \"NY\", \"Address\": \"Las Vegas\"}}]}}" http://localhost:5000/customer
curl -X POST -d "{\"customer\": {\"FirstName\": \"Will\", \"LastName\": \"Hendry\", \"Age\": \"33\", \"Email\": \"will_hendry@icloud.com\", \"case\": [{\"Number\": \"1\", \"StartTimeStamp\": \"8\", \"EndTimeStamp\": \"9\", \"store\": {\"Name\": \"NY\", \"Address\": \"Las Vegas\"}}, {\"Number\": \"2\", \"StartTimeStamp\": \"7\", \"EndTimeStamp\": \"8\", \"store\": {\"Name\": \"LA\", \"Address\": \"Los Angeles\"}}]}}" http://localhost:5000/customer
curl -X POST -d "{\"customer\": {\"FirstName\": \"Tomas\", \"LastName\": \"Rivera\", \"Age\": \"34\", \"Email\": \"tomas_rivera@icloud.com\", \"case\": [{\"Number\": \"1\", \"StartTimeStamp\": \"13\", \"EndTimeStamp\": \"15\", \"store\": {\"Name\": \"BLR\", \"Address\": \"Bangalore\"}}, {\"Number\": \"2\", \"StartTimeStamp\": \"12\", \"EndTimeStamp\": \"13\", \"store\": {\"Name\": \"BLR\", \"Address\": \"Bangalore\"}}]}}" http://localhost:5000/customer