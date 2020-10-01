# nihongo8

## 1. development environment:
```
python 3.6.8
```
## 2. development setting:
```
git clone https://github.com/h4ppyy/nihongo8
cd nihongo8
python -m venv venv
```
mac or linux:
```
. venv/bin/activate
```
windows:
```
venv\Scripts\activate.bat
```
and Install the module:
```
pip install -r requirements.txt
```
change the information "DATABASES in settings.py"
```
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'YOUR DATABASE',
		'USER': 'YOUR DATABASE ID',
		'PASSWORD': 'YOUR DATABASE PASSWORD',
		'HOST': 'YOUR DATABASE HOST',
		'PORT': 'YOUR DATABASE PORT',
	}
}
```
and Insert basic data:
```
python manage.py makemigrations backend
python manage.py migrate backend
python manage.py loaddata doc/seed/seed.json
```
