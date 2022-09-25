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
