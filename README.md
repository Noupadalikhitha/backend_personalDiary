# Personal Diary - Backend

A Django REST Framework backend for the Personal Diary project, providing API endpoints for user authentication and diary entry management.

## Features

- User authentication and authorization
- RESTful API endpoints
- CSRF protection
- CORS support
- Session-based authentication
- PostgreSQL database support

## Tech Stack

- Python 3.8+
- Django 4.2
- Django REST Framework
- PostgreSQL
- Gunicorn (for production)
- Nginx (for production)

## Prerequisites

- Python 3.8 or higher
- PostgreSQL
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Noupadalikhitha/backend_personalDiary.git
cd backend_personalDiary
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=diary
DB_USER=diary
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
CORS_ALLOWED_ORIGINS=http://localhost:5173
CSRF_TRUSTED_ORIGINS=http://localhost:5173
```

5. Set up the database:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication
- POST `/api/login/` - User login
- POST `/api/signup/` - User registration
- POST `/api/logout/` - User logout

### User Profile
- GET `/api/profile/` - Get user profile
- PUT `/api/profile/` - Update user profile

### Diary Entries
- GET `/api/entries/` - List all entries
- POST `/api/entries/` - Create new entry
- GET `/api/entries/<id>/` - Get specific entry
- PUT `/api/entries/<id>/` - Update entry
- DELETE `/api/entries/<id>/` - Delete entry

## Project Structure

```
backend/
├── backend/             # Project settings
├── diary/              # Main application
│   ├── migrations/     # Database migrations
│   ├── models.py       # Database models
│   ├── serializers.py  # API serializers
│   ├── urls.py         # URL routing
│   └── views.py        # View functions
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Deployment

For production deployment:

1. Set up PostgreSQL database
2. Configure environment variables
3. Install Gunicorn and Nginx
4. Collect static files:
```bash
python manage.py collectstatic
```
5. Run with Gunicorn:
```bash
gunicorn backend.wsgi:application
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 