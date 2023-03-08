import sqlite3

c = sqlite3.connect('a2creations\spiders\page1.db')
cursor = c.cursor()


cursor.execute("SELECT PRODUCT_NAME, PRICES FROM PAGE1 ORDER BY PRICES DESC LIMIT 1;")
most_expensive = cursor.fetchone()

cursor.execute("SELECT PRODUCT_NAME, PRICES FROM PAGE1 WHERE PRICES > 0 ORDER BY PRICES ASC LIMIT 1")
cheapest = cursor.fetchone()

most_expensive_name, most_expensive_price = most_expensive
cheapest_name, cheapest_price = cheapest

cursor.execute('SELECT BRAND, COUNT(*) FROM PAGE1 GROUP BY BRAND')
brand_prodcuts = cursor.fetchall()

cursor.execute('SELECT SELLER, COUNT(*) FROM PAGE1 GROUP BY SELLER')
seller_products_no = cursor.fetchall()

print("\nANALYSIS OF THE DATA\n")
print(f"The most expensive product is {most_expensive_name} with a price of {most_expensive_price}.")
print(f"\nThe cheapest product is {cheapest_name} with a price of {cheapest_price}.")
print("\nNumber of products by brand:")
for result in brand_prodcuts:
    print(f"{result[0]}: {result[1]}")
print("\nNumber of products by seller:")
for result in seller_products_no:
    print(f"{result[0]}: {result[1]}")
c.close()
