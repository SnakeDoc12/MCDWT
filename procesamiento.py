q_step=32  
predictor=2  
valores_q_step = [8,16,32,64,128,256,512,700] 
tipos_cuantificacion = ["deadzone","midrise","midthreat"]
imagenes = 5

!rm /tmp/*.png  
for q_step in valores_q_step:
    !cp ../sequences/stockholm/* /tmp/{q_step}/original   
    !cp /tmp/$q_step/original/* /tmp/$q_step/mcdwt  
    !python3 -O MDWT.py -p /tmp/$q_step/mcdwt
    !python3 -O MCDWT.py -P predictor -p /tmp/$q_step/mcdwt  
    for tipo in tipos_cuantificacion:
        for imagen in range(0,imagenes): 
            ii ="{:03d}".format(imagen)
            !python3 ../tools/quantize.py -t $tipo -i /tmp/$q_step/mcdwt/LH$ii.png -o /tmp/$q_step/$tipo/LH$ii.png -q $q_step  
            !python3 ../tools/quantize.py -t $tipo -i /tmp/$q_step/mcdwt/HL$ii.png -o /tmp/$q_step/$tipo/HL$ii.png -q $q_step  
            !python3 ../tools/quantize.py -t $tipo -i /tmp/$q_step/mcdwt/HH$ii.png -o /tmp/$q_step/$tipo/HH$ii.png -q $q_step
            !python3 ../tools/quantize.py -t $tipo -i /tmp/$q_step/mcdwt/LL$ii.png -o /tmp/$q_step/$tipo/LL$ii.png -q $q_step
        !cp /tmp/$q_step/$tipo/* /tmp/$q_step/$tipo/inversas  
        !python3 -O MCDWT.py -P $predictor -p /tmp/$q_step/$tipo/inversas -b  
        !python3 -O MDWT.py -p /tmp/$q_step/$tipo/inversas -b  
!python3 script_general.py




