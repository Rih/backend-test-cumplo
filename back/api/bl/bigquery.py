# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json, os
from google.cloud import bigquery
from datetime import datetime
from django.conf import settings
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f'/{settings.GOOGLE_APP_CREDS_DIR}/{settings.APP_CREDS_NAME}'


class BigQuery:

    gcp_project = 'exam-rodrigo-diaz'
    bq_dataset = 'audit'
    bq_table_name = 'api_calls'
    query_template = '''SELECT
        ac.bbox,
        ac.results,
        ac.uri,
        ac.created,
        ac.user_id
        FROM `{gcp_project}.{bq_dataset}.{bq_table_name}` ac
        WHERE ac.user_id = {user}
        ORDER BY ac.created ASC
    '''

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.per_page = settings.BQ_PER_PAGE
        self.client = bigquery.Client()

    def select(self, page: int = 1) -> dict:
        page = 0 if page < 1 else page - 1
        dataset_ref = self.client.dataset(self.bq_dataset)
        query_str = self.query_template.format(
            gcp_project=self.gcp_project,
            bq_dataset=self.bq_dataset,
            bq_table_name=self.bq_table_name,
            user=self.user_id
        )
        query_job = self.client.query(query_str)
        res = query_job.result()
        total = res.total_rows
        destination = query_job.destination
        destination = self.client.get_table(destination)
        results_obj = self.client.list_rows(
            destination,
            start_index=page * self.per_page,
            max_results=self.per_page
        )
        results = [
            {
                'bbox': json.loads(row.bbox),
                'uri': row.uri,
                'results': json.loads(row.results),
                'created': row.created,
                'user_id': row.user_id,

            }
            for row in results_obj
        ]

        return {
            'data': results,
            'hasPrev': page > 0,
            'hasNext': (page + 1) * self.per_page < total,
            'current': page + 1,
            'perPage': self.per_page,
            'totalCurrent': len(results),
            'total': total
        }

    def insert(self, gps: dict, results: dict) -> dict:

        # Construct a BigQuery client object.
        table_id = f'{self.gcp_project}.{self.bq_dataset}.{self.bq_table_name}'
        rows_to_insert = [
            {
                'bbox': json.dumps(gps),
                'created': datetime.now().timestamp(),
                'results': json.dumps(results),
                'user_id': self.user_id,
                'uri': '/observations'
            },
        ]
        errors = self.client.insert_rows_json(
            table_id,
            rows_to_insert
        )
        # Make an API request.
        if not errors:
            print("New rows have been added.")
        else:
            print("Encountered errors while inserting rows: {}".format(errors))
        return not(errors)
