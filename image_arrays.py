from line_profiler import profile
import numpy as np
import base64
import json
import io
@profile
def image_array(image):
    image_array = np.array(image)
    return image_array

@profile
def image_to_data_uri(image):
    """
    Encodes an image to Base64, converts it to JSON, and then creates a Data URI.

    Args:
    image_path (str): The path to the image file.

    Returns:
    str: A Data URI representing the image.
    """

    def encode_image_to_json(path):
        """
        Encodes an image to Base64 and then converts it to JSON.

        Args:
        path (str): The path to the image file.

        Returns:
        str: A JSON string containing the Base64 encoded image.
        """
        buffered = io.BytesIO()
        image.save(buffered, format=image.format)
        encoded_string = base64.b64encode(buffered.getvalue()).decode()
        # Create a dictionary to hold the image data and convert it to JSON
        image_json = {"image": encoded_string}
        json_str=json.dumps(image_json)
        return json_str

    # Encode the image to JSON
    json_str = encode_image_to_json(image)

    # Extract the Base64 encoded string from the JSON
    image_data = json.loads(json_str)
    base64_string = image_data["image"]

    # Create the Data URI
    data_uri = f"data:image/png;base64,{base64_string}"
    return data_uri
