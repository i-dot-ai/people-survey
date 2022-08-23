from typing import Optional

from ninja import Schema


class SurveySchema(Schema):
    data: Optional[str] = ...


class AnswerSchema(Schema):
    data: Optional[str] = ...
