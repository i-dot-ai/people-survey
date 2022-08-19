from ninja import Schema


class SurveySchema(Schema):
    data: str


class AnswerSchema(Schema):
    data: str
