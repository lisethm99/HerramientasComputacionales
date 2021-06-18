def facturacion ():
    productos = []
    articulo = str(input())
    productos.append(articulo)
    precio = float (input())
    productos.append(precio)
    impuesto = ("SE HACE UN INCREMENTO DEL 8% CORRESPONDIENTE AL IVA")
    productos.append(impuesto)
    iva = precio * 0.08
    preciofinal = precio + iva
    productos.append(preciofinal)
    print(productos)

facturacion()




