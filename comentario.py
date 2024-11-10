import json
import boto3
import os
from datetime import datetime
import uuid

s3_client = boto3.client('s3')
bucket_name = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    try:
        # Obtenemos los datos del cuerpo de la solicitud
        body = json.loads(event['body'])
        
        # Creamos un nombre único para el archivo JSON
        file_name = f"{uuid.uuid4()}.json"
        
        # Guardamos los datos en el bucket S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json.dumps(body),
            ContentType='application/json'
        )

        # Retornamos una respuesta exitosa
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Comentario guardado correctamente en S3", "file_name": file_name})
        }
    
    except Exception as e:
        # Manejo de errores
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error al guardar el comentario en S3", "error": str(e)})
        }
