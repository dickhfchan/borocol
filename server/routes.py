from flask import current_app as app
import controllers
from middlewares import auth

# helpers

def group(opt, routes):
    for item in routes:
        prefix = opt.get('prefix')
        middlewares = opt.get('middlewares')
        if prefix:
            item['path'] = (prefix + item['path']).rstrip('/')
        if middlewares:
            item['middlewares'] = middlewares + item.get('middlewares', [])
    return routes

# generate for resource controller and normal controller
# simpleRoutes: [[], ...]
def generate(controller, prefix, simpleRoutes = [], overwrite = False):
    # inject default
    if not overwrite:
        names = set()
        for item in simpleRoutes:
            name = item if isinstance(item, str) else item['path']
            names.add(name)
        defaults = set(['find', 'select', 'store', 'update', 'destroy'])
        diff = list(defaults-names)
        simpleRoutes = simpleRoutes + diff
    # convert to completed routes
    routes = []
    for item in simpleRoutes:
        route = {'controller': controller}
        routes.append(route)
        if isinstance(item, dict):
            route.update(item)
            name = item['path']
        else:
            name = item
        if name == 'find':
            route.update({'path': prefix + '/<id>', 'action': route.get('action', 'select'), 'methods': route.get('methods', ['GET'])})
        elif name == 'select':
            route.update({'path': prefix + '.select', 'action': route.get('action', 'select'), 'methods': route.get('methods', ['GET', 'POST'])})
        elif name == 'store':
            route.update({'path': prefix, 'action': route.get('action', 'store'), 'methods': route.get('methods', ['POST'])})
        elif name == 'update':
            route.update({'path': prefix, 'action': route.get('action', 'update'), 'methods': route.get('methods', ['PUT'])})
        elif name == 'destroy':
            route.update({'path': prefix, 'action': route.get('action', 'destroy'), 'methods': route.get('methods', ['DELETE'])})
        else:
            route.update({'path': prefix + item['path']})
    return routes

#
routes = [
    {'path': '/', 'controller': controllers.IndexController, 'action': 'index'},
    {'path': '/<t1>', 'controller': controllers.IndexController, 'action': 'spa'},
    {'path': '/<t1>/<t2>', 'controller': controllers.IndexController, 'action': 'spa'},
    *group({'prefix': app.config['api_prefix']}, [
        *generate(controllers.CourseDetailController, '/course_detail'),
        *generate(controllers.UserController, '/user', [
            {'path': '/current_user', 'action': 'current_user', 'methods': ['GET']},
            {'path': '/register', 'action': 'register', 'methods': ['POST']},
            {'path': '/login', 'action': 'login', 'methods': ['POST']},
            {'path': '/logout', 'action': 'logout', 'methods': ['GET'], 'middlewares': [auth]},
        ], True),
    ]),
]
