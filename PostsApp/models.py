from django.db import models
from ProfileApp.models import Profile
from django.urls import reverse


class Post(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='postImages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.profile.user.first_name}'s post"

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return f"Comment by {self.profile.user.first_name} on post {self.post.id}"


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='user_likes')

    class Meta:
        unique_together = ('post', 'profile')

    # def __str__(self):
    #     return f"Like by {self.profile.user.first_name} on post {self.post.id}"
