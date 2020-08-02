import classes as Classes

file_name = input('Введите имя файла (*.html) или нажмите Enter для вывода на экран:')
if file_name:
    outputF = file_name
else:
    outputF = None    

if __name__ == "__main__":
    with Classes.HTML(output=outputF) as doc:
        with Classes.TopLevelTag("head", needTab=False) as head:
            with Classes.Tag("title") as title:
                title.text = "hello"
                head += title
            doc += head

        with Classes.TopLevelTag("body", needTab=True) as body:
            with Classes.Tag("h1", is_single=False, needTab=False, klass=("main-text",)) as h1:
                h1.text = "Test"
                body += h1

            with Classes.Tag("div", is_single=False, needTab=True, klass=("container", "container-fluid"), id="lead") as div:
                with Classes.Tag("p") as paragraph:
                    paragraph.text = "another test"
                    div += paragraph

                with Classes.Tag("img", is_single=True, needTab=True, klass=None, src="/icon.png") as img:
                    div += img

                body += div

            doc += body

