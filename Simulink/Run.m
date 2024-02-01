Fault=0;%No fault

for count=2:0.125:10
    %Varying Irradiation from countmin*100 to countmax*100
    Ir=[0 100*count;3 100*count];
    Ir1=Ir;
    Ir2=Ir;
    Ir3=Ir;
    Ir4=Ir;
    Ir5=Ir;
    Ir6=Ir;
    Ir7=Ir;
    Ir8=Ir;
    Ir9=Ir;
    for count2=5:0.5:55
    %Varying Temperature from count2 min to count2 max
    Temp=[0 count2;3 count2];
    Tmp1=Temp;
    Tmp2=Temp;
    Tmp3=Temp;
    Tmp4=Temp;
    Tmp5=Temp;
    Tmp6=Temp;
    Tmp7=Temp;
    Tmp8=Temp;
    Tmp9=Temp;
    sim('power_PVArray_PartialShading2')
    Data=[Data;Pmax Vmp Imp Tmp1(1,2) Tmp2(1,2) Tmp3(1,2) Tmp4(1,2) Tmp5(1,2) Tmp6(1,2) Tmp7(1,2) Tmp8(1,2) Tmp9(1,2) Ir1(1,2) Ir2(1,2) Ir3(1,2) Ir4(1,2) Ir5(1,2) Ir6(1,2) Ir7(1,2) Ir8(1,2) Ir9(1,2) Fault];
    
    end
end

%save('Datan.txt','Data','-ascii');