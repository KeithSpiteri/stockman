from inventoryParser import parseInventoryFile
from inventoryPrinter import printInventory

converted_entries = parseInventoryFile('inventory.csv')
printInventory(converted_entries)
exit(0)



