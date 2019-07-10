import boto3
from openpyxl import load_workbook
import pandas as pd
import xlrd
import json

wb = load_workbook(filename = 'results.xlsx')
ws = wb['results']
row = 2


def change(emotion):
    current = ['ANGRY', 'CONFUSED', 'DISGUSTED', 'HAPPY', 'CALM', 'SAD', 'SURPRISED']
    transform = ['ANGRY', 'CONFUSED', 'DISGUST', 'HAPPY', 'NEUTRAL', 'SAD', 'SURPRISED']
    result = ''
    for i in range(8):
        if current[i] == emotion:
            result = transform[i]
            break
    return result


export = pd.read_excel('export.xlsx')

for f in range(len(export)):
    if export['type'].at[f] == 'TEST':
        label = export['label'].at[f]

        if __name__ == "__main__":
            imageFile = export['name'].at[f][60:]
            bucket = 'bucket'
            client = boto3.client('rekognition')

            with open(imageFile, 'rb') as image:
                response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])
                print(response['FaceDetails'])

            if response['FaceDetails']==[]:
                ws['A' + str(row)] = imageFile
                wb.save('results.xlsx')
                row = row + 1
                print(row)
            else :
                ANGRY = 0.000
                CONFUSED = 0.000
                DISGUSTED = 0.000
                HAPPY = 0.000
                CALM = 0.000
                SAD = 0.000
                SURPRISED = 0.000

                con = 0.000
                ty = ''
                for emo in response['FaceDetails'][0]['Emotions']:
                    confidence = emo['Confidence']
                    type = emo['Type']
                    if confidence > con:
                        con = confidence
                        ty = change(type)

                ws['A'+str(row)] = imageFile
                ws['B' + str(row)] = ty
                ws['C' + str(row)] = con
                ws['D' + str(row)] = ty==label
                wb.save('results.xlsx')
                row = row+1
                print(row)


