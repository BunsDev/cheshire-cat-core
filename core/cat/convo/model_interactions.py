import time
from io import BytesIO
from enum import Enum
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, ConfigDict

class ModelInteraction(BaseModel):
    """
    Base class for interactions with models, capturing essential attributes common to all model interactions.

    Attributes
    ----------
    model_type : Literal["llm", "embedder"]
        The type of model involved in the interaction, either a large language model (LLM) or an embedder.
    source : str
        The source from which the interaction originates.
    prompt : str
        The prompt or input provided to the model.
    input_tokens : int
        The number of input tokens processed by the model.
    started_at : float
        The timestamp when the interaction started. Defaults to the current time.
    """

    model_type: Literal["llm", "embedder"]
    source: str
    prompt: str
    input_tokens: int
    started_at: float = Field(default_factory=lambda: time.time())

    model_config = ConfigDict(
        protected_namespaces=()
    )


class LLMModelInteraction(ModelInteraction):
    """
    Represents an interaction with a large language model (LLM).

    Inherits from ModelInteraction and adds specific attributes related to LLM interactions.

    Attributes
    ----------
    model_type : Literal["llm"]
        The type of model, which is fixed to "llm".
    reply : str
        The response generated by the LLM.
    output_tokens : int
        The number of output tokens generated by the LLM.
    ended_at : float
        The timestamp when the interaction ended.
    """

    model_type: Literal["llm"] = Field(default="llm")
    reply: str
    output_tokens: int
    ended_at: float


class EmbedderModelInteraction(ModelInteraction):
    """
    Represents an interaction with an embedding model.

    Inherits from ModelInteraction and includes attributes specific to embedding interactions.

    Attributes
    ----------
    model_type : Literal["embedder"]
        The type of model, which is fixed to "embedder".
    source : str
        The source of the interaction, defaulting to "recall".
    reply : List[float]
        The embeddings generated by the embedder.
    """
    model_type: Literal["embedder"] = Field(default="embedder")
    source: str = Field(default="recall")
    reply: List[float]