#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reference:
http://www.slideshare.net/ishraqabd/publish-subscribe-model-overview-13368808
Author: https://github.com/HanWenfang
"""


class Provider:
    def __init__(self):
        self.msg_queue = []
        self.subscribers = {}

    def notify(self, pub_name, msg):
        self.msg_queue.append((pub_name, msg))

    def subscribe(self, msg, subscriber):
        self.subscribers.setdefault(msg, []).append(subscriber)

    def unsubscribe(self, msg, subscriber):
        self.subscribers[msg].remove(subscriber)

    def update(self):
        for pub_name, msg in self.msg_queue:
            for sub in self.subscribers.get(pub_name, []):
                sub.run(msg)
        self.msg_queue = []


class Publisher:
    def __init__(self, name, msg_center):
        self.name = name
        self.provider = msg_center

    def publish(self, msg):
        self.provider.notify(self.name, msg)


class Subscriber:
    def __init__(self, sub_name, msg_center):
        self.sub_name = sub_name
        self.provider = msg_center

    def subscribe(self, pub_name):
        self.provider.subscribe(pub_name, self)

    def unsubscribe(self, pub_name):
        self.provider.unsubscribe(pub_name, self)

    def run(self, msg):
        print("{} got {}".format(self.sub_name, msg))


def main():
    message_center = Provider()

    fftv = Publisher('fftv', message_center)

    jim = Subscriber("jim", message_center)
    jim.subscribe("fftv")
    jack = Subscriber("jack", message_center)
    jack.subscribe("music")
    gee = Subscriber("gee", message_center)
    gee.subscribe("fftv")
    vani = Subscriber("vani", message_center)
    vani.subscribe("movie")
    vani.unsubscribe("movie")

    fftv.publish("cartoon")
    fftv.publish("music")
    fftv.publish("ads")
    fftv.publish("movie")
    fftv.publish("cartoon")
    fftv.publish("cartoon")
    fftv.publish("movie")
    fftv.publish("blank")

    message_center.update()


if __name__ == "__main__":
    main()


OUTPUT = """
jim got cartoon
jack got music
gee got movie
jim got cartoon
jim got cartoon
gee got movie
"""
