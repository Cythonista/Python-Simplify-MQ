class MQ(object):
    def __init__(self, title = None, text = None):
        self.title = title
        self.text  = text

    def getTitle(self):
        return self.title

    def getText(self):
        return self.text
