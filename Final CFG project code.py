import csv


# Opening the CSV file


def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def run():
    data = read_data()

    # put all empty lists here
    # Creating empty lists to store data for later:
    month_year_list = []  # empty array to append months
    sale_list = []  # empty list to append sales
    expenditure_list = []  # empty list to append expenditure
    tot_list = []  # empty list to append sales totals
    tot_list2 = []  # empty list to append expenditure totals
    avg_list = []  # empty list to append averages
    max_list = []  # empty list to append max values
    min_list = []  # empty list to append min values
    per_change_list = []  # empty list to append percentage changes to

    # for loop for calculations for each month (x12), runs through all months one after another:
    for row in data:
        # Current month:
        month_year_list.append([row['month'], row['year']])

        # appending total sales in each month:
        sale = int(row['sales'])
        sale_list.append(sale)

        # calculating totals for each month:
        total = sum(sale_list)
        tot_list.append(total)

        # calculating the average sales from beginning to current month:
        avg_sales = int(total / len(sale_list))
        avg_list.append(avg_sales)

        # calculating the max and min sales as of current month:
        current_max = max(sale_list)
        max_list.append(current_max)
        current_min = min(sale_list)
        min_list.append(current_min)

        # calculating the total expenditure in each month:
        expenditure = int(row['expenditure'])
        expenditure_list.append(expenditure)
        total2 = sum(expenditure_list)
        tot_list2.append(total2)

    # end of running through each month

    # % sales
    # changing sale_list strings to int for calculations
    # calculations
    for i in range(0, len(sale_list), 12):
        rel_data1 = sale_list[i:i + 12]
        for j in range(0, len(rel_data1) - 1):
            per_change_list.append(((rel_data1[j + 1] - rel_data1[j]) / rel_data1[j]) * 100)

    # Total annual % change, ignores months not in completed year
    total_annual = []
    for i in range(0, len(per_change_list), 11):
        rel_data = per_change_list[i:i + 11]
        total_annual.append(sum(rel_data) / len(rel_data))
    # print(total_annual)

    # Total Avg Sales out of 12 for loop -- for calc purposes
    tot_avg_sales = []
    for i in range(0, len(sale_list), 12):
        rel_data2 = sale_list[i:i + 12]
        tot_avg_sales.append(sum(rel_data2) / len(rel_data2))
    # print(tot_avg_sales)  # -- should be 3795.16

    # Total Annual Forecast Sales
    total_forecast = []
    for (item1, item2) in zip(tot_avg_sales, total_annual):
        total_forecast.append(int(((item1 / 100) * item2) + item1))
    # print(total_forecast)  # -- should be 4360.84

    # user inputs for time frame:
    print("Available months and years:")
    for row in data:
        print(row['month'], row['year'])
    start = [input("Start month:"), input("Start year:")]
    if start not in month_year_list:
        print("ERROR: Start month or year not recognised. Please choose from list of available months and years.")
        run()
    end = [input("End month:"), input("End year:")]
    if end not in month_year_list:
        print("ERROR: End month or year not recognised. Please choose from list of available months and years.")
        run()

    # array of available analytics:
    analytics = ['1: monthly sales',
                 '2: total sales by month',
                 '3: average sales by month',
                 '4: maximum sales by month',
                 '5: minimum sales by month',
                 '6: total expenditure by month',
                 '7: overall total sales',
                 '8: overall average sales',
                 '9: overall maximum sales',
                 '10: overall minimum sales',
                 '11: overall total expenditure']

    # user inputs for analytics:
    print("Available analytics:")
    for index in analytics:
        print(index)
    first_input = int(input('Please enter the number of one of the desired analytics:'))
    if first_input not in range(1, len(analytics) + 1):
        print('ERROR: this number is not related to any of the available analytics')
        run()
    analytics_input_list = [first_input]  # list to append inputted numbers
    i = 0  # initializing i
    while i == 0:
        more_inputs = input('More analytics? y/n:')
        if more_inputs == 'y':
            new_input = int(input('Please enter the number of one of the desired analytics:'))
            if new_input not in range(1, len(analytics) + 1):
                print('ERROR: this number is not related to any of the available analytics')
                run()
            if new_input in analytics_input_list:
                print('This number is already selected')
            analytics_input_list.append(new_input)
        elif more_inputs == 'n':
            i = 1
        else:
            print('Please enter y or n')

    # generate relevant start and end index:
    start_index = month_year_list.index(start)
    end_index = month_year_list.index(end)

    # Print values for each month in given time frame:
    for index in range(start_index, end_index + 1):
        if 1 in analytics_input_list:
            print('Number of sales in {} {}: {}'.format(month_year_list[index][0], month_year_list[index][1],
                                                        sale_list[index]))
        if 2 in analytics_input_list:
            print('The total number of sales by {} {}: {}'.format(month_year_list[index][0], month_year_list[index][1],
                                                                  tot_list[index]))
        if 3 in analytics_input_list:
            print('Average sales by {} {}: {}'.format(month_year_list[index][0], month_year_list[index][1],
                                                      avg_list[index]))
        if 4 in analytics_input_list:
            print(
                'The maximum number of sales by {} {}: {}'.format(month_year_list[index][0], month_year_list[index][1],
                                                                  max_list[index]))
        if 5 in analytics_input_list:
            print(
                'The minimum number of sales by {} {}: {}'.format(month_year_list[index][0], month_year_list[index][1],
                                                                  min_list[index]))
        if 6 in analytics_input_list:
            print('The total expenditure by {} {}: £{}'.format(month_year_list[index][0], month_year_list[index][1],
                                                               tot_list2[index]))

    # Print total values over all data:
    if 7 in analytics_input_list:
        tot_sales = tot_list[-1]
        print('The overall total sales: {}'.format(tot_sales))
    if 8 in analytics_input_list:
        tot_avg = avg_list[-1]
        print('The overall average in sales: {}'.format(tot_avg))
    if 9 in analytics_input_list:
        tot_max = max_list[-1]
        print('The overall maximum sales per month: {}'.format(tot_max))
    if 10 in analytics_input_list:
        tot_min = min_list[-1]
        print('The overall minimum sales per month: {}'.format(tot_min))
    if 11 in analytics_input_list:
        tot_expenditure = tot_list2[-1]  # -- Phoebe Edits
        print('The overall total expenditure: £{}'.format(tot_expenditure))

    yn_list = ['y', 'n']  # for error checking - forecast input
    ynforecast = input("Do you want to forecast the average sales for a month based on previous data? y/n:")
    if ynforecast == 'y':
        print("Data available for:")
        for i in range(len(month_year_list)):
            if month_year_list[i - 1][1] != month_year_list[i][1]:
                print(month_year_list[i][1])
        year = int(input("what year do you want to use for the forecasting?:"))
        print('£', total_forecast[year - int(month_year_list[0][1])])
    elif ynforecast not in yn_list:
        print("ERROR: please enter y or n")


run()
