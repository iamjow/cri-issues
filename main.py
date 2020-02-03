if __name__ == '__main__':
    from openpyxl import Workbook
    from modules import main_index
    import config
    import json
    import requests

    auth = config.auth
    url = config.url
    response = requests.request("GET", url, auth=auth)
    data_issues = json.loads(response.text)

    url_issue_link = config.url_issue_link

    worksheet = config.ws

    labels = []
    item_list1 = []
    item_list2 = []

    status = 'Done'

    id_style = config.styleId
    style_id = id_style

    workbook = Workbook()
    work_sheet1 = workbook.active
    work_sheet2 = workbook.create_sheet('Sheet1')

    def getMainIndexData():
        main_data = main_index.__fetchDataFromJira__(data_issues,
                                                     worksheet,
                                                     item_list1,
                                                     item_list2,
                                                     labels,
                                                     style_id,
                                                     status,
                                                     url_issue_link,
                                                     workbook,
                                                     work_sheet1,
                                                     work_sheet2)
        main_data.displayData()
        main_data.displayStyleSheet()

getMainIndexData()
