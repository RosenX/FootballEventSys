# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.place'
        db.add_column('event_event', 'place',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.place'
        db.delete_column('event_event', 'place')


    models = {
        'event.event': {
            'Meta': {'object_name': 'Event'},
            'end_time': ('django.db.models.fields.DateField', [], {}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_time': ('django.db.models.fields.DateField', [], {})
        },
        'event.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'round_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'event.singlematch': {
            'Meta': {'object_name': 'SingleMatch'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'round_belong': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Schedule']"}),
            'teamA': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'A_team'", 'to': "orm['team.Team']"}),
            'teamB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'B_team'", 'to': "orm['team.Team']"})
        },
        'team.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['event']