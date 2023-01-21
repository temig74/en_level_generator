import math

def get_olimpgrid_id(row_num, col_num, olimp_height):
    num = 0
    for j in range(1, col_num + 1):
        for i in range(1, 2**(olimp_height-1)+1):
            if (i-1) % (2**(j-1)) == 0:
                num += 1
            if i == row_num and j == col_num:
                return num


def generate_olimp_rows(olimp_height, row_pattern, level_number):
    start_elems_count = 2**(olimp_height-1)
    rows = ''
    for i in range(1, start_elems_count+1):
        rows += '<tr>'
        for j in range(1, olimp_height+1):
            if (i-1) % (2**(j-1)) == 0:
                sector_number = get_olimpgrid_id(i, j, olimp_height)
                rowspan = 2**(j-1)
                rows += row_pattern.replace('{level_number}', str(level_number)).replace('{sector_number}', str(sector_number)).replace('{rowspan}', str(rowspan))
        rows += '</tr>\n'
    return rows


def generate_img_table(img_count, olimp_prefix, level_num, game_id):
    html = '<table border="0">'
    square = math.ceil(math.sqrt(img_count))
    cnt = 0
    for i in range(1, square+1):
        html += '<tr>'
        for j in range(1, square+1):
            cnt += 1
            if cnt > img_count:
                break
            html += f'<td id="img_{level_num}_{cnt}"><img src = "https://d1.endata.cx/data/games/{game_id}/{olimp_prefix}_{cnt}.png"></td>'
        html += '</tr>'
    html += '</table>'
    return html

