import requests

with open('toMatch.txt') as f:
    s = " ".join([x.strip() for x in f])

s = s.split()
ContestId = "1335"
LIM = 1
pref = "https://codeforces.com/contest/" + ContestId

myset = set()


def check(code, patt):
    l1 = len(code)
    l2 = len(patt)
    if l1 < l2:
        return False
    for i in range(len(patt)):
        if code[i] != patt[i]:
            return False
    return True


submissionIds = set()

def checkSubmission(submissionId):
    if submissionId in submissionIds:
        return False
    submissionIds.add(submissionId)
    Url = pref + "/submission/" + submissionId
    resp = requests.get(Url).text
    i = resp.find("href=\"/profile/")
    if i == -1:
        return
    j = resp.find("\"", i+len("href=\"/profile/"))
    if j == -1:
        return
    userName = resp[i+len("href=\"/profile/"):j]
    if userName in myset:
        return
    i = resp.find("<pre id=\"program-source-text\"")
    if i == -1:
        return
    k = resp.find("style=\"padding: 0.5em;\">", i)
    if k == -1:
        return
    l = k + len("style=\"padding: 0.5em;\">")
    if l == -1:
        return
    m = resp.find("</pre>", l)
    if m == -1:
        return
    code = resp[l:m]
    code = code.replace('\n', ' ').replace('\r', '')
    code = code.split()
    if check(code, s):
        print(userName)
        myset.add(userName)


for i in range(LIM):
    try:
        Url = pref + "/status/page/" + str(i + 1) + "?order=BY_JUDGED_DESC"
        resp = requests.get(Url).text
        i = 0
        while True:
            i = resp.find("<tr data-submission-id=\"", i)
            if i == -1:
                break
            k = i + len("<tr data-submission-id=\"")
            if k == -1:
                break
            j = resp.find("\"", k)
            if j == -1:
                break
            print(resp[k:j])
            checkSubmission(resp[k:j])
            i = j
    except:
        print("Error\n")
