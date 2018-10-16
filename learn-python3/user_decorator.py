
from decorator import Drcorator

class userDecor:

    @Drcorator.json_out(indent=5)
    def json_nothing(self):
        return {"a": 2, "b": 3}

if __name__ == "__main__":
    a = userDecor()
    b = a.json_nothing()
    print(b)