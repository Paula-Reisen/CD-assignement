# CD-assignement
Assignment Winc Academy Continuous Development Pipeline

# Main.Py
Simple code for pushing with use of FLASK module. With flask we publish hello world to app using fuction app.route. The main route goes to Hello, World! and /cow goed to MOoooOo!

# Test_run.py
Tests main.py 

# requirements.txt
Github actions run-pipeline gets stored in this documents. You see this in the run-pipeline.yml file with the sentence: pip install -r requirements.txt

# run_actions.yml
Stores the ipadres from droplet and also gives the password for digital ocean droplets. Only runs after the completion of run-pipeline.yml

# run_pipeline.yml
Runs the test and also installs python and pytest in the host. We have chosen ubuntu to run the commands in. 

# Secrets
There are two installed secrets, namely:
* CD_SECRET: Contains IPadres for website cd-assignment
* PASSWORD_ROOT: Contains password to publish the changes

# problems SSH Keys
Two problems with ssh keys where
* knowing I had to login as root on droplet server and generate a public/private key
* Then the necessary steps I had to take to make the connection with github. 
By loooking on google i found https://medium.com/swlh/how-to-deploy-your-application-to-digital-ocean-using-github-actions-and-save-up-on-ci-cd-costs-74b7315facc2. This link helped me to get the connection started. 

# problem 2
I had an issue with getting my gitactions working. 
* workflow names where incorrect
* before I found the link above I didn't get the connection working with droplet to update the site. 
    Fixing the names so the test did run
    Creating the correct connection with github and adding the right secrets

# problem 3
I had a problem with the format of the yml file: 
    * The steps was not in the right place
    * The syntax wasn't correct
Try multiple times just to find the right format so it didn't fail on the syntax. 