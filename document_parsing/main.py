from unstructured.partition.auto import partition
from unstructured.staging.base import convert_to_dict, elements_to_json, elements_from_json


elements = partition(filename="aipg/aipg_alltext.txt")

for element in elements[:5]:
    print(element.category)
    print("\n")

filename = "outputs.json"
elements_to_json(elements, filename=filename)
#convert_to_dict(elements)