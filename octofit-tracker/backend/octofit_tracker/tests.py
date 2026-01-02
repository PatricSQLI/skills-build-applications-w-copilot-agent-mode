from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="test@example.com", team=team)
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.team.name, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name="User1", email="user1@example.com")
        activity = Activity.objects.create(user=user, activity_type="Run", duration_minutes=30, date="2024-01-01")
        self.assertEqual(activity.activity_type, "Run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Cardio")
        self.assertEqual(workout.name, "Cardio")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team B")
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
