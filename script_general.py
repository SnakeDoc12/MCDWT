from suma import Suma
try:
    import matplotlib.pyplot
except:
    os.system("pip3 install matplotlib --user")
    import matplotlib.pyplot
imagenes = 5
valores_q_step = [8,16,32,64,128,256,512,700] 
tipos_cuantificacion = ["deadzone","midrise","midthreat"]
resultado_total = {"deadzone" : [] ,"midrise" : [],"midthreat":[]}

for q_step in valores_q_step: 
    diccionario = {}
    for tipo in tipos_cuantificacion:
        suma = Suma()
        pesos = suma.GetPesosQ(q_step,tipo)
        MSE_almacenado = 0.0
        for imagen in range(0,imagenes):
            MSE_almacenado+= suma.GetMSE(q_step,tipo,imagen)
        resultado_total[tipo].append([pesos,MSE_almacenado/len(imagenes)]) 

print(resultado_total)
plt.figure()
diccionario = resultado_total
for tipo in diccionario:
    plot = plt.plot([i[0] for i in diccionario[tipo]],[i[1] for i in diccionario[tipo]],label=tipo)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper', borderaxespad=0.)
plt.ylabel('Error')
plt.xlabel('Peso')
plt.show()
