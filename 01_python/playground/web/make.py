
def make(str):
    return str if str[:8] == "https://" else "https://" + str
