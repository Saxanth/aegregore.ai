from services import *
from abc import ABC, abstractmethod
from enum import Enum
from ell import BaseModel, Field, Dict, Any

class AIGenerativeType(Enum):
    NONE    = 0
    AUDIO   = 1
    CODE    = 2
    IMAGE   = 3
    TEXT    = 4
    VIDEO   = 5

class GenerativeAIConfig(BaseModel):    
    name:       str = Field(description="The name of the generative AI model to use",   default="")
    api_key:    str = Field(description="The API key for the generative AI service",    default="")
    api_base:   str = Field(description="The base URL for the generative AI service",   default="")
    type: AIGenerativeType  = Field(description="The type of generative AI model to use", default=AIGenerativeType.NONE)

class GenerativeAIBaseClass(ABC):
    def __init__(self, config: GenerativeAIConfig):
        self.__configuration__: GenerativeAIConfig = config

    @property
    def get_config(self) -> GenerativeAIConfig: return self.__configuration__

    @abstractmethod
    async def generate(self, prompt: str, additional_settings: list[str] = []) -> any:        
        raise NotImplementedError("This method must be implemented in a subclass")