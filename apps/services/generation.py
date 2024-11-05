from abc import ABC, abstractmethod
from enum import Enum
from ell import BaseModel, Field, Dict, Any

class GenerativeModelType(Enum):
    NONE    = 0 # ignored
    AUDIO   = 1 # audio generation
    CODE    = 2 # code  generation
    IMAGE   = 3 # image generation
    TEXT    = 4 # text  generation
    VIDEO   = 5 # video generation 

class ModelConfig(BaseModel):
    api_key:  str  = Field(description="The API key for the generative AI service",    default="")
    api_base: str  = Field(description="The base URL for the generative AI service",   default="")    
    api_args: Dict = Field(description="A dictionary of values representing the arguments to use for the generative model", default={"model" : ''})
    type: GenerativeModelType  = Field(description="The type of generative AI model to use", default=GenerativeModelType.NONE)

class GenerativeModel(ABC):
    def __init__(self, config: ModelConfig):
        self.__configuration__: ModelConfig = config

    @property
    def get_config(self) -> ModelConfig: return self.__configuration__.model_copy()

    @abstractmethod
    async def generate(self, prompt: str, additional_settings: Dict[str, Any] = []) -> Any:
        raise NotImplementedError("This method must be implemented in a subclass")