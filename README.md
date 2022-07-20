# Django Direct Message

A complete one-to-one chat system using websockets and django channels.  

<br>

<img src="https://github.com/vimal-11/django_direct_message/blob/master/screenshot/ss.jpg" width="100%" height="100%">  


### Channels Documentation

https://channels.readthedocs.io/    
  
<br> 

## To Run
  
To run this project:

1. Clone this Repository
2. Navigate to the directory with this README
3. Create virtualenv  - Optional

```bash
virtualenv venv -p python3.9
source venv/bin/activate
# venv\Scripts\activate on Windows
```  
  
4. Install the requirements for the package:

```
pip install -r requirements.txt 
```  

5. Go up a folder 

```
cd ..
```

6. Apply migrations

```
python manage.py migrate
```

7. Create Superuser

```
python manage.py createsuperuser
```  

8. Run the server

```
python manage.py runserver
```

9. Access the browser on

```
http://127.0.0.1:8000
```



