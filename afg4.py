from xml.etree.ElementInclude import default_loader


kapital = float(input("Kapital (in Euro): "))
zinssatz = 2.0
zinsen = kapital / 100 * zinssatz
kapital = kapital + zinsen
print("neues Kapital ist: ", kapital)