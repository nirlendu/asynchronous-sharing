#-*- coding: utf-8 -*-

from __future__ import unicode_literals

#from django.db import models as models_sql
#from express.models import Expression

from neomodel import (StructuredNode, StringProperty, IntegerProperty,
	RelationshipTo, RelationshipFrom)

class Person(StructuredNode):
	person_id = StringProperty(unique_index=True, required=True)
	person_name = StringProperty(required=True)
	person_age = IntegerProperty()
	person_gender = StringProperty() 
	person_follow = RelationshipFrom('Person', 'FOLLOWS')

class Topic(StructuredNode):
	# name = StringProperty(unique_index=True)
	# age = IntegerProperty(index=True, default=0)
	name = StringProperty()
	followed_topic = RelationshipFrom(Person, 'FOLLOWS')
	child_topic = RelationshipTo('Topic', 'CHILD_TOPIC')
	related_topic = RelationshipTo('Topic', 'RELATED')
	related_posts = RelationshipFrom('Expression', 'IN_TOPIC')

class RootTopic(StructuredNode):
	#code = StringProperty(unique_index=True, required=True)
	Root = StringProperty() 
	follow = RelationshipTo(Topic, 'CHILD_TOPIC')