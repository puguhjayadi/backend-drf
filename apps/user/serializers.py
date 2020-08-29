from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	
	class Meta:
		model = User
		fields = (
			'url',
			'id',
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
			'date_joined',
			)

	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user


	def update(self, instance, validated_data):
		fields=instance._meta.fields
		exclude=[]
		for field in fields:
			field=field.name.split('.')[-1]
			if field in exclude:
				continue
			exec("instance.%s = validated_data.get(field, instance.%s)"%(field,field))
		if validated_data.get('password') :
			instance.set_password(validated_data.get('password', instance.password) )
		instance.save()
		return instance
