from google.cloud import storage
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

# Set up the Google Cloud Storage client
storage_client = storage.Client()
bucket_name = "your-bucket-name"
bucket = storage_client.bucket(bucket_name)

# Set up the Google Cloud Vertex AI client
endpoint_id = "your-endpoint-id"
endpoint = f"projects/{PROJECT_ID}/locations/{REGION}/endpoints/{endpoint_id}"
aiplatform.init(project=PROJECT_ID, location=REGION)

# Define the input parameters for the endpoint
input_params = {
    "input_1": Value(string_value="your-value"),
    "input_2": Value(int_value=123),
    "input_3": Value(float_value=1.23),
}

# Set up the prediction request
request = aiplatform_v1beta1.types.PredictRequest(
    endpoint=endpoint,
    instances=[json_format.ParseDict(input_params, Value())],
)

# Get a list of the image file names in the Google Cloud Storage bucket
blobs = bucket.list_blobs(prefix="your-image-folder/")
image_files = [blob.name for blob in blobs if blob.name.endswith(".jpg")]

# Loop over the image files and make predictions for each one
for image_file in image_files:
    # Download the image from Google Cloud Storage
    blob = bucket.blob(image_file)
    image_bytes = blob.download_as_bytes()

    # Set the image bytes as input to the endpoint
    input_params["image_bytes"] = Value(bytes_value=image_bytes)

    # Send the prediction request to the endpoint
    response = aiplatform.PredictionServiceClient().predict(request)

    # Process the prediction response as necessary
    prediction = response.predictions[0]
    print(prediction)