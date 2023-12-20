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

    # lists for the zoom meetings per day
    mon_meets = []
    tues_meets = []

    # add more if necessary
    # wed_meets = []

    for row in range(1, df1.max_row):
        zoom_meet = ''
        zoom_time = ''
        for col in df1.iter_cols(1, df1.max_column):
            print(col[row].value)
            print(col_count)

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
                if col[row].value == 'M':
                    mon_meets.append(zoom_meet + '|' + str(zoom_time))
                elif col[row].value == 'T':
                    tues_meets.append(zoom_meet + '|' + str(zoom_time))

                # reset col_count
                col_count = 0

    week_meets = [mon_meets, tues_meets]
    join_meets(week_meets)


def join_meets(week_meets):

    # process monday meets
    for mon_meet in week_meets[0]:
        mon_meet_str = mon_meet.split("|")
        meet_time = mon_meet_str[1]
        meet_link = mon_meet_str[0]
        sc.every().monday.at(meet_time).do(open_meet, meet_link)

    # process tuesday meets
    for tues_meet in week_meets[1]:
        tues_meet_str = tues_meet.split("|")
        meet_time = tues_meet_str[1]
        meet_link = tues_meet_str[0]
        sc.every().tuesday.at(meet_time).do(open_meet, meet_link)

    # add more days if necessary

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
