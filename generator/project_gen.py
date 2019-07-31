import jsonpickle as jsonpickle
from model.project import Project
import string
import random
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
        # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/project.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = a


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


status_list = ["development", "release", "stable", "obsolete"]
view_state_list = ["public", "private"]


testdata = [Project(name=random_string("name",10),
                    status=random.choice(status_list), view_state=random.choice(view_state_list),
                    description=random_string("desc", 10))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))