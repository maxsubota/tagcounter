# django-tagcounter

django-tagcounter is a minimal application to count a tag statistic on website page.

That are glued together with [initializr](http://www.initializr.com/). And its current `requirements.txt` file is:

```
Django=2.1.4
chardet=3.0.4
decorator=4.3.0
idna=2.8
lxml=4.2.5
pytz=2018.7
requests=2.21.0
setuptools=39.1.0
six=1.12.0
urllib3=1.24.1
validators=0.12.3
```

## Installation

### 1. virtualenv 
You should already know what is [virtualenv](http://www.virtualenv.org/). So, simply create it for your own project, where `projectname` is the name of your project:

`$ virtualenv --clear projectname`

### 2. Download
Now, you need the *django-tagcounter* project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone https://github.com/maxsubota/tagcounter.git projectname && cd projectname

### 3. Requirements
Right there, you will find the *requirements.txt* file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:

`$ pip install -r requirements.txt`




#### Initialize the database

`./manage.py makemigrations`

`./manage.py migrate`

### Ready? Go!

`./manage.py runserver`