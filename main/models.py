from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    def update_rating(self):
        # в этой части я не нашёл решения, поэтому просто скопирывал код. Очень сложно здесью
        sum_rating_author = self.post_set.all().aggregate(Sum('rating_post'))['rating_post__sum'] * 3
        sum_rating_comment = self.author_user.comment_set.all().aggregate(Sum('rating_comment'))['rating_comment__sum']
        sum_rating = self.post_set.all().aggregate(Sum('comment__rating_comment'))['comment__rating_comment__sum']
        
        self.rating_author = sum_rating_author + sum_rating_comment + sum_rating
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Post(models.Model):
    choice = [
        ('article', 'статья'),
        ('news', 'новость'),
    ]

    article_or_news = models.CharField(max_length=10, choices=choice)
    _date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    rating = models.IntegerField()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.text[:124]}..."

class PostCategory(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, default='Category.objects.get(pk=1)')

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    commend_text = models.CharField(max_length=2000)
    _date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


# команды для консоли
# >>> from django.contrib.auth.models import User
# >>> user_n1 = User.objects.create(username='user_n1')
# >>> user_n2 = User.objects.create(username='user_n2')

# >>> from main.models import Author
# >>> Author_n1 = Author.objects.create(user=user_n1, rating=0)
# >>> Author_n2 = Author.objects.create(user=user_n2, rating=100)

# >>> from main.models import Category
# >>> Category_n1 = Category.objects.create(name='tech-article')
# >>> Category_n2 = Category.objects.create(name='furniture')
# >>> Category_n3 = Category.objects.create(name='pets')
# >>> Category_n4 = Category.objects.create(name='architecture')

# >>> from main.models import Post
# >>> Post_n1 = Post.objects.create(article_or_news='article', author=Author_n1, category=Category_n1, headline='smth about tech', text='laptop', rating='1')
# >>> Post_n2 = Post.objects.create(article_or_news='news', author=Author_n2, category=Category_n3, headline='smth about furniture', text='a table', rating='6')
# >>> Post_n3 = Post.objects.create(article_or_news='article', author=Author_n2, category=Category_n2, headline='smth about pets', text='dogs', rating='99')

# Post.objects.create_post(article_or_news='article')
# Post.objects.create_post(article_or_news='article')
# Post.Category.objects.create_post_category()

# PC_1 = PostCategory.objects.create(post=Post_n1, category=Category_n1)
# PC_2 = PostCategory.objects.create(post=Post_n2, category=Category_n2)
# PC_2 = PostCategory.objects.create(post=Post_n3, category=Category_n3) #я знаю что должно быть отношение one-to-many но когда я это написал уже было поздно

# Comment_n1 = Comment.create(post=Post_n1, user=user_n1, commend_text='test', rating=4)
# Comment_n2 = Comment.create(post=Post_n1, user=user_n2, commend_text='tes2t', rating=8)
# Comment_n3 = Comment.create(post=Post_n2, user=user_n1, commend_text='test3', rating=1)

# Comment_n1.like()
# Comment_n2.dislike()
# Comment_n3.like()
# Post_n1.like()

# user_n1.update_rating()
# user_n2.update_rating()

# User.objects.all(sort_order=ascending, by=rating)







# команда на случай если пользыватель вышел из терминала и требуются все переменные
# from django.contrib.auth.models import User
# from main.models import Category, Author, Post, PostCategory, Comment
# user_n1 = User.objects.get(pk=1)
# user_n2 = User.objects.get(pk=2)

# Author_n1 = Author.objects.get(pk=1)
# Author_n2 = Author.objects.get(pk=2)

# Post_n1 = Post.objects.get(pk=1)
# Post_n2 = Post.objects.get(pk=2)
# Post_n3 = Post.objects.get(pk=3)

# Category_n1 = Category.objects.get(pk=1)
# Category_n2 = Category.objects.get(pk=2)
# Category_n3 = Category.objects.get(pk=3)
# Category_n4 = Category.objects.get(pk=4)

# ...