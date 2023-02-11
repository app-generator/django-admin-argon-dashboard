# [Django Admin Argon](https://appseed.us/product/argon-dashboard/django/)

Modern template for **Django** that covers `Admin Section`, all authentication pages (registration included) crafted on top of **[Argon Dashboard](https://appseed.us/product/argon-dashboard/django/)**, an open-source `Bootstrap 5` design from [Creative-Tim](https://www.creative-tim.com/?AFFILIATE=128200).

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br>

**Links & Resources**

- [Django Admin Argon](https://appseed.us/product/argon-dashboard/django/) - `Product` that uses the library
  - `Features`: Fully-configured, `CI/CD` via Render
- UI Kit: [Argon Dashboard BS5](https://www.creative-tim.com/product/argon-dashboard?AFFILIATE=128200) `v2.0.4` by Creative-Tim
- **Sections Covered**: 
  - `Admin Section`, reserved for `superusers`
  - `All pages` managed by `Django.contrib.AUTH`
  - `Registration` page
  - `Misc pages`: colors, icons, typography, blank-page 
  
<br />

![Argon Dashboard 2 - Free Starter.](https://user-images.githubusercontent.com/51070104/215804889-94eba681-8262-41a3-8e57-7d5b12dcc209.png)

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

## How to Customize 

When a template file is loaded in the controller, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found. 
The  theme used to style this starter provides the following files: 

```bash
# This exists in ENV: LIB/admin_argon
< UI_LIBRARY_ROOT >                      
   |
   |-- templates/                     # Root Templates Folder 
   |    |          
   |    |-- accounts/       
   |    |    |-- sign-in.html         # Sign IN Page
   |    |    |-- sign-up.html         # Sign UP Page
   |    |
   |    |-- includes/       
   |    |    |-- footer.html          # Footer component
   |    |    |-- sidebar.html         # Sidebar component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/       
   |    |    |-- base.html            # Masterpage
   |    |    |-- base-fullscreen.html # Masterpage for Auth Pages
   |    |
   |    |-- pages/       
   |         |-- dashboard.html       # Dashboard page
   |         |-- profile.html         # Settings  Page
   |         |-- *.html               # All other pages
   |    
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path. 

For instance, if we want to customize the `footer.html` these are the steps:

- `Step 1`: create the `templates` DIRECTORY inside your app 
- `Step 2`: configure the project to use this new template directory
  - Edit `settings.py` TEMPLATES section 
- `Step 3`: copy the `footer.html` from the original location (inside your ENV) and save it to the `YOUR_APP/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_argon/includes/footer.html`
  - Destination PATH: `YOUR_APP/templates/includes/footer.html`
- Edit the footer (Destination PATH)    

At this point, the default version of the `footer.html` shipped in the library is ignored by Django.

In a similar way, all other files and components can be customized easily.

<br />

## [PRO Version](https://appseed.us/product/argon-dashboard2-pro/django/)   

This design is a pixel-perfect [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Dashboard with a fresh, new design. Argon is a completly new product built on our newest re-built from scratch framework structure that is meant to make our products more intuitive, more adaptive and, needless to say, so much easier to customize. 

> Features: 

- `Up-to-date Dependencies`
- `Design`: Django Theme Argon2 - `PRO Version`
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
