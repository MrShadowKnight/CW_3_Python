import json

# new_list_product = []
with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

    # for i in products:
    #     # print(i['colors'])
    #     for color in i['colors']:
    #         if color.lower() == "чорний":
    #             new_list_product.append(i)
    # print(new_list_product)

    # for i in products:
    #     if "Чорний" in i['colors']:
    #         new_list_product.append(i)
    # print(new_list_product)

# some_err = [1, 1, 2, 3]
# unique_val = []
#
# for el in some_err:
#     # if el in unique_val:
#     #     continue
#     # else:
#     #     unique_val.append(el)
#     if el not in unique_val:
#         unique_val.append(el)
#     continue
# print(unique_val)
#     value_a = 0
#      for i in products:
#
#          for f in i['features']:
#              value_check = f['value']
#
#              if value_check == "А+":
#                  value_a += 1
#      print(value_a)

    # for item in products:
    #     with open(f"singl_products/{item['id']}.json", "w", encoding="cp1251") as file:
    #         json.dump(item, file)
    # id = int(input("Vvedit id produktu: "))
    # if 1 <= id <= 285:
    #     with open(f"singl_products/{id}.json", "r")as file:
    #         products = json.load(file)
    #         print(products)
    # else:
    #     print("Takoho id ne isnuye!")
    # top_list = []
    #for item in products:
        # max_price = 1
        # price = item["price"]
        #
        # price = price.replace(" ", '').replace(' ', '')
        #
        # price = int(price)
        # if max_price < price:
        #     max_price = price
        #     top_list.append(max_price)
        #     price.pop(max_price)
    print(products)

    prices =[]

    for item in products:
        product_price = int(item["price"].replace(" ", '').replace(' ', ''))
        prices.append(product_price)

    print(prices)

    abs_price = sorted(prices)
    print(abs_price)
    desc_price = sorted(prices, reverse=True)
    print(desc_price)

    for i in range(5):
        print(desc_price[i])