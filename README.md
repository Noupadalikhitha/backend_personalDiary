# Personal Diary - Backend (Interview Showcase)

A Django REST Framework backend for the Personal Diary project, demonstrating modern web development practices and API design. This project showcases:

- RESTful API design
- Authentication and authorization
- Database modeling
- API documentation
- Security best practices

## Features

- User authentication and authorization
- RESTful API endpoints
- CSRF protection
- CORS support
- Session-based authentication
- SQLite database (for easy setup and demonstration)

## Tech Stack

- Python 3.8+
- Django 4.2
- Django REST Framework
- SQLite (for demonstration purposes)
- Gunicorn (for production)
- Nginx (for production)

## Quick Start (For Interviewers)

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

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## API Documentation

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

## Technical Highlights

1. **Security**:
   - CSRF protection
   - Session-based authentication
   - Secure password handling
   - CORS configuration

2. **API Design**:
   - RESTful endpoints
   - Proper HTTP methods
   - Status code handling
   - Error responses

3. **Database**:
   - SQLite for easy setup
   - Django ORM usage
   - Model relationships
   - Migrations

4. **Code Organization**:
   - Separation of concerns
   - DRY principles
   - Clean architecture
   - Documentation

## Future Improvements

1. **Database**:
   - Migration to PostgreSQL for production
   - Database optimization
   - Caching implementation

2. **Features**:
   - Email verification
   - Password reset
   - File uploads
   - Rich text editing

3. **Performance**:
   - API caching
   - Query optimization
   - Load balancing

4. **Security**:
   - Rate limiting
   - API key authentication
   - OAuth2 integration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 