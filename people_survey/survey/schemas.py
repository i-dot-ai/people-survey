from typing import Optional

from ninja import Schema


class SurveySchema(Schema):
    data: Optional[dict] = ...


class ResultSchema(Schema):
    data: Optional[dict] = ...
