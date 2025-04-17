from racket import Racket


class Shop(object):
    def __init__(self,name, address):
        if not isinstance(name, str):
            raise TypeError('name is not a string')
        if not isinstance(address, str):
            raise TypeError('address is not a string')
        self._name=name
        self._address=address
        self._racket_collection=[]

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    def load_rackets_from_file(self,path):
        if not isinstance(path, str):
            raise TypeError('path is not a string')
        #hard_coded_path="input/padel-input.txt"
        try:
            with open(path, 'r') as f:
                #print(f)
                content=f.read()
                #print(content)
                split_content=content.split("\n")
                print(split_content)
                elements_dict=dict()
                #print(type(content))
                #print(content)
                for line in split_content:
                 #   print(line)
                    if line=="***":
                        #ho terminato la lettura di una racchetta devo crearla
                        my_racket=Racket(elements_dict["brand"],elements_dict["model"],elements_dict["size"],int(elements_dict["weight"]),int(elements_dict["quantity"]),float(elements_dict["price_per_piece"]))
                        self._racket_collection.append(my_racket)
                    else:
                        split_line= line.split(":")
                        #print(split_line)
                        elements_dict[split_line[0]]=split_line[1].strip()
                       # print(elements_dict)
                print(self._racket_collection)
                print(len(self._racket_collection))
        except FileNotFoundError as e:
            print(e)

    def average_rackets_price(self):
        total_price=0
        total_rackets=0
        for racket in self._racket_collection:
            price=racket.price
            pieces=racket.quantity
            total_price+=price*pieces
            total_rackets+=pieces
        average=total_price/total_rackets
        return average

    def total_number_of_rackets(self): # contare tutte le racchette nella collezione
        total_number=0
        for racket in self._racket_collection:
            total_number+=racket.quantity
        return total_number

    # Scriviamo nel file nome del negozio, prezzo medio e quantità
    def write_summary_on_file(self, path):
        if not isinstance(path, str):
            raise TypeError('path is not a string')
        shop_name = self._name
        average_price = self.average_rackets_price()
        rackets_quantity = self.total_number_of_rackets()
        string_to_write = f'shop name: {shop_name}\naverage price: {average_price}\nrackets quantity: {rackets_quantity}'
        try:
            with open(path, 'w') as f:
                f.write(string_to_write)
        except Exception as e:
            print(e)
