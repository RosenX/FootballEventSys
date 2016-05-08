# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'RedCard.reason' to match new field type.
        db.rename_column('result_redcard', 'reason', 'reason_id')
        # Changing field 'RedCard.reason'
        db.alter_column('result_redcard', 'reason_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['result.RedCardReason'], null=True))
        # Adding index on 'RedCard', fields ['reason']
        db.create_index('result_redcard', ['reason_id'])


        # Renaming column for 'YellowCard.reason' to match new field type.
        db.rename_column('result_yellowcard', 'reason', 'reason_id')
        # Changing field 'YellowCard.reason'
        db.alter_column('result_yellowcard', 'reason_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['result.YellowCardReason'], null=True))
        # Adding index on 'YellowCard', fields ['reason']
        db.create_index('result_yellowcard', ['reason_id'])


    def backwards(self, orm):
        # Removing index on 'YellowCard', fields ['reason']
        db.delete_index('result_yellowcard', ['reason_id'])

        # Removing index on 'RedCard', fields ['reason']
        db.delete_index('result_redcard', ['reason_id'])


        # Renaming column for 'RedCard.reason' to match new field type.
        db.rename_column('result_redcard', 'reason_id', 'reason')
        # Changing field 'RedCard.reason'
        db.alter_column('result_redcard', 'reason', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Renaming column for 'YellowCard.reason' to match new field type.
        db.rename_column('result_yellowcard', 'reason_id', 'reason')
        # Changing field 'YellowCard.reason'
        db.alter_column('result_yellowcard', 'reason', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

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
            'referee': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'round_belong': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Schedule']"}),
            'teamA': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'A_team'", 'to': "orm['team.Team']"}),
            'teamA_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'teamB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'B_team'", 'to': "orm['team.Team']"}),
            'teamB_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'result.redcard': {
            'Meta': {'object_name': 'RedCard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.SingleMatch']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team.Player']"}),
            'reason': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['result.RedCardReason']", 'null': 'True', 'blank': 'True'})
        },
        'result.redcardreason': {
            'Meta': {'object_name': 'RedCardReason'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'result.score': {
            'Meta': {'object_name': 'Score'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.SingleMatch']"}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team.Player']"})
        },
        'result.sumscore': {
            'Meta': {'object_name': 'SumScore'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sum_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team.Team']"})
        },
        'result.yellowcard': {
            'Meta': {'object_name': 'YellowCard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event.SingleMatch']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team.Player']"}),
            'reason': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['result.YellowCardReason']", 'null': 'True', 'blank': 'True'})
        },
        'result.yellowcardreason': {
            'Meta': {'object_name': 'YellowCardReason'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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

    complete_apps = ['result']