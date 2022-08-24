from typing import Optional

from ninja import Schema


class SurveySchema(Schema):
    data: Optional[dict] = ...


class AnswerSchema(Schema):
    data: Optional[dict] = ...
