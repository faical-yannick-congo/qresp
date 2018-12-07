class PaperDetails(object):
    def __init__(self):
        self.id = ""
        self.title = ""
        self.tags = []
        self.collections = []
        self.authors = []
        self.publication = ""
        self.abstract = ""
        self.doi = ""
        self.serverPath = ""
        self.folderAbsolutePath = ""
        self.fileServerPath = ""
        self.downloadPath = ""
        self.notebookPath = ""
        self.notebookFile = ""
        self.cite = ""
        self.heads = ""
        self.charts = []
        self.datasets = []
        self.workflows = []
        self.scripts = []
        self.tools = []
        self.year = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, val):
        self.__id = val

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val):
        self.__title = val

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, val):
        self.__tags = val

    @property
    def collections(self):
        return self.__collections

    @collections.setter
    def collections(self, val):
        self.__collections = val

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, val):
        self.__authors = val

    @property
    def publication(self):
        return self.__publication

    @publication.setter
    def publication(self, val):
        self.__publication = val

    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, val):
        self.__abstract = val

    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self, val):
        self.__doi = val

    @property
    def serverPath(self):
        return self.__serverPath

    @serverPath.setter
    def serverPath(self, val):
        self.__serverPath = val

    @property
    def folderAbsolutePath(self):
        return self.__folderAbsolutePath

    @folderAbsolutePath.setter
    def folderAbsolutePath(self, val):
        self.__folderAbsolutePath = val

    @property
    def fileServerPath(self):
        return self.__fileServerPath

    @fileServerPath.setter
    def fileServerPath(self, val):
        self.__fileServerPath = val

    @property
    def downloadPath(self):
        return self.__downloadPath

    @downloadPath.setter
    def downloadPath(self, val):
        self.__downloadPath = val

    @property
    def notebookPath(self):
        return self.__notebookPath

    @notebookPath.setter
    def notebookPath(self, val):
        self.__notebookPath = val

    @property
    def notebookFile(self):
        return self.__notebookFile

    @notebookFile.setter
    def notebookFile(self, val):
        self.__notebookFile = val

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        self.__year = val

    @property
    def cite(self):
        return self.__cite

    @cite.setter
    def cite(self, val):
        self.__cite = val

    @property
    def imageFile(self):
        return self.__imageFile

    @imageFile.setter
    def imageFile(self, val):
        self.__imageFile = val

    @property
    def charts(self):
        return self.__charts

    @charts.setter
    def charts(self, val):
        self.__charts = val

    @property
    def datasets(self):
        return self.__datasets

    @datasets.setter
    def datasets(self, val):
        self.__datasets = val

    @property
    def scripts(self):
        return self.__scripts

    @scripts.setter
    def scripts(self, val):
        self.__scripts = val

    @property
    def tools(self):
        return self.__tools

    @tools.setter
    def tools(self, val):
        self.__tools = val

    @property
    def workflows(self):
        return self.__workflows

    @workflows.setter
    def workflows(self, val):
        self.__workflows = val

    @property
    def heads(self):
        return self.__heads

    @heads.setter
    def heads(self, val):
        self.__heads = val