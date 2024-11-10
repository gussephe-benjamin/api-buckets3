import json
import boto3
import os
import uuid

# Crear cliente S3
s3_client = boto3.client('s3')
bucket_name = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    try:
        # Obtener el JSON del cuerpo de la solicitud
        body = json.loads(event['body'])
        
        # Generar un nombre de archivo único
        file_name = f"{uuid.uuid4()}.json"
        
        # Guardar el JSON como archivo en el bucket S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json.dumps(body),
            ContentType='application/json'
        )

        # Retornar una respuesta exitosa
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Archivo guardado en S3", "file_name": file_name})
        }
    
    except Exception as e:
        # Manejo de errores
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error al guardar el archivo en S3", "error": str(e)})
        }
