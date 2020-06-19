from data_classes.databse_file_handlers.smartphone import SmartPhone
from random import randint
import pickle

smart_phone1 = SmartPhone("Samsung", "A50", 500,
                          "Taiwan", "Samsung INC", randint(1, 100000000), [])
smart_phone2 = SmartPhone("Nokia", "3310", 130, "Finland",
                          "Nokia INC", randint(1, 100000000), [])
smart_phone3 = SmartPhone("Apple", "Iphone 7s", 500,
                          "China", "Apple INC", randint(1, 100000000), [])
smart_phone4 = SmartPhone("Apple", "Iphone X", 800,
                          "China", "Apple INC", randint(1, 100000000), [])
smart_phone5 = SmartPhone("Huawei", "P40 Pro", 700,
                          "China", "Huawei INC", randint(1, 100000000), [])

linked_data_paths = {"data_path": "bin/smartphone_data",
                     "metadata_path": "bin/smartphone_metadata.json", "database_type": "serial"}

data = []
data.append(smart_phone1)
data.append(smart_phone2)
data.append(smart_phone3)
data.append(smart_phone4)
data.append(smart_phone5)


file_name = type(smart_phone1).__name__.lower()

# for d in data:
#     print(str(d))


# print(file_name)
# with open("bin/"+file_name+"_data", 'wb') as data_file:
#     # koristimo pickle da bismo serijalizovali u binarnu datoteku
#     pickle.dump(data, data_file)


res = None
with open("bin/smartphone_data", "rb") as f:
    res = pickle.load(f)

print(res)
