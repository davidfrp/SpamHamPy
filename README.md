DEPLOYMENT STEPS:

STEP 1 : Create a virtual environment with pipenv and install Flask and Gunicorn .
```bash
$ pipenv install flask gunicorn 
```

STEP 2 : Create a “Procfile” and add the following:
```bash
$ touch Procfile
```
``` 
web: gunicorn wsgi:app
```

STEP 5 : Create a python file, “main.py” and enter our app code.

```bash
$ mkdir app
$ cd app
$ touch main.py
```

STEP 6 :Get back to the previous directory “eflask”.Create a file“wsgi.py” and insert the following code:
 
```py 
from app.main import app
if __name__ == "__main__":
   app.run()
```

STEP 7: INSTALL TENSOFLOW-CPU, LIGHTWEIGHT VERSION!

STEP 8 : Run the virtual environment.
```bash
$ pipenv shell
```

STEP 9 : Initialize an empty repo, add the files in the repo and commit all the changes
```bash
$ git init 
$ git add .
$ git commit -m "Initial Commit"
```

STEP 10 : Login to heroku and push the repo
```bash
$ git push heroku main
```
