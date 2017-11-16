import re
from subprocess import check_output


class FLEXLMReader(object):

    def __init__(self, path, port, server):
        """
        Construction
        """
        self._path = path
        self._port = port
        self._server = server

    def getInfo(self):
        try:
            result = {}
            flexlmpath = self._path + "\\lmutil.exe"
            flexlmresult = check_output(
                [
                    flexlmpath,
                    "lmstat",
                    "-a",
                    "-c",
                    "%s@%s" % (self._port, self._server)
                ])
            result = self._parseInfo(flexlmresult)
            return result
        except Exception as e:
            raise ValueError(e)

    def _parseInfo(self, flexlmresult):
        # Parse lmutil output
        licenseInfo = {}
        licenseType_re = re.compile(r"Users of(.*):.*(\d).*(\d)")
        userInfo_re = re.compile(r"^\s+(\S+) (\S+).*, start (.*)")
        lines = flexlmresult.splitlines()
        currentType = None
        for line in lines:
            # Get Line that shows License Type
            matchType = licenseType_re.match(line)
            if matchType:
                currentType = matchType.group(1)
                if currentType in licenseInfo:
                    # add number of 'inuse' and 'count'
                    licenseInfo[currentType][0][0] += int(matchType.group(3))
                    licenseInfo[currentType][0][1] += int(matchType.group(2))
                else:
                    licenseInfo[currentType] = [[int(matchType.group(3)),
                                                int(matchType.group(2))]]
            # Get Line that contains User Information
            matchUser = userInfo_re.match(line)
            if matchUser and currentType:
                # Extract User Information into variables
                user = "%s@%s" % (matchUser.group(1), matchUser.group(2))
                time = matchUser.group(3)
                licenseInfo[currentType].append([user, time])
        return licenseInfo
