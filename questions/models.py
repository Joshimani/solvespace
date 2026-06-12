from django.db import models
from users.models import User
from django.utils.text import slugify

# Create your models here.
TYPES_CHOICE= (
    ("math", "Math"),
    ("history", "History"),
    ("science", "Science"),
    ("tech", "Technology"),
    ("coding", "Coding"),
    ("reality", "Reality"),
    ("curiosity", "Curiosity"),

)

STATUS_CHECK= (
    ('active', 'Active'),
    ('closed', 'Closed'),

)

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    slug = models.SlugField(max_length=250)
    topic = models.CharField(max_length=300)
    the_question = models.TextField()
    image = models.ImageField(upload_to='questions/media/', null=True, blank=True)
    question_type = models.CharField(max_length=50, choices=TYPES_CHOICE, default='reality')
    status = models.CharField(max_length=50, choices=STATUS_CHECK, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.ManyToManyField(User, blank=True, related_name='upvoted_questions')
    
    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        super().save(*args, **kwargs)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, blank=True, related_name='upvoted_answers')

    def __str__(self):
        return self.user.username






