from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from donggram.users import models as user_models

# Create your models here.
@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE, related_name='images')

    def __str__(self): # 어드민 화면에서 해당 제목이 어떻게 보이는지 형태를 정의한다
        return '{} - {}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at'] # 가장 최근 순으로 정렬하기 위한 설정

@python_2_unicode_compatible
class Comment(TimeStampedModel):

    """ Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE, related_name='comments')

    def __str__(self): # 어드민 화면에서 해당 제목이 어떻게 보이는지 형태를 정의한다
        return self.message

@python_2_unicode_compatible
class Like(TimeStampedModel):

    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE, related_name='likes')

    def __str__(self): # 어드민 화면에서 해당 제목이 어떻게 보이는지 형태를 정의한다
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)