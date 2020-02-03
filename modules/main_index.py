from pprint import pprint
from pydash import py_
from modules import sheet_style as style


class __fetchDataFromJira__(object):
    def __init__(self,
                 data_issues,
                 worksheet,
                 item_list1,
                 item_list2,
                 labels,
                 style_id,
                 status,
                 url_issue_link,
                 workbook,
                 work_sheet1,
                 worksheet2):
        self.data_issues = data_issues
        self.worksheet = worksheet
        self.list1 = item_list1
        self.labels = labels
        self.style_id = style_id
        self.list2 = item_list2
        self.status = status
        self.issue_link = url_issue_link
        self.workbook = workbook
        self.work_sheet1 = work_sheet1
        self.work_sheet2 = worksheet2

    def displayData(self):
        for idx, item in enumerate(self.data_issues['issues']):
            pprint(idx)
            filteredLabel = (item['fields']['labels'])
            filteredSummary = (item['fields']['summary'])
            filteredStyleId = (item['fields'][self.style_id])
            filteredKey = (item['key'])
            filteredStatus = (item['fields']['status']['name'])

            colors_issue_count = 0
            fabrics_issue_count = 0
            pipings_issue_count = 0
            team_name_issue_count = 0
            player_number_issue_count = 0
            player_name_issue_count = 0
            logos_issue_count = 0
            brand_issue_count = 0
            team_roster_issue_count = 0
            application_sizing_issue_count = 0
            pdf_issue_count = 0
            preview_thumbnail_issue_count = 0
            view_summary_issue_count = 0
            scroll_button_issue_count = 0
            server_issue_count = 0
            saved_design_issue_count = 0
            custom_scale_issue_count = 0
            browser_issue_count = 0
            page_issue_count = 0
            tooltip_issue_count = 0
            bounding_box_issue_count = 0

            if filteredLabel:
                if filteredLabel[0] == 'colors':
                    colors_issue_count += 1

                if filteredLabel[0] == 'fabrics':
                    fabrics_issue_count += 1

                if filteredLabel[0] == 'pipings':
                    pipings_issue_count += 1

                if filteredLabel[0] == 'team_name':
                    team_name_issue_count += 1

                if filteredLabel[0] == 'player_number':
                    player_number_issue_count += 1

                if filteredLabel[0] == 'player_name':
                    player_name_issue_count += 1

                if filteredLabel[0] == 'logos':
                    logos_issue_count += 1

                if filteredLabel[0] == 'brand':
                    brand_issue_count += 1

                if filteredLabel[0] == 'team_roster':
                    team_roster_issue_count += 1

                if filteredLabel[0] == 'application_sizing':
                    application_sizing_issue_count += 1

                if filteredLabel[0] == 'pdf':
                    pdf_issue_count += 1

                if filteredLabel[0] == 'preview_thumbnail':
                    preview_thumbnail_issue_count += 1

                if filteredLabel[0] == 'view_summary':
                    view_summary_issue_count += 1

                if filteredLabel[0] == 'scroll_button':
                    scroll_button_issue_count += 1

                if filteredLabel[0] == 'server':
                    server_issue_count += 1

                if filteredLabel[0] == 'saved_design':
                    saved_design_issue_count += 1

                if filteredLabel[0] == 'custom_scale':
                    custom_scale_issue_count += 1

                if filteredLabel[0] == 'browser':
                    browser_issue_count += 1

                if filteredLabel[0] == 'page':
                    page_issue_count += 1

                if filteredLabel[0] == 'tooltip':
                    tooltip_issue_count += 1

                if filteredLabel[0] == 'bounding_box':
                    bounding_box_issue_count += 1

            if filteredStatus == self.status:
                fabrics_issue_count -= 1
                colors_issue_count -= 1
                pipings_issue_count -= 1
                team_name_issue_count -= 1
                player_number_issue_count -= 1
                player_name_issue_count -= 1
                logos_issue_count -= 1
                brand_issue_count -= 1
                team_roster_issue_count -= 1
                application_sizing_issue_count -= 1
                pdf_issue_count -= 1
                preview_thumbnail_issue_count -= 1
                view_summary_issue_count -= 1
                scroll_button_issue_count -= 1
                server_issue_count -= 1
                saved_design_issue_count -= 1
                custom_scale_issue_count -= 1
                browser_issue_count -= 1
                page_issue_count -= 1
                tooltip_issue_count -= 1
                bounding_box_issue_count -= 1

            if filteredStatus:
                filter_stat = filteredStatus

            if filteredKey:
                key_issue = filteredKey

            if filteredSummary:
                summary_issue = filteredSummary

            if filteredStyleId:
                style_id = filteredStyleId
                pprint('Style ID Processing...' + style_id)

                stat = filter_stat if filter_stat == self.status else filter_stat

                obj = {
                    'summary': summary_issue,
                    'item_id': style_id,
                    'fabrics': fabrics_issue_count if fabrics_issue_count >= 1 else 0,
                    'colors': colors_issue_count if colors_issue_count >= 1 else 0,
                    'pipings': pipings_issue_count if pipings_issue_count >= 1 else 0,
                    'team_name': team_name_issue_count if team_name_issue_count >= 1 else 0,
                    'player_number': player_number_issue_count if player_number_issue_count >= 1 else 0,
                    'player_name': player_name_issue_count if player_name_issue_count >= 1 else 0,
                    'logos': logos_issue_count if logos_issue_count >= 1 else 0,
                    'brand': brand_issue_count if brand_issue_count >= 1 else 0,
                    'team_roster': team_roster_issue_count if team_roster_issue_count >= 1 else 0,
                    'application_sizing': application_sizing_issue_count if application_sizing_issue_count >= 1 else 0,
                    'pdf': pdf_issue_count if pdf_issue_count >= 1 else 0,
                    'preview_thumbnail': preview_thumbnail_issue_count if preview_thumbnail_issue_count >= 1 else 0,
                    'view_summary': view_summary_issue_count if view_summary_issue_count >= 1 else 0,
                    'scroll_button': scroll_button_issue_count if scroll_button_issue_count >= 1 else 0,
                    'server': server_issue_count if server_issue_count >= 1 else 0,
                    'saved_design': saved_design_issue_count if saved_design_issue_count >= 1 else 0,
                    'custom_scale': custom_scale_issue_count if custom_scale_issue_count >= 1 else 0,
                    'browser': browser_issue_count if browser_issue_count >= 1 else 0,
                    'page': page_issue_count if page_issue_count >= 1 else 0,
                    'tooltip': tooltip_issue_count if tooltip_issue_count >= 1 else 0,
                    'bounding_box': bounding_box_issue_count if bounding_box_issue_count >= 1 else 0,
                    'issue_link': self.issue_link + key_issue,
                    'key_issue': key_issue,
                    'status': stat
                }

                if not self.list1:
                    self.list1.append(obj)
                    pprint('Recent adding' + ' ' + style_id)
                else:
                    filtered = py_.filter(self.list1, lambda x: x['item_id'] == style_id)

                    if len(filtered) == 0:
                        pprint(f'Adding...{style_id} - {filteredStatus} ')
                        self.list1.append(obj)
                    else:
                        pprint(f'Not adding... {style_id} - {filteredStatus}')

                        if filter_stat != self.status:
                            filtered[0][filteredLabel[0]] = int(filtered[0][filteredLabel[0]]) + 1

                        sub_issue = obj
                        self.list2.append(sub_issue)

            else:
                # pprint('No ID attached')
                self.labels.append('No ID')

            if filteredLabel:
                self.labels.append(filteredLabel[0])

    def displayStyleSheet(self):
        self.workbook
        self.work_sheet1
        self.work_sheet2

        header_width = [
            self.work_sheet1.column_dimensions["D"],
            self.work_sheet1.column_dimensions["E"],
            self.work_sheet1.column_dimensions["F"],
            self.work_sheet1.column_dimensions["G"],
            self.work_sheet1.column_dimensions["H"],
            self.work_sheet1.column_dimensions["I"],
            self.work_sheet1.column_dimensions["J"],
            self.work_sheet1.column_dimensions["K"],
            self.work_sheet1.column_dimensions["L"],
            self.work_sheet1.column_dimensions["M"],
            self.work_sheet1.column_dimensions["N"],
            self.work_sheet1.column_dimensions["O"],
            self.work_sheet1.column_dimensions["P"],
            self.work_sheet1.column_dimensions["Q"],
            self.work_sheet1.column_dimensions["R"],
            self.work_sheet1.column_dimensions["S"],
            self.work_sheet1.column_dimensions["T"],
            self.work_sheet1.column_dimensions["U"],
            self.work_sheet1.column_dimensions["V"],
            self.work_sheet1.column_dimensions["W"],
            self.work_sheet1.column_dimensions["X"],
        ]

        for cell in header_width:
            cell.width = 5

        self.work_sheet1.column_dimensions['c'].width = 50
        self.work_sheet1.column_dimensions['a'].width = 15
        self.work_sheet1.column_dimensions['z'].width = 15

        self.work_sheet2.column_dimensions['c'].width = 50
        self.work_sheet2.column_dimensions['a'].width = 15
        self.work_sheet2.column_dimensions['d'].width = 15

        self.work_sheet1.cell(row=1, column=1).value = 'ISSUES'
        self.work_sheet1.cell(row=1, column=1).font = style.header_main_title

        self.work_sheet2.cell(row=1, column=1).value = 'SUB ISSUES'
        self.work_sheet2.cell(row=1, column=1).font = style.header_main_title

        list1_header_title = [
            'KEY ISSUE',
            'STYLE ID',
            'SUMMARY',
            'COLORS',
            'FABRICS',
            'PIPINGS',
            'TEAM NAME',
            'PLAYER NUMBER',
            'PLAYER NAME',
            'LOGOS',
            'BRAND',
            'TEAM ROSTER',
            'APPLICATION SIZING',
            'PDF',
            'PREVIEW THUMBNAIL',
            'VIEW SUMMARY',
            'SCROLL BUTTON',
            'SERVER',
            'SAVED DESIGN',
            'CUSTOM SCALE',
            'BROWSER',
            'PAGE',
            'POP-UP/TOOLTIP',
            'BOUNDING BOX',
            '',
            'STATUS'
        ]
        self.work_sheet1.append(list1_header_title)

        for cell in self.work_sheet1["2:2"]:
            cell.font = style.header_font_style
            cell.alignment = style.header_font_alignment

        if self.list1:
            a3 = 3
            z3 = 3
            for index, lists1 in enumerate(self.list1):
                self.work_sheet1.append(
                    [
                        lists1['key_issue'],
                        lists1['item_id'],
                        lists1['summary'],
                        lists1['colors'],
                        lists1['fabrics'],
                        lists1['pipings'],
                        lists1['team_name'],
                        lists1['player_number'],
                        lists1['player_name'],
                        lists1['logos'],
                        lists1['brand'],
                        lists1['team_roster'],
                        lists1['application_sizing'],
                        lists1['pdf'],
                        lists1['preview_thumbnail'],
                        lists1['view_summary'],
                        lists1['scroll_button'],
                        lists1['server'],
                        lists1['saved_design'],
                        lists1['custom_scale'],
                        lists1['browser'],
                        lists1['page'],
                        lists1['tooltip'],
                        lists1['bounding_box']
                    ]
                )
                self.work_sheet1['Z{}'.format(z3)] = lists1['status']
                self.work_sheet1['A{}'.format(a3)].hyperlink = lists1['issue_link']
                self.work_sheet1['A{}'.format(a3)].value = lists1['key_issue']
                self.work_sheet1['A{}'.format(a3)].style = "Hyperlink"
                self.work_sheet1['A{}'.format(a3)].alignment = style.indent
                a3 += 1
                z3 += 1

                pprint(f'List1 {index} ' + lists1['item_id'])

        pprint('-------------')
        list2_header_title = [
            'KEY ISSUE',
            'STYLE ID',
            'SUMMARY',
            'LINK'
        ]
        self.work_sheet2.append(list2_header_title)

        for cell in self.work_sheet2["2:2"]:
            cell.font = style.header_font_style

        if self.list2:
            a3 = 3
            d3 = 3
            for index, lists2 in enumerate(self.list2):
                self.work_sheet2.append(
                    [
                        lists2['key_issue'],
                        lists2['item_id'],
                        lists2['summary'],
                    ]
                )
                self.work_sheet2['D{}'.format(d3)].hyperlink = lists2['status']
                self.work_sheet2['A{}'.format(a3)].hyperlink = lists2['issue_link']
                self.work_sheet2['A{}'.format(a3)].value = lists2['key_issue']
                self.work_sheet2['A{}'.format(a3)].style = "Hyperlink"
                a3 += 1
                d3 += 1

                pprint(f'List2 {index} ' + lists2['item_id'])

        self.workbook.save(self.worksheet)
