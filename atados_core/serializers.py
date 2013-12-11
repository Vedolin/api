from atados_core.models import (Nonprofit, Volunteer, Project, Availability, Cause,
  Skill, State, City, Suburb, Address, Work, Role,
  Apply, Recommendation, Job, User)
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    lookup_field = 'slug'
    depth = 1
    fields = ('email', 'slug', 'first_name', 'last_name', 'phone', 'address')

class AvailabilitySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model  = Availability
    fields = ('weekday', 'period')

class CauseSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Cause
    lookup_field = 'id'
    fields = ('id', 'name')

class SkillSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Skill
    lookup_field = 'id'
    fields = ('id', 'name')

class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields = ('id', 'name', 'code')

class CitySerializer(serializers.ModelSerializer):
  state = StateSerializer()

  class Meta:
    model = City
    fields = ('id', 'name', 'state', 'active')

class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Address
    depth = 2
    fields = ('id', 'zipcode', 'addressline', 'addressnumber', 'neighborhood', 'city')

class WorkSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Work
    depth = 1
    fields = ('availabilities', 'weekly_hours', 'can_be_done_remotely')

class RoleSerializer(serializers.HyperlinkedModelSerializer):

  def __init__(self, *args, **kwargs):
    many = kwargs.pop('many', True)
    super(RoleSerializer, self).__init__(*args, **kwargs)

  class Meta:
    model = Role
    fields = ('url', 'name', 'prerequisites', 'vacancies')

class JobSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Job
    depth = 1
    fields = ('start_date', 'end_date')

class ApplySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Apply
    fields = ('volunteer', 'project', 'date')

class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Recommendation
    fields = ('project', 'sort', 'state', 'city')

class NonprofitSerializer(serializers.HyperlinkedModelSerializer):
  user = UserSerializer()
  causes = CauseSerializer()
  slug = serializers.Field(source='user.slug')
  role = serializers.Field(source='get_type')
  image_url = serializers.CharField(source='get_image_url', required=False)
  cover_url = serializers.CharField(source='get_cover_url')

  class Meta:
    model = Nonprofit
    lookup_field = 'slug'
    depth = 1
    fields = ('url', 'user', 'slug', 'image_url', 'cover_url', 'name', 'causes', 'details', 'description', 
              'website', 'facebook_page', 'google_page', 'twitter_handle', 'role')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
  causes = CauseSerializer()
  nonprofit = NonprofitSerializer()
  work = WorkSerializer(required=False)
  job = JobSerializer(required=False)
  address = AddressSerializer()
  image_url = serializers.CharField(source='get_image_url', required=False)
  volunteers = serializers.IntegerField(source='get_volunteers', required=True)

  class Meta:
    model = Project
    lookup_field = 'slug'
    depth = 1
    fields = ('nonprofit', 'causes', 'name', 'slug', 'details', 'description', 'facebook_event',
              'responsible', 'address', 'phone', 'email', 'published', 'closed', 'deleted',
              'job', 'work', 'image_url', 'volunteers', 'skills', 'roles')

class VolunteerSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  causes = serializers.HyperlinkedRelatedField(many=True, view_name='cause-detail', lookup_field='id')
  skills  = serializers.HyperlinkedRelatedField(many=True, view_name='skill-detail', lookup_field='id')
  slug = serializers.Field(source='user.slug')
  role = serializers.Field(source='get_type')
  image_url = serializers.CharField(source='get_image_url', required=False)

  class Meta:
    model = Volunteer
    lookup_field = 'slug'
    fields = ('user', 'slug', 'image_url', 'causes', 'skills', 'role')
