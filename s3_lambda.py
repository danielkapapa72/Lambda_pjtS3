def lambda_handler(event,context):
    
    #1. Get the bucket name
    bucket-event['Record'][0]['bucket']['name']
    #2. Get the file/key name
    key - urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding-'utf-8')
    try:
    #3. Fetch file from s3
        response - s3.get-object(Bucket-bucket, key-key)
    #4. Deserialize the file's content
        text - response["Body"].read().decode()
        data - json.load(text)
    #5. Print the content
        print(data)
    #6. Parse and Print the transactions
        transaction - data['transactions']
        for record in transaction:
            print(record['transType'])
        return 'Success!'
    except Exception as e:
        print (e)
        raise e 