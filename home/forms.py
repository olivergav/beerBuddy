from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
	class Meta:
		model = Room
		# fields = ('host', 'topic', 'name', 'description', 'updated', 'created') # participants
		# error_messages = {
		#
		# }
		fields = '__all__'
