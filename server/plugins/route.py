from utils import str_rand

controllerInstanceMap = {}
def getControllerInstance(ctl):
    key = str(id(ctl))
    if key not in controllerInstanceMap:
        controllerInstanceMap[key] = ctl()
    return controllerInstanceMap[key]

def registerMany(routes, globalMiddlewares, app):
    # for loop hasn't scope, so put loop code into func
    def resolveRoute(item):
        ctlInstance = getControllerInstance(item['controller'])
        originalAction = getattr(ctlInstance, item['action'])
        if 'middlewares' in item:
            middlewares = globalMiddlewares + item['middlewares']
        else:
            middlewares = list(globalMiddlewares)
        middlewares.reverse()
        def action(*args, **kwargs):
            next = originalAction
            def loop(mdl):
                nonlocal next
                oldNext = next
                def nextFunc(*args, **kwargs):
                    return mdl(oldNext, *args, **kwargs)
                next = nextFunc
            for mdl in middlewares:
                loop(mdl)
            return next(*args, **kwargs)
        endPoint = item['name'] if 'name' in item else str_rand(4)
        app.add_url_rule(item['path'], endPoint, view_func=action, methods=item.get('methods', ['GET']))
    for item in routes:
        resolveRoute(item)

# helpers

def group(opt, routes):
    prefix = opt.get('prefix')
    middlewares = opt.get('middlewares')
    controller = opt.get('controller')
    for item in routes:
        if prefix:
            item['path'] = (prefix + item['path']).rstrip('/')
        if middlewares:
            item['middlewares'] = middlewares + item.get('middlewares', [])
        if controller and 'controller' not in item:
            item['controller'] = controller
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
