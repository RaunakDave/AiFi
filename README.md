#### Challenge 1:

Usage:    
Install minikube:  
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64  
sudo install minikube-darwin-amd64 /usr/local/bin/minikube  
Start minikube:  
minikube delete && minikube start --vm-driver=docker  
Apply all 1 .yaml:  
kubectl apply -f dapi-envars-container.yaml  
See logs:  
kubectl logs init-demo  

### Challenge 2:

I have taken a few liberties with this challenge. I hope that's okay. If not, please let me know.

I have decided to dockerise my app and the db. I have also written configuration files to deploy the containers on kubernetes.
Also, I am using mongoDB to model the tables and relationships described in the challenge.

The reason for the 2 decisions above is that I was asked a few questions regarding mondoDB by Will in my interview with him.
And I wasn't able to comprehend what he was trying to ask me. I hope my code might be able to answer those questions on my behalf. I hope this helps you gleam into what I know and do not know.

Thus CRUD operations are available at the customer level.
CRUD operations at the case and store level can be performed by using the PUT operation at the customer level.

Having said that, I have provided views into the DB which are centered around cases and stores.
You can invoke those views by calling the /stores and /cases endpoints.

And performance testing is done for the GET of all 3 views as requested.

I am using only one collection to model the necessary relationships. That collection is called "customer".

The schema of each document in the customer collection is as below:

{  
"customer":  
{  
"FirstName": "Raunak",  
"LastName": "Dave",  
"Age": "31",   
"Email": "raunak_dave@icloud.com",  
"case":  
[  
{  
"Number": "1",  
"StartTimeStamp": "0",  
"EndTimeStamp": "1",  
"store":  
{  
"Name": "BLR",  
"Address": "Bangalore"  
}  
},  
{  
"Number": "2",  
"StartTimeStamp": "2",  
"EndTimeStamp": "3",  
"store":  
{  
"Name": "NM",  
"Address": "New Mexico"  
}  
}  
]  
}  
}  

Bootstrapping has been done for the DB with some dummy entries.

Usage:  
Install docker.  
Start docker.  
Install minikube:  
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64  
sudo install minikube-darwin-amd64 /usr/local/bin/minikube  
Start minikube:  
minikube delete && minikube start --vm-driver=docker  
Apply all 6 .yamls.  
Bash into the app pod:  
kubectl exec -it app-xxxxxxxx bash  
Bootstrap DB:  
chmod +x bootstrap_db.sh  
./bootstrap_db.sh  

See usage.txt for usage.

Performance Testing:  
Bash into the app pod:  
kubectl exec -it app-xxxxxxxx bash  
Bootstrap DB:  
chmod +x bootstrap_db.sh  
./bootstrap_db.sh  
locust -f tester.py --headless -u 1000 -r 100 --host wfng  
Ctrl + c at your own leisure.  
