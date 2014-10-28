from pecan import expose, redirect
from api.controllers import v1


class RootController(object):
    v1 = v1.ContainerController()
