from django.db import models

from django.db import models

class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(null=False)
    year = models.IntegerField()
    


    def __str__(self):
        return self.title  

class People(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    birth = models.IntegerField(null=True)
    


    def __str__(self):
        return self.name  


class Stars(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE,null=False)
    person_id = models.ForeignKey(People, on_delete=models.CASCADE,null=False)
    
    


    def __str__(self):
        return self.person_id  


class Directors(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE,null=False)
    person_id = models.ForeignKey(People, on_delete=models.CASCADE,null=False)
    


    def __str__(self):
        return self.person_id  


class Ratings(models.Model):
    movie_id = models.OneToOneField(Movies,on_delete=models.CASCADE,primary_key=True)
    rating = models.FloatField(null=False)
    votes = models.IntegerField(null=False)



    def __str__(self):
        return self.rating  
