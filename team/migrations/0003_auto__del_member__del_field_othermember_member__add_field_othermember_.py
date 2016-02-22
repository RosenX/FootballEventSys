# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Member'
        db.delete_table('team_member')

        # Deleting field 'OtherMember.member'
        db.delete_column('team_othermember', 'member_id')

        # Adding field 'OtherMember.name'
        db.add_column('team_othermember', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'OtherMember.team'
        db.add_column('team_othermember', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['team.Team']),
                      keep_default=False)

        # Adding field 'OtherMember.phone'
        db.add_column('team_othermember', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'OtherMember.email'
        db.add_column('team_othermember', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'OtherMember.age'
        db.add_column('team_othermember', 'age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Player.player'
        db.delete_column('team_player', 'player_id')

        # Adding field 'Player.name'
        db.add_column('team_player', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Player.team'
        db.add_column('team_player', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['team.Team']),
                      keep_default=False)

        # Adding field 'Player.phone'
        db.add_column('team_player', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Player.email'
        db.add_column('team_player', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Player.age'
        db.add_column('team_player', 'age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Member'
        db.create_table('team_member', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Team'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('team', ['Member'])

        # Adding field 'OtherMember.member'
        db.add_column('team_othermember', 'member',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['team.Member'], unique=True),
                      keep_default=False)

        # Deleting field 'OtherMember.name'
        db.delete_column('team_othermember', 'name')

        # Deleting field 'OtherMember.team'
        db.delete_column('team_othermember', 'team_id')

        # Deleting field 'OtherMember.phone'
        db.delete_column('team_othermember', 'phone')

        # Deleting field 'OtherMember.email'
        db.delete_column('team_othermember', 'email')

        # Deleting field 'OtherMember.age'
        db.delete_column('team_othermember', 'age')

        # Adding field 'Player.player'
        db.add_column('team_player', 'player',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['team.Member'], unique=True),
                      keep_default=False)

        # Deleting field 'Player.name'
        db.delete_column('team_player', 'name')

        # Deleting field 'Player.team'
        db.delete_column('team_player', 'team_id')

        # Deleting field 'Player.phone'
        db.delete_column('team_player', 'phone')

        # Deleting field 'Player.email'
        db.delete_column('team_player', 'email')

        # Deleting field 'Player.age'
        db.delete_column('team_player', 'age')


    models = {
        'team.othermember': {
            'Meta': {'object_name': 'OtherMember'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team.Team']"}),
            'title': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'team.player': {
            'Meta': {'object_name': 'Player'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team.Team']"})
        },
        'team.team': {
            'Meta': {'object_name': 'Team'},
            'club': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['team']