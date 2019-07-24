# API-MUSIC
api for music lists

Testing using Postman and Debian 9

Publish Postman : https://documenter.getpostman.com/view/8200038/SVSRGR9F

cara menjalankan (dengan menggunakan os linux):
1. buka terminal pada directory file
2. install virtualenv "pip install virtualenv"
3. buat virtualenv "virtualenv -p python3 api_env"
4. aktifkan virtualenv ". {direktori virtualenv}/bin/activate"
5. lakukan migrasi database "python manage.py makemigrations", "python manage migrate"
6. run server "python manage.py runserver"
7. server akan running di "http://127.0.0.1:8000/"
