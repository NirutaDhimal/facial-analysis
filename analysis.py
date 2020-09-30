import boto3
import json

#change photo to the path and file name of your image
photo = "lisa.jpg"

client = boto3.client('rekognition')

with open(photo, 'rb') as image:
    response = client.detect_faces(
        Image = {'Bytes': image.read()},
        Attributes = ['ALL']
    )

#print(response)

for detail in response["FaceDetails"]:
    print("Details of candidate:")
    print("Gender: {}".format(detail['Gender']['Value']))
    print("Age range: {} - {} years old".format(detail['AgeRange']['Low'], detail['AgeRange']['High']))
    print("Emotion state: appears to be {}".format(detail['Emotions']['Type']))
    
    if (detail['Beard']['Value'] and detail['Mustache']['value']):
        print("The candidate has a beard and a mustache.")
    else:
        if(detail['Beard']['Value']):
            print("The candidate has a beard.")
        if(detail['Mustache']['Value']):
            print("The candidate has a mustache.")

    if (detail['Sunglasses']['Value']):
        print("The candidate is wearing sunglasses.")