# Wavepool
Industry Dive's django code exercise for software engineer candidates. I did not pass.

Thoughts: This is a great reference for templating in the future, if I ever encounter a need to use the template language for Django again.

Main takeaways: 
  -autoescaping can be a security flaw => see myspace. 
  -you can clean() a model on save to enact changes to other models if necessary, in this case, enforcing a unique model value. Definitely need to know this in the future. Maybe I would have passed if I didn't mess this part up.
  -Never forget to make/run migrations again!
  -Next time install whatever dependencies exist to the letter before the start of the project. In this case, it was pipenv.
  -Admin.py file customizes a good amount of the functionality that goes into the vanilla Django CMS experience. If I end up using Django to host my blog this is what I could look into.
  
-some tasks:
-fix and implement all included tests
-implement view in admin.py file

Based on feedback from ID. 
  - in the future, verify solutions with included tests or write them for programming assessments
  - make migrations and migrate
  - General knowledge on using template/MVC features of Django. Perhaps before future programming challenges look into reading one or more pages of documentation of features i have not used to implement before. 
  - Unique boolean cuts off after true and false, invalidating every single other value after the first two.


## Requirements
* Python 3
* Pipenv or other python virtual environment package

## Install & run
Using pipenv:

Install an environment using python 3

`pipenv install`
or
`pipenv install --python your-path-to-python3`

SSH into your environment
`pipenv shell`

Serve the app locally
`python manage.py runserver`

If you do not want to use pipenv, you can install requirements for your environment found in the `requirements.txt` file.

## Use
Navigate in your browser to the wavepool homepage at `http://127.0.0.1:8000/`

Click on the "Instructions" link to view the assessment instructions.

## CMS Admin
To log into the Django CMS Admin, navigate to `http://127.0.0.1:8000/admin` and use the username `divecandidate` and password `divecandidatetest` to log in.
