class Page(object):
    def __init__(self, title=None, teaser=None, body=None, metadata=None,
            filepath=None, metadatapath=None):
        self.title = title
        self.teaser = teaser
        self.body = body
        if metadata is None:
            self.metadata = {}
        else:
            self.metadata = metadata
        self.filepath = filepath
        self.metadatapath = metadatapath

    def __unicode__(self):
        return u'[Page title=%s]' % self.title
