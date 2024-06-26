name = "fabric"

version = "0.0.1"

authors = [
    "Arjun Thekkumadathil"
]


# tools = [
#     "hello"
# ]

requires = [
    "~python-3"
]

uuid = "toybrid.fabric.py"

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")
    env.KONFIG_SETTINGS=("{root}/configs/konfig.json")