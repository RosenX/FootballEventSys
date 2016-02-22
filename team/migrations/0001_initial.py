# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table('team_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal('team', ['Team'])

        # Adding model 'Member'
        db.create_table('team_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Team'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('team', ['Member'])

        # Adding model 'Player'
        db.create_table('team_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['team.Member'], unique=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('team', ['Player'])

        # Adding model 'OtherMember'
        db.create_table('team_othermember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['team.Member'], unique=True)),
            ('title', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('team', ['OtherMember'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table('team_team')

        # Deleting model 'Member'
        db.delete_table('team_member')

        # Deleting model 'Player'
        db.delete_table('team_player')

        # Deleting model 'OtherMember'
        db.delete_table('team_othermember')


    models = {
        'team.member': {
            'Meta': {'object_name': 'Member'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team.Team']"})
        },
        'team.othermember': {
            'Meta': {'object_name': 'OtherMember'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['team.Member']", 'unique': 'True'}),
            'title': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'team.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['team.Member']", 'unique': 'True'})
        },
        'team.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['team']