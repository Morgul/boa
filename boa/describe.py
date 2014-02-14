from suite import Suite

indent = 0

def describe(description):
    global indent

    suite = Suite(description, indent)
    indent += 2
    return suite
