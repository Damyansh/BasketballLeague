🏀 BasketballLeague – Django Advanced Web Application

📌 Project Description BasketballLeague is a full-stack Django application for managing basketball teams, players, games, awards, and player statistics.

This advanced version extends the original project with:

Authentication & Authorization (Groups, Permissions, Extended User Model)
Custom Middleware & Session Management
REST API (Django REST Framework)
Asynchronous Processing (Celery + Redis)
Cloud Deployment (Azure App Service + PostgreSQL + Redis + Cloudinary)
Automated Testing
Clean architecture using Class-Based Views and modular design

The project is fully functional both locally and in production and follows Django best practices.
________________________________________
🌍 Live Demo  
https://basketball2026-b2hxfvaaawc3ckep.spaincentral-01.azurewebsites.net

The application is deployed on Azure App Service and fully functional.
________________________________________
🔐 Access & Testing the Application

The application can be tested directly via the Live Demo.

👤 Demo Accounts

Admin user

Username: admin
Password: admin
Permissions:
is_staff = True
Member of Admin group
Full CRUD access to all resources

Fan user

Username: testfan
Password: 12test34
Permissions:
Member of Fan group
Read-only access
📝 Register New User

New users can register from:

/accounts/register/
Automatically assigned to Fan group
Have read-only permissions by default
________________________________________
⚙️ Technologies Used
Python 3.11+
Django 5.2.10
Django REST Framework
PostgreSQL (Azure production)
SQLite (local fallback)
Redis (Azure Cache for Redis)
Celery (background tasks)
Cloudinary (media storage)
Gunicorn (production WSGI server)
WhiteNoise (static files)
Bootstrap 5
python-dotenv
________________________________________
📦 Requirements
amqp==5.3.1
asgiref==3.11.1
billiard==4.2.4
celery==5.6.3
certifi==2026.2.25
charset-normalizer==3.4.7
click==8.3.1
click-didyoumean==0.3.1
click-plugins==1.1.1.2
click-repl==0.3.0
cloudinary==1.44.1
colorama==0.4.6
Django==5.2.10
django-cloudinary-storage==0.3.0
djangorestframework==3.17.1
gunicorn==25.3.0
idna==3.11
kombu==5.6.2
packaging==26.0
pillow==12.1.0
prompt_toolkit==3.0.52
psycopg2-binary==2.9.11
python-dateutil==2.9.0.post0
python-dotenv==1.2.1
redis==7.4.0
requests==2.33.1
six==1.17.0
sqlparse==0.5.5
tzdata==2025.3
tzlocal==5.3.1
urllib3==2.6.3
vine==5.1.0
wcwidth==0.6.0
whitenoise==6.12.0
________________________________________

📦 Installation & Local Setup
1️⃣ Clone repository
git clone https://github.com/Damyansh/BasketballLeague.git
cd BasketballLeague
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set up settings.py Database with this credentials:

SECRET_KEY=django-insecure-ef_*a=semng1imhq_-oos4psfn079g(_)((eiu0ealm8#dabpf

DB_NAME=basketball_league
DB_USER=postgres
DB_PASS=damyansh12
DB_PORT=5432
DB_HOST=127.0.0.1
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1,http://localhost
CELERY_BROKER_URL=redis://127.0.0.1:6379/0
CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/0
CLOUDINARY_CLOUD_NAME=dl2ui4ztv
CLOUDINARY_API_KEY=441948988886259
CLOUDINARY_API_SECRET=kDIXzlaUfH971cNTKH3b4IQxjxU
5️⃣ Apply migrations
 python manage.py makemigrations python manage.py migrate
6️⃣ Run the development server python manage.py runserver Open in browser: http://127.0.0.1:8000/
7️⃣ Create Superuser 
python manage.py createsuperuser
________________________________________
🌍 Database Configuration The project supports:
• SQLite (default – no setup required)
• PostgreSQL (optional via environment variables)
If no environment variables are provided, the application automatically uses SQLite, ensuring it runs immediately after installation without modifications.

________________________________________
🔄 Running Locally (Async Mode)

Local development uses full asynchronous processing.

Terminal 1 – Redis
redis-server
Terminal 2 – Celery worker
celery -A BasketballLeague worker --loglevel=info --pool=solo
Terminal 3 – Django server
python manage.py runserver

Tasks like:

notify_new_player.delay(...)
notify_new_game.delay(...)

run asynchronously.
________________________________________
🔐 Authentication & Authorization
✔ Extended User Model

A Profile model extends Django’s built-in User.

✔ Groups & Permissions
Group	Permissions
Admin	Full CRUD
Fan	Read-only
✔ Registration Behavior
New users are automatically assigned to Fan group
Only users who are:
is_staff=True
AND part of Admin group

can create, edit, or delete data.
________________________________________
🧠 Custom Middleware & Sessions
VisitCounterMiddleware → counts user visits
LastVisitedMiddleware → tracks last visited page
BlockAnonymousPostMiddleware → blocks unauthorized POST requests
________________________________________
🌐 REST API (Django REST Framework)
Endpoints:
/api/teams/
/api/players/
/api/games/
Features:
ModelViewSet implementation
Serializers for all models
Permission class: IsAdminOrReadOnly
Full CRUD via API (admin only)
________________________________________
⚡ Asynchronous Processing (Celery + Redis)
Local Development (Async Mode)
redis-server
celery -A BasketballLeague worker --loglevel=info --pool=solo
python manage.py runserver

Tasks run asynchronously using .delay().
________________________________________
☁️ Azure Deployment (Sync Mode)

Azure App Service supports only one main process per container, so Celery workers cannot run alongside Gunicorn.

✔ Implemented solution:
if settings.DEBUG:
    task.delay()
else:
    task()
✔ Result:
Local → async (Celery + Redis)
Production → sync (stable execution)
Redis remains configured
________________________________________
☁️ Azure Deployment Details
Startup Command
gunicorn BasketballLeague.wsgi
Environment Variables (Azure)
Configured in Azure App Service (not included in repository for security reasons):

- DEBUG=False
- SECRET_KEY
- DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT
- CLOUDINARY_*
- CELERY_BROKER_URL
- CELERY_RESULT_BACKEND
- ALLOWED_HOSTS
- CSRF_TRUSTED_ORIGINS
Redis URL format:
rediss://:PASSWORD@HOST:6380/0?ssl_cert_reqs=none
________________________________________
🗄 Database Design
Relationships:
Team → Players (One-to-Many)
Game → Teams (Two Foreign Keys)
Game ↔ Players (Many-to-Many via GamePlayerStats)
Awards ↔ Players (Many-to-Many)
User ↔ Profile (One-to-One)
________________________________________
🛠 Features Overview
Full CRUD (Teams, Players, Games)
Filtering & Sorting
Pagination
Cloudinary image uploads
Default images
Bootstrap UI
Confirmation pages
Custom template tags
Responsive design
Navigation across all pages
________________________________________
🧪 Testing

Run:

python manage.py test

Includes:

Model tests
View tests
Permission tests
Authentication checks
15+ test cases
________________________________________
🔐 Security
Environment variables for secrets
CSRF protection
Middleware for request validation
No hardcoded credentials
Input validation in forms and models
________________________________________
📈 Architecture & Advanced Features

This project demonstrates a scalable and production-ready Django architecture, including:

Core Architecture

Separation of concerns using multiple apps:
teams, players, games, accounts, common
Use of Class-Based Views (CBVs) for modular and reusable logic 
Clean URL structure with namespacing
Environment-based configuration (development vs production)

Database Design

Complex relationships:
One-to-Many (Team → Players)
Many-to-Many (Players ↔ Awards)
Many-to-Many through model (GamePlayerStats)
PostgreSQL in production, SQLite fallback locally
Data validation at both model and form level

Authentication & Authorization

Extended User model via Profile (One-to-One)
Role-based access control using Groups:
Admin (full access)
Fan (read-only)
Permission-based view protection

Middleware & Sessions

Custom middleware for:
Visit tracking (session-based)
Last visited page tracking
Blocking unauthorized POST requests
Demonstrates session management and request lifecycle control

REST API Integration

Django REST Framework with:
ModelViewSet architecture
Serializers for all major models
Custom permission class (IsAdminOrReadOnly)
Fully functional REST endpoints for external integration

Asynchronous Processing

Celery + Redis integration for background tasks
Environment-based execution:
Async in development
Sync fallback in production (Azure limitation)
Demonstrates real-world distributed task handling

Cloud & Deployment

Deployed on Azure App Service
Azure PostgreSQL database
Azure Redis Cache (configured)
Cloudinary for media storage
Gunicorn as WSGI server

Frontend & UX

Bootstrap-based responsive design
Pagination, filtering, sorting
Custom template tags
Reusable templates and components

Testing & Reliability

15+ unit tests covering:
Models
Views
Permissions
Ensures application stability and correctness

________________________________________
✅ Project Status

✔ Fully functional locally
✔ Fully deployed on Azure
✔ Covers all Django Advanced requirements
✔ Ready for evaluation

Designed for academic demonstration of Django best practices.
________________________________________

## 📸 Screenshots

Home Page  
![Home Page](https://github.com/user-attachments/assets/7882af8d-00a4-4cd3-81b0-0a2dd531cc96)
<img width="1897" height="906" alt="image" src="https://github.com/user-attachments/assets/dd5e73b1-7c35-4b55-b2f1-fb71357ddbf5" />



Players List  
![Players List](https://github.com/user-attachments/assets/9a1dde07-904f-4932-a801-57b1c0980aca)
<img width="1897" height="932" alt="image" src="https://github.com/user-attachments/assets/92084c39-1b79-4283-b101-fdd6055945af" />


Game Details  
![Game Details](https://github.com/user-attachments/assets/8e61164b-9b37-4656-ab04-b980fe258099)
<img width="1882" height="916" alt="image" src="https://github.com/user-attachments/assets/aa4b5c7e-856a-4857-99db-5b7425ac338e" />

