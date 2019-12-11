![Auto-Search-Gif](/autosearch/autosearchapp/images/autosearch.gif "Auto_Search_gif")

### Installing

1. Clone down this repository and cd into it.
2. Once inside this repository, cd into `autosearch`
1. Create your virtual environment
```
python -m venv autosearchenv
```
* Start virtual environment on Mac
```
source ./autosearchenv/bin/activate
```
* Start virtual environment on Windows
```
source ./autosearchenv/Scripts/activate
```
5. Run `cd ..` You should be in a directory containing `requirements.txt`
6. Install the app's dependencies:
```
pip install -r requirements.txt
```
7. Run makemigrations
`python manage.py makemigrations autosearchapp`

8. Run migrate
`python manage.py migrate`
>This will create all the migrations needed for Django Framework to post items to the database based on the models in the Models/ directory
9. You'll need to creat an account with marketcheck.com and obtain an api key for their 'search api'<br>

 Once you have an api key, create a file called 'secrets.py' in the main directory and put your key inside <br>
 ```
 API_KEY="your API_KEY here"
 ```
## Run Server
make sure you're inside of the 'autosearch' directory

`python manage.py runserver `
Ctrl+C to quit

10. Go to http://127.0.0.1:8000/ and create an account <br>

11. Search for some vehicles and enjoy!


