from requests.auth import HTTPBasicAuth

username = "jowin@qstrike.com"
token = "nH484g7DFwDAMUoRunufFC3D"
auth = HTTPBasicAuth(username, token)

maxResult = 100
startAt = 0

styleId = "customfield_10440"
server = "qstrike.atlassian.net"
project_key = "CRI"
fields = "fields=key,summary," + styleId + ",status,labels"
max_results = "maxResults={}".format(maxResult)
start_at = "startAt={}".format(startAt)
url = "https://" + server + "/rest/api/2/search?jql=project=" + project_key + "&" + fields + "&" + max_results + "&" + start_at + ""

url_issue_link = "https://qstrike.atlassian.net/browse/"

ws = "C:\\Users\\Public\\cri_issues.xlsx"



