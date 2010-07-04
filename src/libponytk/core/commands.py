import logging

REGISTRY = {}

class CommandMetaClass(type):
    """
    This is used as a simple registry for all the command classes
    that are imported as subclasses of BaseCommand.
    """

    def __new__(meta, classname, bases, classDict):
        cls = type.__new__(meta, classname, bases, classDict)
        if classDict['__module__'] != __name__:
            cmdname = classDict['__module__'].split('.')[-1]
            if cmdname in REGISTRY:
                LOG.error("%s already in use." % cmdname)
            else:
                REGISTRY[cmdname] = cls
        return cls

class BaseCommand(object):
    __metaclass__ = CommandMetaClass

    def __init__(self):
        pass

    def pre_execute(self, args):
        return True

    def execute(self, args):
        pass

    def post_execute(self, result, args):
        pass

    def __call__(self, args):
        self.log = logging.getLogger(self.__class__.__module__ + '.' + self.__class__.__name__)
        self.log.debug("Executing command")
        if self.pre_execute(args):
            result = self.execute(args)
            self.post_execute(result, args)

    @classmethod
    def provide_arguments(cls, parser):
        """
        Here a command can attach additional arguments to the given
        parser.
        """
        pass
