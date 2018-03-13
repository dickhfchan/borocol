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
    methods = opt.get('methods')
    for item in routes:
        if prefix:
            item['path'] = (prefix + item['path']).rstrip('/')
        if middlewares:
            item['middlewares'] = middlewares + item.get('middlewares', [])
        if controller and 'controller' not in item:
            item['controller'] = controller
        if methods and 'methods' not in item:
            item['methods'] = methods
    return routes
