# edison
Authentication middleware for JWT auth in Flask and Django apps

![edison architecture](/edison_architecture.png "edison architecture")


## Usage
_____

### Django Integration

#### settings.py

```python
MIDDLEWARE_CLASSES = [
  'django.middleware.security.SecurityMiddleware',
  ...
  'edison.middleware.django.JWTAuthenticationMiddleware'
]

EDISON_JWT_AUTHENTICATION_HEADER = 'TOKEN'
```

### Flask Integration

#### use as decorator function

```python
    # app.py
    from flask import render_template
    from edison.middleware.flask import edison_jwt_authentication_required

    @app.route('/only-auth-users')
    @edison_jwt_authentication_required(jwt_authentication_header='TOKEN')
    def only_auth_users():
      return render_template('only_auth_users.html')
```

## Join me make JWT even more awesome!
_____________________________________
:+1::+1::+1::+1::+1::+1::+1::+1::+1:
