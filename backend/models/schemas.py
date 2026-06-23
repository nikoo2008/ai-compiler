from pydantic import BaseModel
from typing import List, Dict, Any


class IntentModel(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]
    entities: List[str]


class IRModel(BaseModel):
    app_type: str
    entities: Dict[str, List[str]]
    flows: List[str]
    roles: Dict[str, List[str]]


class UISchema(BaseModel):
    pages: List[Dict[str, Any]]


class APISchema(BaseModel):
    endpoints: List[Dict[str, Any]]


class DBSchema(BaseModel):
    tables: List[Dict[str, Any]]


class AuthSchema(BaseModel):
    permissions: Dict[str, List[str]]


class FinalConfig(BaseModel):
    ui: UISchema
    api: APISchema
    db: DBSchema
    auth: AuthSchema