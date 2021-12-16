""" REST API controllers responsible of handling the security schemas.
"""

from typing import Dict, Optional
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer
from connexion.exceptions import Unauthorized  # type: ignore
from dms2122backend.data.config import BackendConfiguration


def verify_api_key(token: str) -> Dict:
    """Callback testing the received API key.
    Args:
        - token (str): The received API key.
    Raises:
        - Unauthorized: When the given API key is not valid.
    Returns:
        - Dict: Information retrieved from the key to be passed to the endpoints.
    """
    with current_app.app_context():
        cfg: BackendConfiguration = current_app.cfg
        if not token in cfg.get_authorized_api_keys():
            raise Unauthorized('Invalid API key')
    return {}
    
    
    

def verify_token(token: str) -> Dict:
    """Callback testing a JWS user token.
    Args:
        - token (str): The JWS user token received.
    Raises:
        - Unauthorized: When the token is incorrect.
    Returns:
        - Dict: A dictionary with the user name (key `user`) if the credentials are correct.
    """
    with current_app.app_context():
        token_bytes: bytes = token.encode('ascii')
        jws: TimedJSONWebSignatureSerializer = current_app.jws
        try:
            data = jws.loads(token_bytes)
        except Exception as ex:
            raise Unauthorized from ex
        if 'user' not in data:
            return Unauthorized('Invalid token')
        return {
            'sub': data['sub'],
            'user': data['user']
        }