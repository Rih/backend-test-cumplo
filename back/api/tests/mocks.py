import json


API_RESPONSE = {
    'token': {
        'failed': {
            'error': 'invalid_grant',
            'error_description': 'The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client.'
        },
        'success': {
            'access_token': '7fe9ad7e6aeccac0cbc29af7a4b3fb180a8f0c48f2529a0e182659f2e97fecf8',
            'token_type': 'Bearer',
            'scope': 'write login',
            'created_at': 1626487193
        }
    },
    'observation': {
        'success': [
            {
                "id": 83433296,
                "observed_on": "2021-06-17",
                "description": None,
                "latitude": "-39.8371200562",
                "longitude": "-73.2069473267",
                "map_scale": None,
                "timeframe": None,
                "species_guess": "Mariposas y polillas",
                "user_id": 3918216,
                "taxon_id": 47157,
                "created_at": "2021-06-17T21:06:54.468Z",
                "updated_at": "2021-06-18T14:45:32.473Z",
                "place_guess": "Valdivia",
                "id_please": False,
                "observed_on_string": "Thu Jun 17 2021 17:02:30 GMT -0400 (GMT-4)",
                "iconic_taxon_id": 47158,
                "num_identification_agreements": 2,
                "num_identification_disagreements": 0,
                "time_observed_at": "2021-06-17T21:02:30.000Z",
                "time_zone": "Santiago",
                "location_is_exact": False,
                "delta": False,
                "positional_accuracy": 202,
                "private_latitude": None,
                "private_longitude": None,
                "geoprivacy": None,
                "quality_grade": "needs_id",
                "positioning_method": None,
                "positioning_device": None,
                "out_of_range": None,
                "license": "CC-BY-NC",
                "uri": "https://www.inaturalist.org/observations/83433296",
                "observation_photos_count": 1,
                "comments_count": 0,
                "zic_time_zone": "America/Santiago",
                "oauth_application_id": 333,
                "observation_sounds_count": 0,
                "identifications_count": 2,
                "captive": False,
                "community_taxon_id": 47157,
                "site_id": 1,
                "old_uuid": None,
                "public_positional_accuracy": 202,
                "mappable": True,
                "cached_votes_total": 0,
                "last_indexed_at": "2021-06-18T14:45:36.018Z",
                "private_place_guess": None,
                "uuid": "0faceebf-5e45-4d52-b2ee-08909c9f7f17",
                "taxon_geoprivacy": None,
                "short_description": None,
                "user_login": "ndarwin",
                "iconic_taxon_name": "Insecta",
                "tag_list": [],
                "faves_count": 0,
                "created_at_utc": "2021-06-17T21:06:54.468Z",
                "updated_at_utc": "2021-06-18T14:45:32.473Z",
                "time_observed_at_utc": "2021-06-17T21:02:30.000Z",
                "owners_identification_from_vision": True,
                "taxon": {
                    "id": 47157,
                    "name": "Lepidoptera",
                    "rank": "order",
                    "ancestry": "48460/1/47120/372739/47158/184884",
                    "common_name": {
                        "id": 865882,
                        "name": "Butterflies and Moths",
                        "is_valid": True,
                        "lexicon": "English"
                    }
                },
                "iconic_taxon": {
                    "id": 47158,
                    "name": "Insecta",
                    "rank": "class",
                    "rank_level": 50.0,
                    "ancestry": "48460/1/47120/372739"
                },
                "user": {
                    "login": "ndarwin",
                    "user_icon_url": None
                },
                "photos": [
                    {
                        "id": 137026879,
                        "user_id": 3918216,
                        "native_photo_id": "137026879",
                        "square_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/137026879/square.jpeg?1623964017",
                        "thumb_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/137026879/thumb.jpeg?1623964017",
                        "small_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/137026879/small.jpeg?1623964017",
                        "medium_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/137026879/medium.jpeg?1623964017",
                        "large_url": "https://inaturalist-open-data.s3.amazonaws.com/photos/137026879/large.jpeg?1623964017",
                        "created_at": "2021-06-17T21:06:59.196Z",
                        "updated_at": "2021-06-17T21:06:59.196Z",
                        "native_page_url": "https://www.inaturalist.org/photos/137026879",
                        "native_username": "ndarwin",
                        "native_realname": "Nelson",
                        "license": 2,
                        "subtype": None,
                        "native_original_image_url": None,
                        "uuid": "d3336fc4-aacf-44a1-80bc-7046b14c4ac7",
                        "license_code": "CC-BY-NC",
                        "attribution": "(c) Nelson, some rights reserved (CC BY-NC)",
                        "license_name": "Creative Commons Attribution-NonCommercial License",
                        "license_url": "http://creativecommons.org/licenses/by-nc/4.0/",
                        "type": "LocalPhoto"
                    }
                ]
            }
        ]
    }
}


class ItemMock:
    def __init__(self):
        self.bbox = json.dumps({'sw': {'lat': 1, 'lng': 1}, 'ne': {'lat': 1, 'lng': 1}})
        self.results = json.dumps([
            {
                'photos': [
                    {
                        'thumb_url': 'http://thumb.url.com/img.png',
                        'large_url': 'http://thumb.url.com/img.png',
                    }
                ],
                'b': 2
            }
        ])
        self.created = ''
        self.uri = ''
        self.user_id = ''


class TableRefMock:

    def __iter__(self):
        return [ItemMock(), ItemMock()]


class RowResultMock:

    @property
    def total_rows(self):
        return 1


class QJobMock:
    def result(self):
        return RowResultMock()

    @property
    def destination(self):
        return TableRefMock()


class RowIterMock:
    def __iter__(self):
        for i in [ItemMock(), ItemMock()]:
            yield i


class TableIterMock:
    def __iter__(self):
        for i in [ItemMock(), ItemMock()]:
            yield i


class BQClientMock:
    def __init__(self, **kwargs):
        self.insert = kwargs.get('insert', True)
        pass

    def query(self, qs: str) -> QJobMock:
        return QJobMock()

    def get_table(self, p: RowIterMock) -> TableIterMock:
        return TableIterMock()

    def list_rows(self, dest, **kwargs):
        return RowIterMock()

    def insert_rows_json(self, tbl_id: str, list_dict: list) -> list:
        if not self.insert:
            return [
                {
                    'index': 0,
                    'errors': [
                        {
                            'reason': 'invalid',
                            'location': 'x_id',
                            'debugInfo': '',
                            'message': 'no such field: x_id.'
                        }
                    ]
                }
            ]

        return []


class bquerymock:

    def __init__(self, **kwargs):
        self.args = kwargs

    def Client(self):
        return BQClientMock(**self.args)
