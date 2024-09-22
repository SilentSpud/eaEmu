import yaml

from zope.interface import implements
from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.python.usage import portCoerce

from eaEmu.ea.games.mercs2 import Service

from . import loadConfig


## TODO: migrate to a eaEmu service that uses flags or config.yml to determine what services run
## The service should be put together based on what's in the tap section of config.yml
## Or maybe just select 'ra3' or 'mow' or 'mercs2' in the config and then start up that service
## TODO: consider finding a way to run 'ra3' and 'mercs2' by somehow sharing port 80
class EaEmuOptions(usage.Options):
    # optParameters = [['port', 'p', 1235, 'The port number to listen on.']]
    optParameters = [
        ["config", "c", "config.yml", "The YAML-formatted config file to load settings from. Any other options given on the command line overwrite what's in this file."],
        ["module", "m", None, "What module to load the Service from."],
        ## TODO: divert these game-specific options to another usage.Options in the module specified above?
        ["webPort", "p", None, "The port to run the http web services on, if applicable.", portCoerce],
    ]
    tapname = "eaEmu"

    def postOptions(self):
        config = loadConfig(self["config"])
        try:
            ## Replace option with those found in config only if they aren't
            ## already in the options dict that was passed in from the commandline.
            self.update(dict((k, v) for k, v in config["tap"][self.tapname].iteritems() if self.get(k, None) is None))
        except (KeyError, AttributeError) as ex:
            pass  ## section in config file was not found

        ##default vals must be set here, not above in definitions, otherwise there's no way to tell if a commandline
        ##option was passed to override what's in the config.
        self["webPort"] = self["webPort"] or 80

        if None in self.values():
            raise Exception("Missing an essential parameter. Add it to config file or commandline.")


class EaEmuServiceFactory(object):
    implements(IServiceMaker, IPlugin)
    description = "EA Online Server Emulator"
    options = EaEmuOptions
    tapname = options.tapname

    def makeService(self, options):
        return Service(**options)


eaEmu = EaEmuServiceFactory()
