class Tag:
    def __init__(self, tag, is_single=False, needTab=False, klass=None, **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.is_single = is_single
        self.needTab = needTab #для ввода с новой строки текущего тэга - для удобства чтения

        if klass is not None:
            self.attributes["class"] = " ".join(klass)

        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def __iadd__(self, other):
        self.text = self.text + str(other)
        return self

    def __enter__(self):
        return self

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)
        if self.is_single:
            if self.needTab:
                return "\n<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs)
            else:
                return "\n<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs)
        else:
            if self.needTab:
                return "\n<{tag} {attrs}>\n{text}\n</{tag}>".format(
                    tag=self.tag, attrs=attrs, text=self.text
                )
            else:
                return "<{tag} {attrs}>\n{text}\n</{tag}>".format(
                    tag=self.tag, attrs=attrs, text=self.text
                )

    
    def __exit__(self, type, value, traceback):
        return self

class HTML:
    def __init__(self, output):
        self.output = output
        self.text = ""

    def __iadd__(self, other):
        self.text = self.text + str(other)
        return self

    def __enter__(self):
        return self

    def __str__(self):
        return "<{tag}>\n{text}\n</{tag}>".format(
            tag="html", text=self.text
        )

    def __exit__(self, type, value, traceback):
        if self.output is not None:
            with open(self.output, "w") as f1:
                f1.write(str(self))            
        else:
            print(self)

class TopLevelTag:
    def __init__(self, tag, needTab=False):
        self.tag = tag
        self.text = ""
        self.needTab = needTab #для ввода с новой строки текущего тэга - для удобства чтения

    def __iadd__(self, other):
        self.text = self.text + str(other)
        return self

    def __enter__(self):
        return self

    def __str__(self):
        if self.needTab:
            return "\n<{tag}>\n{text}\n</{tag}>".format(
                tag=self.tag, text=self.text
            )
        else:
            return "<{tag}>\n{text}\n</{tag}>".format(
                tag=self.tag, text=self.text
            )

    def __exit__(self, type, value, traceback):
        return self
