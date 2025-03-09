# __init__.py

"""
VisionCraft Package

This package provides tools for computer vision tasks, including image processing,
model training, and inference.
"""

# Import necessary modules or classes to expose them at the package level
from .image_processing import preprocess_image, postprocess_image
from .model import VisionModel
from .utils import load_config, save_results

# Define the version of the package
__version__ = "0.1.0"

# Optionally, you can define a list of public objects
__all__ = [
    "preprocess_image",
    "postprocess_image",
    "VisionModel",
    "load_config",
    "save_results",
]
