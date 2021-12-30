# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:52:34 2021

@author: akash
"""

import requests, time
import base64
import io
from PIL import Image

tic = time.time()
# Load Image with PIL
image = Image.open("1.jpg").convert("RGB")

# Convert to JPEG Buffer
buffered = io.BytesIO()
image.save(buffered, quality=90, format="JPEG")

# Base 64 Encode
img_str = base64.b64encode(buffered.getvalue())
img_str = img_str.decode("ascii")

# Construct the URL
upload_url = "".join([
    "https://detect.roboflow.com/hyperkvasir-polyp/1",
    "?api_key=WchXQJ1iXfb5FbAsQZAN",
    "&name=1.jpg"
])

# POST to the API
r = requests.post(upload_url, data=img_str, headers={
    "Content-Type": "application/x-www-form-urlencoded"
})

toc = time.time()

# Output result
print(r.json())

print(toc-tic)