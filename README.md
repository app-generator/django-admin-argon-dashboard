# [Django Admin Argon](https://appseed.us/product/argon-dashboard/django/)

Modern template for **Django** that covers `Admin Section`, all authentication pages (registration included) crafted on top of **Argon Dashboard**, an open-source `Bootstrap 5` design from `Creative-Tim`.

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br>

**Links & Resources**

- [Django Admin Argon](https://appseed.us/product/argon-dashboard/django/) - `Product page`
  - `Features`: Fully-configured, `CI/CD` via Render
- UI Kit: [Material Dashboard BS5](https://www.creative-tim.com/product/material-dashboard?AFFILIATE=128200) `v3.0.5` by Creative-Tim

<br />

![image](https://user-images.githubusercontent.com/51070104/211161884-56ef77d2-1e5a-4269-a148-7ac4a5482e0c.png)

![Argon Dashboard 2](https://user-images.githubusercontent.com/51070104/183684596-4b29a886-f13d-4da5-98d3-12b5b90df47f.png)

<br />

## Why `Django Argon Design`

- Modern [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Design
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

## [PRO Version](https://appseed.us/product/argon-dashboard2-pro/django/)   

This design is a pixel-perfect [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Dashboard with a fresh, new design. Argon is a completly new product built on our newest re-built from scratch framework structure that is meant to make our products more intuitive, more adaptive and, needless to say, so much easier to customize. 

> Features: 

- `Up-to-date Dependencies`
- `Design`: [Django Theme Argon2](https://github.com/app-generator/django-argon-dashboard2-pro) - `PRO Version`
- `Sections` covered by the design:
  - **Admin section** (reserved for superusers)
  - **Authentication**: `Django.contrib.AUTH`, Registration
  - **All Pages** available in for ordinary users 
- `Docker`, `Deployment`:
  - `CI/CD` flow via `Render`

<br />

![Argon Dashboard 2 PRO - Automotive (Premium Bootstrap 5 Design).](https://user-images.githubusercontent.com/51070104/211158013-fea76b79-bb54-4066-a617-5ec3b4b6ec42.jpg)

<br />

---
**[Django Admin Argon](https://appseed.us/product/argon-dashboard/django/)** - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
