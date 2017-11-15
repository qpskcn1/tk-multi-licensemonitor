import re
from subprocess import check_output


class RLMReader(object):

    def __init__(self, path, port, server, isv):
        """
        Construction
        """
        self._path = path
        self._port = port
        self._server = server
        self._isv = isv

    def getInfo(self):
        try:
            result = {}
            rlmpath = self._path + "\\rlmutil.exe"
            rlmresult = check_output(
                [
                    rlmpath,
                    "rlmstat",
                    "-c",
                    "%s@%s" % (self._port, self._server),
                    "-i",
                    self._isv,
                    "-a"
                ])
            result = self._parseInfo(rlmresult)
            return result
        except Exception as e:
            raise ValueError(e)

    def _parseInfo(self, rlmresult):
        licenseInfo = {}
        licenseType_re = re.compile(r"(nuke[^\s]+).*\n.*(count:)\s(\d).*(inuse:)\s(\d)")
        matchType = licenseType_re.finditer(rlmresult)
        if matchType:
            for t in matchType:
                if t.group(1) in licenseInfo:
                    # add number of 'inuse' and 'count'
                    licenseInfo[t.group(1)][0][0] += int(t.group(5))
                    licenseInfo[t.group(1)][0][1] += int(t.group(3))
                else:
                    licenseInfo[t.group(1)] = [[int(t.group(5)), int(t.group(3))]]

        userInfo_re = re.compile(r"(nuke[^\s]+).*:\s(.*@[^\s]+).*at\s([^\r]+)")
        matchUser = userInfo_re.finditer(rlmresult)
        if matchUser:
            for i in matchUser:
                if i.group(1) in licenseInfo:
                    licenseInfo[i.group(1)].append([i.group(2), i.group(3)])
        return licenseInfo
