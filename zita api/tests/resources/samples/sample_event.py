from typing import Dict, Any

VALID_EVENT: Dict[str, Any] = {
    "version": "2.0",
    "routeKey": "ANY /{proxy+}",
    "rawPath": "/athena-request",
    "rawQueryString": "practiceid=12345&patientid=1&departmentid=1"
    "&athena_endpoint_path=v1/12345/patients/1/appointments&email=test%40mail.com",
    "headers": {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "authorization": (
            "Bearer eyJraWQiOiJ3SXpZSnlpWHFMNkpoQVNJMXR"
            "Ka2Y1SXBSWnp2bGpzTWgrM0tQYUJkQVJFPSIsImFsZy"
        ),
        "content-length": "84",
        "content-type": "application/json",
        "host": "jrds6nt8j4.execute-api.us-east-1.amazonaws.com",
        "postman-token": "31d57a09-f460-4a53-a173-cd21cc5438e5",
        "user-agent": "PostmanRuntime/7.28.4",
        "x-amzn-trace-id": "Root=1-61771d53-3a271045505cd52622b01799",
        "x-forwarded-for": "66.130.18.230",
        "x-forwarded-port": "443",
        "x-forwarded-proto": "https",
    },
    "queryStringParameters": {
        "athena_endpoint_path": "v1/12345/patients/1/appointments",
        "departmentid": "1",
        "email": "brock+test@gmail.com",
        "patientid": "1",
        "practiceid": "12345",
        "messagethreadid": "54231",
        "encounterid": "54231",
        "documentid": "54231",
        "patientcaseid": "54321",
        "result_type": "something",
    },
    "requestContext": {
        "accountId": "028439129753",
        "apiId": "jrds6nt8j4",
        "authorizer": {
            "jwt": {
                "claims": {
                    "auth_time": "1635195673",
                    "client_id": "jtcvb531drl28o513djc9mta9",
                    "event_id": "55ccac8e-e257-4404-add8-e184161bcd75",
                    "exp": "1635199273",
                    "iat": "1635195673",
                    "iss": (
                        "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_lVDieK4Cw"
                    ),
                    "jti": "ddfe5b06-2281-414b-b870-59bbe44fcff2",
                    "scope": "email",
                    "sub": "8fba3875-03fa-4f36-a3dd-7d15e6ef6907",
                    "token_use": "access",
                    "username": "8fba3875-03fa-4f36-a3dd-7d15e6ef6907",
                    "version": "2",
                },
                "scopes": ["email"],
            }
        },
        "domainName": "jrds6nt8j4.execute-api.us-east-1.amazonaws.com",
        "domainPrefix": "jrds6nt8j4",
        "http": {
            "method": "GET",
            "path": "/athena-request",
            "protocol": "HTTP/1.1",
            "sourceIp": "66.130.18.230",
            "userAgent": "PostmanRuntime/7.28.4",
        },
        "requestId": "HyGFAi2PoAMEMYQ=",
        "routeKey": "ANY /{proxy+}",
        "stage": "$default",
        "time": "25/Oct/2021:21:10:43 +0000",
        "timeEpoch": 1635196243012,
    },
    "pathParameters": {"proxy": "athena-request"},
    "body": (
        '{"params": {'
        '"departmentid":1}, "data": {}, "athena_endpoint_path": "23211/patients"'
        "}"
    ),
    "isBase64Encoded": False,
}
