import xlsxwriter
import pandas as pd

df_train = pd.read_excel('nnnodes.xlsx')
primera = df_train['latitute']
segunda = df_train['longitude']

large = len(primera)

workbook = xlsxwriter.Workbook('nuevosnodeslimpioskkk.xlsx')
worksheet = workbook.add_worksheet()

row = 0
for j in range(large):
    if segunda[j] < -71:
        worksheet.write(row, 2, "Costa")
    if segunda[j] > -71:
        worksheet.write(row, 2, "Cordillera")
    if primera[j] > -18.9875312:
        worksheet.write(row, 1, "XV")
        worksheet.write(row, 2, "1")

    elif primera[j] > -21.431166:
        worksheet.write(row, 1, "I")  
        worksheet.write(row, 2, "2")
      
    elif primera[j] > -25.973074:
        worksheet.write(row, 1, "II") 
        worksheet.write(row, 2, "3")
       
    elif primera[j] > -29.2832805:
        worksheet.write(row, 1, "III")     
        worksheet.write(row, 2, "4")
   
    elif primera[j] > -32.045603:
        worksheet.write(row, 1, "IV")
        worksheet.write(row, 2, "5")
        
    elif primera[j] > -34.1292265:
        worksheet.write(row, 1, "RM-V")
        worksheet.write(row, 2, "6")
        
    elif primera[j] > -34.8051606:
        worksheet.write(row, 1, "VI")
        worksheet.write(row, 2, "7")
        
    elif primera[j] > -36.2039871:
        worksheet.write(row, 1, "VII")
        worksheet.write(row, 2, "8")
        
    elif primera[j] > -37.89447:
        worksheet.write(row, 1, "VIII")
        worksheet.write(row, 2, "9")
        
    elif primera[j] > -39.4841594:
        worksheet.write(row, 1, "IX") 
        worksheet.write(row, 2, "10")
       
    elif primera[j] > -40.5195415:
        worksheet.write(row, 1, "XIV")  
        worksheet.write(row, 2, "11")
   
    elif primera[j] > -43.7621927:
        worksheet.write(row, 1, "XIV")    
        worksheet.write(row, 2, "12")
     
    else:
        worksheet.write(row, 1, "sur")  
    row += 1      
       

workbook.close()

mitad = -71
arica_xiv = -18.9875312
tarapaca_i = -21.431166
antofagasta_ii = -25.973074
atacama_iii = -29.2832805
coquimbo_iv = -32.045603
valparaiso_metro_v_rm = -34.1292265
ohhigins_vi = -34.8051606
maule_vii = -36.2039871
biobio_viii = -37.89447
araucania_ix = -39.4841594
losrios_xiv = 40.5195415
loslagos_x = -43.7621927


           
