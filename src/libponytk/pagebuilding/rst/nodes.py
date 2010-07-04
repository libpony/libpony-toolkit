from docutils import nodes as basenodes


class Abbreviation(basenodes.Inline, basenodes.TextElement): pass
class Url(basenodes.Inline, basenodes.TextElement): pass
class File(basenodes.Inline, basenodes.TextElement): pass
class Command(basenodes.Inline, basenodes.TextElement): pass

basenodes._add_node_class_names(["Abbreviation", "Url", "File", "Command"])
