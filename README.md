# [Django Admin Argon](https://github.com/app-generator/django-admin-argon-dashboard)

Modern template for **Django Admin Interface** coded on top of **Argon Dashboard**, an open-source `Boostrap 5` design from `Creative-Tim`.

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br>

**Links & Resources**

- UI Kit: [Argon Dashboard BS5](https://www.creative-tim.com/product/argon-dashboard?AFFILIATE=128200) `v2.0.4` by Creative-Tim
- [Django Argon Dashboard](https://django-argon-dashboard.appseed-srv1.com/) - LIVE Demo
- [Django Argon Dashboard](https://github.com/app-generator/django-argon-theme-playground) - `playground project` 

<br />

## [Black Friday](https://appseed.us/discounts/) - `75%OFF`

> The campaign is active until `30.NOV` and applies to all products and licenses.

[![AppSeed - Black Friday 2022 Campaign, 75% OFF Discount (all products).](https://user-images.githubusercontent.com/51070104/201829599-9fe6bdd7-3f19-46f3-9115-962eeb13bf29.jpg)](https://appseed.us/discounts/)

<br />

## Why `Django Argon Design`

- Modern `Bootstrap 5` Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`

<br />

## How to use it

<br />

> **Install the package** via `PIP` 

```bash
$ pip install django-admin-argon-dashboard
// OR
$ pip install git+https://github.com/app-generator/django-admin-argon-dashboard.git
```

<br />

> Add `admin_argon` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file (note it should be before `django.contrib.admin`):

```python
    INSTALLED_APPS = (
        ...
        'admin_argon.apps.AdminArgonConfig',
        'django.contrib.admin',
    )
```

<br />

> Add `admin_argon` urls in your Django Project `urls.py` file.

```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_argon.urls')),
    ]
```

Here are the available `links`: 

```python

    path('', views.index, name='index'),
    path('billing/', views.billing, name='billing'),
    path('profile/', views.profile, name='profile'),
    path('tables/',  views.tables,  name='tables' ),
    path('rtl/',     views.rtl,     name='rtl'    ),
    path('vr/',      views.vr,      name='vr'     ),
    
```

<br />

> **Collect static** if you are in `production environment`:

```bash
$ python manage.py collectstatic
```

<br />

> **Start the app**

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />

## How to use it for common users

> `Create view functions` for a particular pages and render the html template.

```python
    def dashboard(request):
        return render(request, 'pages/dashboard.html')
```

<br />

> Create `urls.py` file and map the function to the `urls.py` file.

```python
    path('dashboard/', views.dashboard, name="dashboard")
```

<br />

>  Available pages 

- `dashboard.html`
- `billing.html`
- `profile.html`
- `rtl.html`
- `tables.html`
- `virtual-reality.html`

<br />

## Screenshots

> **Django Admin Theme**: `Edit users`

![django-admin-argon-users-min](https://user-images.githubusercontent.com/51070104/201162283-90fb0637-687e-4926-ab12-bf409491dac6.jpg)

<br />

> **Django Admin Theme**: `Dashboard` page

![django-admin-argon-dashboard-min](https://user-images.githubusercontent.com/51070104/201162509-80df6786-e595-4fca-a570-45f6a4438c24.jpg) 

<br />

---
**[Django Admin Argon](https://github.com/app-generator/django-admin-argon-dashboard)** - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
