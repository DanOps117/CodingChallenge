# SailPoint-CodingChallenge
This is a Coding Challenge feel free to clone and fork!

To test the code please follow the next steps:

1. for test the `send_email.py` functionallity you need to add the necessary credentials fron a valid `SMTP server` you can find a free SMTP server on the next link https://moosend.com/blog/free-smtp-server/
   if you don't want to test you can execute the script and the timeout finish the execution of the program. 
2.

   # TEST ON YOUR LOCAL
   you can test the script on your local machine installing python3 and using venv, On `MacOS` or `Linux` you can follow the next steps, if you are using Windoge you can install `WSL2` 
```   
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python3 ./app.py
```
  # TEST WITH DOCKER
  build the docker image with the next command you need have docker already installed
```
  docker build -t pr-report-app .
  docker run -p 5000:5000 pr-report-app
```
3. Open your web browser and type the next URL http://localhost:5000
4. Add the required information
```
   - github user
   - github repo
   - number of week in the past
   - stakeholder's email
```
5. After put the information a new window with the report appears and if all is correct click on the button to send the report to the stakeholder.
   
