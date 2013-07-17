#! /usr/bin/env python

from twisted.internet import reactor
from twisted.web import static, server, resource

from controllers.jsontest import testList

if __name__ == "__main__":
    root = static.File("html")
    site = server.Site(root)
    reactor.listenTCP(8000, site)
    reactor.run()

