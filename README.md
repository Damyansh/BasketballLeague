🏀 BasketballLeague – Django Web Application


📌 Project Description
BasketballLeague is a Django-based web application for managing basketball teams, players, games, statistics, and awards.
The system allows:

•	Creating and managing Teams

•	Managing Players and assigning them to Teams

•	Recording Games between Teams

•	Tracking Player statistics per Game

•	Assigning Awards to Players

•	Filtering, sorting, and paginating data in the frontend

•	Performing full CRUD operations with confirmation pages

The project demonstrates Django concepts including relational modeling, filtering with GET parameters, pagination, and environment-based configuration.
________________________________________
⚙️ Technologies Used

•	Python 3.12

•	Django 6.0.2

•	PostgreSQL (production configuration)

•	SQLite (automatic fallback for local/testing)

•	Bootstrap 5

•	Pillow (image handling)

•	python-dotenv (environment variable management)
________________________________________
📦 Requirements

asgiref==3.11.1

Django==6.0.2

pillow==12.1.0

psycopg2-binary==2.9.11

python-dotenv==1.2.1

sqlparse==0.5.5

tzdata==2025.3
________________________________________
🚀 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/Damyansh/BasketballLeague.git
cd BasketballLeague
Or download ZIP from GitHub and extract it.
________________________________________
2️⃣ Create virtual environment (recommended)
Windows:
python -m venv venv
venv\Scripts\activate
Mac/Linux:
python -m venv venv
source venv/bin/activate
________________________________________
3️⃣ Install dependencies
pip install -r requirements.txt
________________________________________
4️⃣ Apply migrations
python manage.py migrate
________________________________________
5️⃣ Run the development server
python manage.py runserver
Open in browser:
http://127.0.0.1:8000/
________________________________________
6️⃣ Create Superuser
python manage.py createsuperuser
________________________________________
🌍 Database Configuration
The project supports:

•	SQLite (default – no setup required)

•	PostgreSQL (optional via environment variables)

If no environment variables are provided, the application automatically uses SQLite, ensuring it runs immediately after installation without modifications.
________________________________________
🔑 Environment Variables
The project uses a .env file located in the root directory
(same level as manage.py).
The .env file is excluded from version control for security reasons.
🔒 Hidden Variables
The following sensitive variables are stored in .env:

•	SECRET_KEY

•	DB_NAME

•	DB_USER

•	DB_PASS

•	DB_PORT

•	DB_HOST

📄 Example .env Structure

SECRET_KEY=django-insecure-ef_*a=semng1imhq_-oos4psfn079g(_)((eiu0ealm8#dabpf

DB_NAME=basketball_league

DB_USER=postgres

DB_PASS=damyansh12

DB_PORT=5432

DB_HOST=127.0.0.1

⚠️ The real credentials are not included in the repository for security reasons.
________________________________________
📊 Database Relationships

•	One Team → Many Players (ForeignKey)

•	One Award(title + year) → Many Players (ManyToMany)

•	One Game → Two Teams (home & away)

•	One Game → Many Players (ManyToMany through GamePlayerStats)

•	Intermediate model: GamePlayerStats

•	Data integrity enforced through model validation and form validation

________________________________________
🛠 Features
🔹 Core Functionality

•	Full CRUD operations (Create, Read, Update, Delete)

•	Delete confirmation pages for safe data removal

•	PostgreSQL production-ready configuration

•	SQLite automatic fallback for easy setup

🔹 Filtering & Sorting

•	Filter players by team

•	Sort players by:

o	Name

o	Team

o	Points per game

o	Rebounds per game

o	Assists per game

•	Filter games by team and date

🔹 Pagination

•	Paginated Teams list on the home page

•	Paginated Players list with preserved filtering & sorting

•	Dynamic page navigation (First / Previous / Next / Last)

🔹 UI & Forms

•	Bootstrap 5 styling

•	Image upload support (team logos)

•	Custom form labels, widgets and validation messages

•	Custom template tags

________________________________________
📈 Scalability & Architecture Highlights

This project demonstrates:

•	QuerySet filtering with GET parameters

•	Safe pagination applied after filtering and sorting

•	Separation of concerns (apps: teams, players, games, common)

•	Environment-based database configuration

•	Through models for complex ManyToMany relationships

•	Proper confirmation before destructive operations

________________________________________
✅ Project Status

The project is fully:

•	Downloadable

•	Installable

•	Runnable without modifications

•	Database-ready (SQLite by default)

Designed for academic demonstration of Django best practices.

## 📸 Screenshots

Home Page  
![Home Page](https://github.com/user-attachments/assets/7882af8d-00a4-4cd3-81b0-0a2dd531cc96)



Players List  
![Players List](https://github.com/user-attachments/assets/9a1dde07-904f-4932-a801-57b1c0980aca)


Game Details  
![Game Details](https://github.com/user-attachments/assets/8e61164b-9b37-4656-ab04-b980fe258099)

