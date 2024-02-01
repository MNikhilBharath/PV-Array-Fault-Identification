Fault=2;%Short Circuit
for k=3:11
    kk=num2str(k); %the name of the slx file  
for count=3.5:1:7.5
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
    for count2=15:1:30
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
    name=strcat('power_PVArray_PartialShading',kk);%The name of slx file with short circuit of respective module
    sim(name)
    %Appending the data 
    Data=[Data;Pmax Vmp Imp Tmp1(1,2) Tmp2(1,2) Tmp3(1,2) Tmp4(1,2) Tmp5(1,2) Tmp6(1,2) Tmp7(1,2) Tmp8(1,2) Tmp9(1,2) Ir1(1,2) Ir2(1,2) Ir3(1,2) Ir4(1,2) Ir5(1,2) Ir6(1,2) Ir7(1,2) Ir8(1,2) Ir9(1,2) Fault];
    
    end
end
end