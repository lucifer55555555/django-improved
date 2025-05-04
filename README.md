Bookstore Project
Project Overview
The Bookstore project is a web application designed to manage and showcase a collection of books. Users can browse books, add them to their cart, and proceed to checkout. The project is built using Django, a high-level Python web framework, and includes features such as user authentication, cart management, and an admin interface for managing books.

Setup & Run Instructions
Prerequisites
Python 3.12 or higher
Docker (optional, for containerized setup)
pip (Python package manager)
Steps to Run Locally
Clone the repository:
git clone <repository-url>
cd bookstore-main
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Apply migrations:
python manage.py migrate
Create a superuser:
python manage.py createsuperuser
Run the development server:
python manage.py runserver
Open the application in your browser at http://127.0.0.1:8000/.
Docker Setup
Build the Docker image:
docker-compose build
Start the containers:
docker-compose up
Access the application at http://127.0.0.1:8000/.
Tech Stack Used
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: SQLite (default, can be replaced with PostgreSQL or MySQL)
Containerization: Docker
CI/CD: Jenkins
Docker and Jenkins Usage Notes
Docker: The docker-compose.yml file is configured to build and run the application in a containerized environment. Ensure Docker is installed and running on your system.
Jenkins: The Jenkinsfile contains the pipeline configuration for automating builds, tests, and deployments. Integrate this file with your Jenkins server to enable CI/CD.
License
This project is licensed under the MIT License. See the LICENSE file for details.
