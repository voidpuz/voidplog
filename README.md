# voidplog
Voidplog - void pointer's, blog. Created during the lesson for B4 group

---

# VOIDPLOG PROJECT


### 26 April, 2025

0. git clone "project"
1. venv yaratdik
2. django-admin startproject core .
3. python manage.py startapp posts
4. INSTALLED_APPSni configuratsiya qildik
5. Post modelini yozdik
6. ImageField supporti uchun Pillow o'rnatdik
7. python manage.py makemigrations && python manage.py migrate qildik
8. Post modeli uchun adminka config qildik
9. Superuser yaratdik va adminkaga kirib korib tekshirdik
10. REST_FRAMEWORK o'rnatamiz va INSTALLED_APPS ga config qo'shamiz
11. Post List API chiqaramiz:
    - views.py fayli ichiga PostListAPIView yozamiz, 
    - serializers.py fayliga PostListSerializer yozamiz
    - urls.py faylini ochib /posts/ GET api endpoint ochamiz.
12. Browsable API bilan tanishamiz.