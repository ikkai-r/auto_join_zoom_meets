import openpyxl as op
import webbrowser as wb

import schedule as sc
import time as t

# get the zoom meetings
dataframe = op.load_workbook("zoom_meets.xlsx")
df1 = dataframe.active


def process_meeting():
    # read the cols and rows
    col_count = 0

    for row in range(1, df1.max_row):
        zoom_meet = ''
        zoom_time = ''
        for col in df1.iter_cols(1, df1.max_column):

            # get zoom link for the row
            if col_count == 1:
                zoom_meet = col[row].value
            elif col_count == 2:
                zoom_time = col[row].value

            # start from 0 if next row
            if col_count < 3:
                col_count += 1
            else:
                # check what day the zoom meet occurs
                meet_days = str(col[row].value).split()

                for mdays in meet_days:
                    if mdays == 'M':
                        sc.every().monday.at(zoom_time).do(open_meet, zoom_meet)

                    if mdays == 'T':
                        sc.every().tuesday.at(zoom_time).do(open_meet, zoom_meet)

                    if mdays == 'Th':
                        sc.every().thursday.at(zoom_time).do(open_meet, zoom_meet)

                    if mdays == 'F':
                        sc.every().friday.at(zoom_time).do(open_meet, zoom_meet)

                # reset col_count
                col_count = 0

def open_meet(meet_link):
    wb.open(meet_link)


def main():
    process_meeting()
    while True:
        sc.run_pending()
        t.sleep(1)


if __name__ == "__main__":
    print('running...')
    main()
