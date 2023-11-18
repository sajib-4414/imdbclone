# myapp/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from decimal import Decimal
import random
from movie_app.models import StreamPlatform, Movie, Review

fake = Faker()

class Command(BaseCommand):
    help = 'Seed data into the database'

    def handle(self, *args, **options):
        # Create users
        users = []
        for _ in range(5):
            users.append(User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password()
            ))

        # Create streaming platforms
        platforms = []
        for _ in range(4):
            platforms.append(StreamPlatform.objects.create(
                name=fake.word(),
                about=fake.text(),
                website=fake.url()
            ))

        # Create movies and reviews
        for _ in range(20):
            movie = Movie.objects.create(
                title=fake.sentence(),
                storyline=fake.text(),
                platform=platforms[fake.random_int(0, len(platforms) - 1)],
                avg_rating=Decimal(random.uniform(0, 5)),
                number_rating=fake.random_int(1, 100),
            )

            for _ in range(3):  # Create 3 reviews for each movie
                Review.objects.create(
                    review_user=users[fake.random_int(0, len(users) - 1)],
                    rating=fake.random_int(1, 5),
                    description=fake.text(),
                    movie=movie,
                )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
