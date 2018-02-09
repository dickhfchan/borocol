from flask import current_app as app, request
import models
from ResourceController import ResourceController

class UserController(ResourceController):
    model = models.user
