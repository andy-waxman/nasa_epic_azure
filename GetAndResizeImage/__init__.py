# Azure Funcion to get an NASA EPIC image, resize it and send out as an image.
# For more info about EPIC visit https://epic.gsfc.nasa.gov/
# Author: Andy Waxman
# License: MIT 
# Requests must be POST with a content-type of application/json
# Arguments in JSON object
# api_key: API key from NASA, Required
# identitier: 14 digit identifier for specific image, Required
# format: natural|enhanced, See NASA documention difference, default natural
# width: Width in pixels for output image, default 240, valid range 180 to 1850
# height: Height in pixels for output image, default 240, valid range 180 to 1850
# output: bmp|png|jpeg, Output format to serve image as, default bmp.
# Example with minimal required arguments : { "api_key":"YOUR_NASA_API_KEY", "identifier":"20220304002713" }

import datetime
import logging
import azure.functions as func
from PIL import Image
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from io import BytesIO

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("+")
    
    # Grabbing and validating posted data
    try:
        req_body = req.get_json()
    except:
        error = f"Unable to get body from request"
        logging.error(error)
        return func.HttpResponse(error, status_code=400)

    logging.info(f"body: {req_body}")
    
    api_key = req_body.get("api_key")  
    if api_key is None:
        error = f"No value was found for \"api_key\""
        logging.error(error)
        return func.HttpResponse(error, status_code=400)

    identifier =  req_body.get("identifier")  
    logging.info(f"identifier: {identifier}")
    if identifier is None:
        error = f"No value was found for \"identifier\""
        logging.error(error)
        return func.HttpResponse(error, status_code=400)

    if len(identifier) < 14:
        error = f"Invalid \"identifier\" value: {identifier}"
        logging.error(error)
        return func.HttpResponse(error, status_code=400)

    year = identifier[0:4]
    month = identifier[4:6]
    day = identifier[6:8]
    if not year.isdigit() or not month.isdigit() or not day.isdigit:
        error = f"Invalid date from month: {month}, day: {day}, year: {year}"
        logging.error(error)
        return func.HttpResponse(error, status_code=400)

    # Slight code smell using exception for validation
    try:
        datetime.date(year=int(year), month=int(month), day=int(day))
    except ValueError:
        error = f"Invalid date from month: {month}, day: {day}, year: {year}"
        logging.error(error)
        return func.HttpResponse(error, status_code=400)

    # Optional values
    format = req_body.get("format")
    if format is None:
        format = "natural"
    
    if format == "natural":
        image_type = "1b"
    elif format == "enhanced":
        image_type = "RGB"
    else:
        error = f"Unrecognized value for \"format\""
        logging.error(error)
        return func.HttpResponse(error, status_code=400)

    logging.info(f"format: {format}")
    nasa_url = f"https://api.nasa.gov/EPIC/archive/{format}"

    width = req_body.get("width")
    if width is None:
        width = 240
    
    if isinstance(width,str):
        if not width.isdigit():
            error = f"Unrecognized value for \"width\" {width}"
            logging.error(error)
            return func.HttpResponse(error, status_code=400)
        else:
            width = int(width)

    if width <= 120 or width > 1850:
        error = f"Invalid value for \"width\" {width}"
        logging.error(error)
        return func.HttpResponse(error, status_code=400)
    logging.info(f"width: {width}")

    height = req_body.get("height")
    if height is None:
        height = 240
    
    if isinstance(height,str):
        if not height.isdigit():
            error = f"Unrecognized value for \"height\" {height}"
            logging.error(error)
            return func.HttpResponse(error, status_code=400)
        else:
            height = int(height)

    if height <= 120 or height > 1850:
        error = f"Invalid value for \"height\" {height}"
        logging.error(error)
        return func.HttpResponse(error, status_code=400)
    logging.info(f"height: {height}")

    output = req_body.get("output")
    if output is None:
        output = "bmp"
    
    if output != "bmp" and output != "png" and output != "jpeg":
        error = f"Invalid value for \"output\" {output}"
        logging.error(error)
        return func.HttpResponse(error, status_code=400)
    logging.info(f"output: {output}")

    # Grab the image
    try:
        with urlopen(f"{nasa_url}/{year}/{month}/{day}/png/epic_{image_type}_{identifier}.png?api_key={api_key}") as imageurl:
            full_image = Image.open(imageurl)
    except HTTPError as e:
        error = f"HTTPError: {e.status}: {e.reason}"
        logging.error(error)
        return func.HttpResponse(error, status_code=e.status)
    except URLError as e:
        error = f"URLError: {e.reason}"
        logging.error(error)
        return func.HttpResponse(error, status_code=400)
    except TimeoutError:
        error = f"TimeoutError"
        logging.error(error)
        return func.HttpResponse(error, status_code=503)

    # Stripping out some outer space
    cropped_image = full_image.crop((100,100,1950,1950))
    
    # Resize
    size = (width,height)
    cropped_image.thumbnail(size)
 
    # Convert to byte data
    bio = BytesIO()
    cropped_image.save(bio,output.upper())
    bdata = bio.getvalue()

    # Clean up
    full_image.close()
    cropped_image.close()

    # Send response
    logging.info("-")
    return func.HttpResponse(
            body=bdata,
            status_code=200,
            mimetype=f"image/{output}"
        )
