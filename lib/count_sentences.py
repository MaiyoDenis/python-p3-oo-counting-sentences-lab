class MyString:
    def __init__(self, initial_value=""):
        self._value = ""
        self.value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        import re
        # Count sentences ending with ., !, or ? including multiple punctuation marks like !! or ...
        sentences = re.findall(r'[^.!?]*[.!?]+', self._value)
        return len(sentences)
