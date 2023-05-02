import xlrd
class Array3D:
    def __init__(self, depth, rows, cols):
        self.__depth=depth
        self.__rows=rows
        self.__cols= cols
        self.__arreglo=[[[0 for j in range(cols)] for i in range(rows)] for k in range(depth)]
    
    def get_num_depth(self):
        return self.__depth
    
    def get_num_rows(self):
        return self.__rows
    
    def get_num_cols(self):
        return self.__cols

    def set_item(self, depth,rows,cols,value):
        self.__arreglo[depth][rows][cols]=value

    def get_item(self,depth,rows,cols):
        return self.__arreglo[depth][rows][cols]



def main():
    a3=Array3D(34,33,14)
    for anio in range(2017,2019,1):
        ruta='./Precipitaciones/'+str(anio)+'Precip.xls'
        #print(ruta)
        archivo=xlrd.open_workbook(filename=ruta)
        hoja=archivo.sheet_by_index(0)
        for r in range(1,33,1):
            for c in range(0,14,1):
                #print(hoja.cell_value(r,c), end='')                
                a3.set_item(anio-2017,r-1,c,hoja.cell_value(r,c))
    a=int(input("Seleccione un año (2017-2018): "))
    e=int(input("Seleccione un Estado (1-32):"))
    m=int(input("Seleccione un mes (1-12): "))
    print(f"En el estado de {a3.get_item(0,e,0)} llovió un promedio de {a3.get_item(a-2017,e,m)} centímetros cúbicos en el mes de {a3.get_item(0,0,m)} del año {a}")
main()
