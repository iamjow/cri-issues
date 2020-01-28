from openpyxl.styles import Font, colors, Alignment, Border, Side

header_font_style = Font(
    color='00FF0000',
    italic=False,
    bold=True)

header_font_alignment = Alignment(
    vertical="center",
    text_rotation=180,
    wrap_text=True,
    indent=1,
    shrink_to_fit=True)

header_main_title = Font(
    color=colors.BLACK,
    size=15,
    italic=True,
    bold=True)

indent = Alignment(indent=1)

