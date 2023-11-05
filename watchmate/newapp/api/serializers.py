from rest_framework import serializers
from newapp.models import Movie

def name_length(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
        
class MovieSerializer(serializers.ModelSerializer):
    len_name=serializers.SerializerMethodField()

    class Meta:
        model=Movie
        fields="__all__"

    def get_len_name(self,object):
         length=len(object.name)
         return length



# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description=serializers.CharField()
#     active=serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)
    
    # def validate_name(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
        
    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError("title and Description should be different.")
        
        else:
            return data