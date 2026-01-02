from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):

        # Clear existing data in correct order (children before parents), handle missing collections gracefully
        for model in [Activity, Leaderboard, Workout, User, Team]:
            try:
                model.objects.all().delete()
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Warning deleting {model.__name__}: {e}"))

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users (do not use bulk_create for related objects)
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True)

        # Create Activities
        Activity.objects.create(user=spiderman, activity_type='Running', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=ironman, activity_type='Cycling', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=wonderwoman, activity_type='Swimming', duration_minutes=60, date=timezone.now().date())
        Activity.objects.create(user=batman, activity_type='Yoga', duration_minutes=40, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150, rank=1)
        Leaderboard.objects.create(team=dc, total_points=120, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
