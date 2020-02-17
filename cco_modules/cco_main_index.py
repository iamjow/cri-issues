from pprint import pprint
from styles import sheet_style as style


class __fetchCCOIssues__(object):
    def __init__(self, cco_data_issues, cco_workbook, cco_worksheet, cco_work_sheet1, cco_work_sheet2):
        self.cco_data_issues = cco_data_issues
        self.cco_workbook = cco_workbook
        self.cco_worksheet = cco_worksheet
        self.cco_work_sheet1 = cco_work_sheet1
        self.cco_work_sheet2 = cco_work_sheet2

    def displayData(self):
        for idx, item in enumerate(self.cco_data_issues['issues']):
            filtered_label = (item['fields']['labels'])
            pprint(filtered_label)

    def displayStyleSheet(self):
        header_width = [
            self.cco_work_sheet1.column_dimensions["D"],
            self.cco_work_sheet1.column_dimensions["E"],
            self.cco_work_sheet1.column_dimensions["E"],
            self.cco_work_sheet1.column_dimensions["E"],
            self.cco_work_sheet1.column_dimensions["E"],
            self.cco_work_sheet1.column_dimensions["E"],
            self.cco_work_sheet1.column_dimensions["F"],
            self.cco_work_sheet1.column_dimensions["G"],
            self.cco_work_sheet1.column_dimensions["H"],
            self.cco_work_sheet1.column_dimensions["I"],
            self.cco_work_sheet1.column_dimensions["J"],
            self.cco_work_sheet1.column_dimensions["K"],
            self.cco_work_sheet1.column_dimensions["L"],
            self.cco_work_sheet1.column_dimensions["M"],
            self.cco_work_sheet1.column_dimensions["N"],
            self.cco_work_sheet1.column_dimensions["O"],
            self.cco_work_sheet1.column_dimensions["P"],
            self.cco_work_sheet1.column_dimensions["Q"],
            self.cco_work_sheet1.column_dimensions["R"],
            self.cco_work_sheet1.column_dimensions["S"],
            self.cco_work_sheet1.column_dimensions["T"],
            self.cco_work_sheet1.column_dimensions["U"],
            self.cco_work_sheet1.column_dimensions["V"],
            self.cco_work_sheet1.column_dimensions["W"],
            self.cco_work_sheet1.column_dimensions["X"],
        ]

        for cell in header_width:
            cell.width = 5

        self.cco_work_sheet1.column_dimensions['c'].width = 50
        self.cco_work_sheet1.column_dimensions['a'].width = 15
        self.cco_work_sheet1.column_dimensions['z'].width = 15

        self.cco_work_sheet2.column_dimensions['c'].width = 50
        self.cco_work_sheet2.column_dimensions['a'].width = 15
        self.cco_work_sheet2.column_dimensions['d'].width = 15

        self.cco_work_sheet1.cell(row=1, column=1).value = 'PROLOOK ISSUES'
        self.cco_work_sheet1.cell(row=1, column=1).font = style.header_main_title

        self.cco_work_sheet2.cell(row=1, column=1).value = 'SUB ISSUES'
        self.cco_work_sheet2.cell(row=1, column=1).font = style.header_main_title

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
        self.cco_work_sheet1.append(list1_header_title)

        for cell in self.cco_work_sheet1["2:2"]:
            cell.font = style.header_font_style
            cell.alignment = style.header_font_alignment

        self.cco_workbook.save(self.cco_worksheet)







