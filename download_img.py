import os
import quilt3 as q3
from botocore import UNSIGNED
from botocore.config import Config

# Data

BUCKET_NAME = 'cellpainting-gallery'
b = q3.Bucket(f"s3://{BUCKET_NAME}")

DATASET_TYPE = 'cpg0000-jump-pilot'
S3_KEY_PATH = f'{DATASET_TYPE}/source_4/images'
TIMEPOINT = '2020_11_04_CPJUMP1'
MEASURE_FILE = 'BR00117006__2020-11-02T19_54_45-Measurement1'
PATH_TO_DATA = f'{S3_KEY_PATH}/{TIMEPOINT}/images/{MEASURE_FILE}/'
print(f"Attempting to download the data: {PATH_TO_DATA}")


try:
	b.fetch(PATH_TO_DATA, f'./data/{PATH_TO_DATA}')
	print(f"✅ Download successful! File saved as {os.path.abspath(PATH_TO_DATA)}")

except Exception as e:
	print(f"❌ An error occurred during download.")
	print(f"Error details: {e}")
 
 
# After some time
BUCKET_NAME = 'cellpainting-gallery'
b = q3.Bucket(f"s3://{BUCKET_NAME}")

DATASET_TYPE = 'cpg0000-jump-pilot'
S3_KEY_PATH = f'{DATASET_TYPE}/source_4/images'
TIMEPOINT = '2020_11_18_CPJUMP1_TimepointDay1'
MEASURE_FILE = 'BR00117006__2020-11-03T19_45_39-Measurement1'
PATH_TO_DATA = f'{S3_KEY_PATH}/{TIMEPOINT}/images/{MEASURE_FILE}/'
print(f"Attempting to download the data: {PATH_TO_DATA}")

try:
	b.fetch(PATH_TO_DATA, f'./data/{PATH_TO_DATA}')
	print(f"✅ Download successful! File saved as {os.path.abspath(PATH_TO_DATA)}")

except Exception as e:
	print(f"❌ An error occurred during download.")
	print(f"Error details: {e}")