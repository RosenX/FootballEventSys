# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('event_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start_time', self.gf('django.db.models.fields.DateField')()),
            ('end_time', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('event', ['Event'])

        # Adding model 'Schedule'
        db.create_table('event_schedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Event'])),
            ('round_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('event', ['Schedule'])

        # Adding model 'SingleMatch'
        db.create_table('event_singlematch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teamA', self.gf('django.db.models.fields.related.ForeignKey')(related_name='A_team', to=orm['team.Team'])),
            ('teamB', self.gf('django.db.models.fields.related.ForeignKey')(related_name='B_team', to=orm['team.Team'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('round_belong', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Schedule'])),
        ))
        db.send_create_signal('event', ['SingleMatch'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('event_event')

        # Deleting model 'Schedule'
        db.delete_table('event_schedule')

        # Deleting model 'SingleMatch'
        db.delete_table('event_singlematch')


    models = {
        'event.event': {
            'Meta': {'object_name': 'Event'},
            'end_time': ('django.db.models.fields.DateField', [], {}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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