# Django Web Framework abc

### Set up

1. Start a trial project 

   ```bash
   django-admin startproject trydjango .
   python manage.py runserver
   ```

   

2. Sync the setting.py with project

   ```bash
   python manage.py migrate
   ```

   

### componant

Before doing modification, remember to migrate first. Recommand to runserver on the other terminal.

1. Create supersuser(admin)

   ```bash
   python manage.py createsuperuser
   ```


2. custermized componant

   ```bash
   python manage.py startapp <custermized name>
   
   # do modification on the model.py file
   # add it into setting.py
   
   python manage.py makemigrations
   python manage.py migrate
   
   # and regiter mdel in admin.py(reletive import)
   ```

### Create Object in shell

```bash
python manage.py shell
Insurance.objects.all() # show the objects in the class
Insurance.objects.create(title='something', land='something') #create object
```



