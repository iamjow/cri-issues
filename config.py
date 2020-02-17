from requests.auth import HTTPBasicAuth

username = "jowin@qstrike.com"
token = "nH484g7DFwDAMUoRunufFC3D"

url_issue_link = "https://qstrike.atlassian.net/browse/"
auth = HTTPBasicAuth(username, token)

maxResult = 100
startAt = 0

cri_project_key = "CRI"
cco_project_key = "CCO"

server = "qstrike.atlassian.net"

# CRI
styleId = "customfield_10440"
fields = "fields=key,summary," + styleId + ",status,labels"
max_results = "maxResults={}".format(maxResult)
start_at = "startAt={}".format(startAt)
cri_url = "https://" + server + "/rest/api/2/search?jql=project=" + cri_project_key + "&" + fields + "&" + max_results + "&" + start_at + ""

cri_ws = "C:\\Users\\Public\\richardson_issues.xlsx"


# CCO
cco_url = "https://qstrike.atlassian.net/rest/api/3/search?jql=project=" + cco_project_key + ""

cco_ws = "C:\\Users\\Public\\prolook_issues.xlsx"


