from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    last_modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
        
    class Meta:
        db_table = 'mp_user'

class UserGroup(models.Model):
    name = models.CharField(max_length=254)
    user = models.ManyToManyField(User)
    last_modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'mp_user_group'
        
class Music(models.Model):
    name = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'mp_music'

class PlayListType(models.Model):
    name = models.CharField(max_length=254)
    last_modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'mp_playlist_type'

class UserPlayList(models.Model):
    name = models.CharField(max_length=254)
    playlist_type = models.ForeignKey(PlayListType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'mp_user_playlist'
        
def fun_raw_sql_query(**kwargs):
    music = kwargs.get('music')
    if music:
        result = Music.objects.raw('SELECT m.id, m.name, u.username, m.last_modify_date, m.created_date FROM mp_user u, mp_music m WHERE u.id = m.user_id AND m.id = %s', [music])
    else:
        result = None
    return result