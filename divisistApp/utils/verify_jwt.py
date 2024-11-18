from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime, timezone, timedelta
import jwt

from datetime import datetime, timezone, date

def encode_jwt(user_id):
    key = "secret"
    payload = {
        'user_id': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=10)
    }
    encoded = jwt.encode(payload, key, algorithm="HS256")
    return encoded

def decode_jwt(token):
    key = "secret"
    try:
        decoded = jwt.decode(token, key, algorithms=["HS256"])
        
        exp = datetime.fromtimestamp(decoded['exp'], timezone.utc)
        now = datetime.now(timezone.utc)
        
        return exp > now
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
