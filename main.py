import matplotlib.pyplot as plt
import django


print("This is a simple tool to help you keep track of you company's sales metrics. Let's get started.")

while True:
    srev = input("Would you like to calculate sales revenue: yes or no? ")
    if srev == "yes":
        print("SALES REVENUE")
        sr = float(input("Number of units sold or number of customers: "))
        sr2 = float(input("Average price per unit (product or service): $ "))
        sr3 = sr * sr2
        print("Sales Revenue = $",(sr3))
        continue
    elif srev == "no":
        while True:
            q = input("What would you like to calculate? \nEnter npm for Net Profit Margin \nEnter gm for Gross Margin \nEnter cac for Customer Acquisition Cost \nEnter sgytd for Sales Growth YTD \nEnter clr for Customer Loyalty & Retention \nEnter nps for Net Promoter Score \nEnter ltcr for Lead-to-Client Conversion Rate \nResponse: ")
            if q == "npm":
                print("NET PROFIT MARGIN")
                np = float(input("Total Sales Revenue: $ "))
                np2 = float(input("Costs: $ "))
                np3 = np - np2 / np
                print("Net Profit Margin = $ ", np3)
                break #continue
            elif q == "gm":
                print("GROSS MARGIN")
                gm = float(input("Total Revenue: $ "))
                gm2 = float(input("Cost of goods sold: $ "))
                gm3 = gm - gm2 / gm
                print("Gross Margin = $ ", gm3)
                break
            elif q == "cac":
                print("CUSTOMER ACQUISITION COST")
                cac = float(input("Cost of sales: $ "))
                cac2 = float(input("Cost of marketing: $ "))
                cac3 = float(input("New customers acquired: "))
                cac4 = (cac + cac2) / cac3
                print("Customer acquisition cost = $ ", cac4)
                break
            elif q == "clr":
                print("CUSTOMER LOYALTY & RETENTION") #Retention Rate = ((CE-CN)/CS)) X 100
                ec = float(input("Number of customers at the end of time period: "))
                nc = float(input("Number of new customers acquired during the same time period: "))
                sc = float(input("Number of customers at the start of the time period: "))
                rr = ((ec - nc) / sc) * 100
                print("Customer retention rate = ", rr,"%")
                break
            else:
                print("Please try again.")
    else:
        print("Please try again.")



#Year-over-year Growth = [(This Year – Last Year) / Last Year] X 100








