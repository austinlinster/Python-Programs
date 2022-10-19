#Jonathan Zhou jaz978
#Homework 5
#October 11th, 2022
#MultiNational Operations Program to store and analyze sales data

#function to request country name and validate length
def request_countryname():
    country = input("Please enter the country's name: ")
    while len(country) < 2:
        country = input("Please enter the country's name: ")
    return country

#function to request sales for a given product type and country name and additionally validate sales number is numeric and non-negative
def request_sales(product_type, country):
    sales = input(f'Please enter the total sales for {product_type} in {country}: ')
    check = True
    while check:
        if sales.isnumeric() is False:
            sales = input(f'Please enter a numeric non-negative number for the total sales for {product_type} in {country}: ')
        elif float(sales) < 0:
            sales = input(f'Please enter a numeric non-negative number for the total sales for {product_type} in {country}: ')
        else:
            check = False
    return sales

#utilize request_countryname() and request_sales() to request software, hardware, and accessories sales information by the country
def request_data(file_name):
    checker = True
    count = 0
    program_file = open(file_name, 'w')
    while checker:
        country_input = request_countryname()
        program_file.write(f'{country_input} \n')
        software_input = request_sales("software", country_input)
        program_file.write(f'{software_input} \n')
        hardware_input = request_sales("hardware", country_input)
        program_file.write(f'{hardware_input} \n')
        accessories_input = request_sales("accessories", country_input)
        program_file.write(f'{accessories_input} \n')
        count += 1
        another = input('Do you want to enter data for another country? (Enter y/Y for Yes, any other key to stop) ').upper()
        if another != "Y":
            checker = False
    print(f'{count} record(s) were successfully added to file.')

#function to analyze the received data and calculate and display averages and totals
def analyze_data(file_name):
    count = 0
    line = file_name.readline()
    software_total = 0
    hardware_total = 0
    accessories_total = 0
    while line != '':
        software_total += float(file_name.readline())
        hardware_total += float(file_name.readline())
        accessories_total += float(file_name.readline())
        count += 1
        line = file_name.readline()
    average_software = software_total / count
    average_hardware = hardware_total / count
    average_accessories = accessories_total / count
    total_sales = software_total + hardware_total + accessories_total
    print(f'Average software sales per country: ${average_software:,.2f}')
    print(f'Average hardware sales per country: ${average_hardware:,.2f}')
    print(f'Average accessories sales per country: ${average_accessories:,.2f} \n')
    print(f'Total software sales: ${software_total:,.2f}')
    print(f'Total hardware sales: ${hardware_total:,.2f}')
    print(f'Total accessories sales: ${accessories_total:,.2f} \n')
    print(f'Total Sales: ${total_sales:,.2f}')

#function to request and analyze and display data
def main():
    request_data("sales_data.txt")
    analyze_data(open("sales_data.txt", 'r'))

# main()
gita = get_grade('examin')
print(gita)


