from shop import Shop

my_shop = Shop("matteo","viale italia")
my_shop.load_rackets_from_file("input/padel-input.txt")

#print(my_shop.average_rackets_price())
my_shop.write_summary_on_file('output/result.txt')