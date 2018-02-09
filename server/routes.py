from flask import current_app as app
import controllers

# helpers

def group(opt, routes):
    for item in routes:
        prefix = opt.get('prefix')
        middlewares = opt.get('middlewares')
        if prefix:
            item['path'] = (prefix + item['path']).rstrip('/')
        if middlewares:
            item['middlewares'] = middlewares + item['middlewares']
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
        if isinstance(item, str):
            path = item
            action = None
            methods = None
        else:
            path = item['path']
            action = item['action']
            methods = item['methods']
        name = path
        if name == 'find':
            routes.append({'path': prefix + '/<id>', 'controller': controller, 'action': action or 'select', 'methods': methods or ['GET']})
        elif name == 'select':
            routes.append({'path': prefix + '.select', 'controller': controller, 'action': action or 'select', 'methods': methods or ['GET', 'POST']})
        elif name == 'store':
            routes.append({'path': prefix, 'controller': controller, 'action': action or 'store', 'methods': methods or ['POST']})
        elif name == 'update':
            routes.append({'path': prefix, 'controller': controller, 'action': action or 'update', 'methods': methods or ['PUT']})
        elif name == 'destroy':
            routes.append({'path': prefix, 'controller': controller, 'action': action or 'destroy', 'methods': methods or ['DELETE']})
        else:
            routes.append({'path': prefix + path, 'controller': controller, 'action': action, 'methods': methods})
    return routes

#
routes = [
    {'path': '/', 'controller': controllers.IndexController, 'action': 'index'},
    {'path': '/<t1>', 'controller': controllers.IndexController, 'action': 'spa'},
    {'path': '/<t1>/<t2>', 'controller': controllers.IndexController, 'action': 'spa'},
    *group({'prefix': app.config['api_prefix']}, [
        *generate(controllers.CourseDetailController, '/course_detail'),
        *generate(controllers.UserController, '/user', [
            {'path': '/register', 'action': 'register', 'methods': ['POST']},
        ], True),
    ]),
]
