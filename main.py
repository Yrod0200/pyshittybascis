from sys import stdout
import io


messages = ["Hello", ", ", "World", "!"]
printer = io.StringIO()

class HelloWord():
    def __init__(self) -> None:
        self.i = ""
        pass
    def loop_for_each_word_and_then_set_everything_on_io(self):
        for message in messages:
            self.i += message
        printer.write(self.i)
    def after_getting_everything_on_the_io_then_print_everything(self):
        stdout.write(printer.getvalue())

helloworld = HelloWord()
helloworld.loop_for_each_word_and_then_set_everything_on_io()
helloworld.after_getting_everything_on_the_io_then_print_everything()