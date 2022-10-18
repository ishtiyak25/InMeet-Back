# InMeet

InMeet is a Django based task and meeting management tool

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages for InMeet.

## Crete virtual environment

```virtualenv
# install virtual environment in machine
python -m pip install --user virtualenv
# create virtualenv in preferred location
virtualenv venv
```

## Installable Packages

```
djanago
rest_framework
rest_framework_simplejwt
corsheaders
import_export
whitenoise
drf-spectacular
```

## Run

```
#install requirements
pip install -r requirements.txt

# run a migration
python manage.py makemigrations
python manage.py migrate

# returns 'phenomenon'
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)