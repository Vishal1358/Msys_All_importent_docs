from rest_framework import serializers
from .models import Person, Color
# from .models import Person



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()




# class ColorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Color
#         fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    # color = ColorSerializer()
    # color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = "__all__"
        # fields = ["id","name","age"]
        # depth = 1

    def get_color_info(self,obj):
        color_obj = Color.objects.get(id = obj.color.id)

        return {'color_name' : color_obj.color_name}

    def validate_age(self, data):
        print(data)
        return data

    # def validate(self, data):
    #     special_character = "!@#$%^&*()_+=,./<>?;':'[]\|"
    #     if any(c in special_character for c in data['name']):
    #         raise serializers.ValidationError('name cannot contain special chars')
        
        # if data['age'] < 18:
        #     raise serializers.ValidationError("age should be greather than 18")
        # return data