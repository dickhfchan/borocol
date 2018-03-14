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
        initialAction = getattr(ctlInstance, item['action'])
        middlewares = globalMiddlewares[:]
        if 'middlewares' in item:
            middlewares += item['middlewares']
        #
        actions = []
        def makeAction(index):
            mdl = middlewares[index]
            def action(*args, **kwargs):
                nextAction = actions[index + 1]
                return mdl(nextAction, *args, **kwargs)
            return action
        args2 = None
        kwargs2 = None
        def noArg(action):
            def actionWithoutArg():
                return action(*args2, **kwargs2)
            return actionWithoutArg
        for index, _ in enumerate(middlewares):
            action = makeAction(index)
            actions.append(action)
        actions.append(initialAction)
        for i, action in enumerate(actions):
            actions[i] = noArg(action)
        def entryAction(*args, **kwargs):
            nonlocal args2
            nonlocal kwargs2
            args2 = args
            kwargs2 = kwargs
            return actions[0]()
        endPoint = item['name'] if 'name' in item else str_rand(4)
        app.add_url_rule(item['path'], endPoint, view_func=entryAction, methods=item.get('methods', ['GET']))
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
