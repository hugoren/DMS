#-*-coding:utf-8-*-


from dtr.models import  Book
from rest_framework import  serializers
from  django.contrib.auth.models import  User

class BookSerializer(serializers.Serializer):

    class Meta:
        model = Book
        field = ('name','title','author')
    # name = serializers.CharField(max_length=100)
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)

    def restore_object(self,attrs,instance=None):
        if instance:
            instance.title = attrs['title']
            instance.name = attrs['name']
            instance.author = attrs['author']

            return instance
        return Book(**attrs)

#
# class UserSerializer(serializers.ModelSerializer):
#     book = serializers.PrimaryKeyRelatedField(many=True)
#     class Meta:
#         model = User
#         field = ('id','username','book')