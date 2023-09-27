from selenium.webdriver.common.by import By

class Sales:

    Sales_button_xpath = "//nav/ul/li/a/i[@class='nav-icon fas fa-shopping-cart']"
    Sales_item_xpath = "//ul/li/a[@href='/Admin/Order/List']"

    Start_Date_xpath = "//span[@aria-controls='StartDate_dateview']"
    select_Start_Date_xpath = "//tbody/tr/td/a[@data-value='2023/7/8']"

    End_Date_xpath = "//span[@aria-controls='EndDate_dateview']"
    select_End_Date_xpath = "//tbody/tr/td/a[@data-value='2023/7/10']"

    Warehouse_select_xpath = "//div/select[@id='WarehouseId']"
    Warehouse_select_all_xpath = "//select[@id='WarehouseId']/option[@selected='selected']"

    select_product_xpath = "//input[@id='search-product-name']"

    Order_Statuses_xpath = "//div/ul[@id='OrderStatusIds_taglist']"
    order_status_all_xpath = "//div/ul/li[text()='all']"
    order_status_pending_xpath = "//div/ul/li[text()='Pending']"
    order_status_processing_xpath = "//div/ul/li[text()='Processing']"
    order_status_complete_xpath = "//div/ul/li[text()='Complete']"
    order_status_cancelled_xpath = "//div/ul/li[text()='Cancelled']"

    Payment_Status_xpath = "//ul[@id='PaymentStatusIds_taglist']"
    Payment_Status_All_xpath = "//ul/li[text()='All']"
    Payment_Status_Pending_xpath = "//ul/li[text()='Pending']"
    Payment_Status_Authorized_xpath = "//ul/li[text()='Authorized']"
    Payment_Status_Paid_xpath = "//ul/li[text()='Paid']"
    Payment_Status_Partially_refunded_xpath = "//ul/li[text()='Partially refunded']"
    Payment_Status_Refunded_xpath = "//ul/li[text()='Refunded']"
    Payment_Status_Voided_xpath = "//ul/li[text()='Voided']"

    Shipping_statuses_Xpath = "//ul[@id='ShippingStatusIds_taglist']"
    Shipping_status_All_Xpath = "//ul/li[text()='All']"
    Shipping_status_Shipping_not_required_Xpath = "//ul/li[text()='Shipping not required']"
    Shipping_status_Not_yet_shipped_Xpath = "//ul/li[text()='Not yet shipped']"
    Shipping_status_Partially_shipped_Xpath = "//ul/li[text()='Partially shipped']"
    Shipping_status_Shipped_Xpath = "//ul/li[text()='Shipped']"
    Shipping_status_Delivered_Xpath = "//ul/li[text()='Delivered']"

    Vender_select_xpath = "//select[@name='VendorId']"
    vender2_select_xpath = "//select[@id='VendorId']//option[text()='Vendor 2']"
    