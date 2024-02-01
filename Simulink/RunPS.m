Fault=1;%Partial Shading
for k=1:9 %K denotes the panel with partial shading
for count=3.1:1:7.1
    Ir=100*count;
    %Setting the Irradiance to 100*count
    Irset=[Ir Ir Ir Ir Ir Ir Ir Ir Ir];
    Irset(k)=Ir/2; %Irradiation of the partial shaded module
    Ir1=[0 Irset(1);3 Irset(1)];
    Ir2=[0 Irset(2);3 Irset(2)];
    Ir3=[0 Irset(3);3 Irset(3)];
    Ir4=[0 Irset(4);3 Irset(4)];
    Ir5=[0 Irset(5);3 Irset(5)];
    Ir6=[0 Irset(6);3 Irset(6)];
    Ir7=[0 Irset(7);3 Irset(7)];
    Ir8=[0 Irset(8);3 Irset(8)];
    Ir9=[0 Irset(9);3 Irset(9)];
    for count2=17:1:32%Varying Temperature from count2 min to count2 max
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
    %Appending the data
    Data=[Data;Pmax Vmp Imp Tmp1(1,2) Tmp2(1,2) Tmp3(1,2) Tmp4(1,2) Tmp5(1,2) Tmp6(1,2) Tmp7(1,2) Tmp8(1,2) Tmp9(1,2) Ir1(1,2) Ir2(1,2) Ir3(1,2) Ir4(1,2) Ir5(1,2) Ir6(1,2) Ir7(1,2) Ir8(1,2) Ir9(1,2) Fault];
    
    end
end
end