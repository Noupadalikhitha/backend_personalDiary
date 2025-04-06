import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from diary.models import DiaryEntry, User
from django.db import connection

def check_database():
    print("\n=== Database Status ===")
    
    # Check Users
    users = User.objects.all()
    print(f"\nTotal Users: {users.count()}")
    for user in users:
        print(f"- Username: {user.username}")
    
    # Check Diary Entries
    entries = DiaryEntry.objects.all()
    print(f"\nTotal Diary Entries: {entries.count()}")
    for entry in entries:
        print(f"\nEntry ID: {entry.id}")
        print(f"Title: {entry.title}")
        print(f"By: {entry.user.username}")
        print(f"Created: {entry.created_at}")
        print("-" * 30)

if __name__ == "__main__":
    check_database() 