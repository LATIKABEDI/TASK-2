import re
import json

def validate_credentials(credentials):
    username = credentials.get('username')
    password = credentials.get('password')
    
    if not username or not password:
        return 'FAILED'
    
    if not re.match('^[a-zA-Z0-9]{1,8}$', username):
        return 'FAILED'
    
    if not re.match('^(?=.*[a-zA-Z0-9])(?=.*[@$!%*?&])[a-zA-Z0-9@$!%*?&]{1,8}$', password):
        return 'FAILED'
    
    return 'SUCCESS'