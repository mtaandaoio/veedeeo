outputPath = "out/"


# Takes in data and returns a string representing that data
def parseOutput(output):
    nbCacheServers = len(output)
    string = str(nbCacheServers) + "\n"
    for cacheServer, videos in output.items():
        string += str(cacheServer)
        for video in videos:
            string += " " + str(video)
        string += "\n"
    return string


def parseOutputs(outputs):
    for name, output in outputs.items():
        file = open(outputPath + name + ".out", "w")
        file.write(parseOutput(output))
        file.close()