import refles as rx
from enum import Enum

class Color(Enum):
    """Enum for color names."""
    PRIMARY = "#86B73D"
    SECONDARY = "#3E665C"
    EXTRA = "#3C403E"
    BACKGROUND = "#F1F1F1"
    TEXT = "#3C403E"
    

BASE_STYLE = {
    "background_color": Color.BACKGROUND.value, 
    "text_color": Color.TEXT.value,
    "primary_color": Color.PRIMARY.value
    
}