import urllib.request
from bs4 import BeautifulSoup

#Requirement
# This script was developed on Python 3
#You have to install biutifulsoup library (pip install beautifulsoup4 )
# start the program in the console with python webscraping_samuel_guibin.py

#WEBCRAPING SCRIPT FOR WWW.EBAY.COM WITH SHOE DATA

brand = "PUMA" #Brand of the shoe | e.g PUMA, adidas, Nike, Crocs, Gucci
shoe_new = ["1000", "New shoe with box"] #code for new shoe with box
shoe_category = ["93427", "Men"] # Code for category for men is ["93427", "Men"] | code for category for women is ["3034","Women"]

url_webpage = "https://www.ebay.com/sch/" + shoe_category[0] + "/i.html?_from=R40_&Brand=" + brand + "&LH_ItemCondition=" + shoe_new[0]

########################PRINT OF THE INITIAL VALUES######################################
print("Shoe brand:", brand)
print("Shoe Condition:",shoe_new[1])
print("Shoe Category:",shoe_category[1])
print("URL of the Web:", url_webpage, "\n\n")

##########################################################################################

html_code = urllib.request.urlopen(url_webpage).read() #read the HTML of the url_webpage
soup = BeautifulSoup(html_code, "html.parser") #HTML as nested data structure

#number of result from the search
result_search_number = soup.findAll("h1",{"class" : "srp-controls__count-heading"})[0].text 
print(result_search_number, "found","\n\n")

##########################################################################################
number_of_products = 5 #how many items will be displayed
i = 0 #timer
product_name_list = [] #list of the name 
product_prize_list = [] #list of the price
product_shipping_list = [] #list of the shipping price
product_prize_final = [] #list of the final price (price of the product + shipping)

##########################################################################################
#function to extract the value of the price
def number_extract(amount_string):
    if amount_string.split()[1].isalpha():
        amount_value = "0"
    else:
        amount_value = amount_string.split()[1]
    return amount_value

#function to print the value of the shoes

def print_information(product_matrix, t_product):
    for j in range(0, t_product):
        print("PRODUCT: ",product_matrix[j][0])
        print("PRIZE: ", product_matrix[j][1])
        print("PRIZE SHIPPING: ", product_matrix[j][2])
        print("FINAL PRIZE: ", product_matrix[j][3],"\n\n")        

##########################################################################################
#the first (number_of_products) with their prices and print them in console 

print("LIST OF THE FIRST "+ number_of_products.__str__() + " PRODUCTS DISPLAYED")
print("----------------------------------------\n")
for products_EBAY in soup.findAll("li",{"class" : "s-item"}):
    if i < number_of_products:
        product_name_list.append(products_EBAY.findAll("h3", {"class" : "s-item__title"})[0].text) #save the name of the product in a list
        product_prize_list.append(products_EBAY.findAll("span",{"class" : "s-item__price"})[0].text) #save the value of the prize in a list 
        product_shipping_list.append(products_EBAY.findAll("span",{"class" : "s-item__shipping s-item__logisticsCost"})[0].text) #save the value of the prize shipping in a list
        product_prize_final.append((round(float(number_extract(product_prize_list[i])) + float(number_extract(product_shipping_list[i])),2)).__str__()) #save the value of the product (price + shipping)
        
        print("PRODUCT: ", product_name_list[i])
        print("PRIZE: ", product_prize_list[i])
        print("PRIZE SHIPPING: ", product_shipping_list[i])
        print("FINAL PRIZE: ", product_prize_final[i],"\n\n")  
        
        i+=1
    else:
        break

##########################################################################################

matrix_of_product_price = list(zip(product_name_list, product_prize_list, product_shipping_list,product_prize_final)) #Matrix with all results

##########################################################################################
#Order by price (ascendant)

matrix_of_product_price.sort(key = lambda names : names[3]) #list sorted by final price (ascendant)

print("LIST SORTED BY FINAL PRICE")
print("-------------------\n")

print_information(matrix_of_product_price,i)

##########################################################################################
#Order and print the products by name (ascendant)

matrix_of_product_price.sort(key = lambda names : names[0]) #list sorted by name

print("LIST SORTED BY NAME")
print("----------------------------\n")

print_information(matrix_of_product_price,i)

##########################################################################################
#Order and print the products by price in descendant mode

matrix_of_product_price.sort(key = lambda names : names[3], reverse=True)


print("LIST SORTED BY FINAL PRICE (DESCENDANT)") #list sorted by final price (descendant)
print("-----------------------------------\n")

print_information(matrix_of_product_price,i)