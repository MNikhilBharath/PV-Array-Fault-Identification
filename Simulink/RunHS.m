Fault=3;%Hotspot
for k=1:9
for count=3:10
    %Varying Irradiation from countmin*100 to countmax*100
    Ir=100*count;
    Irset=[Ir Ir Ir Ir Ir Ir Ir Ir Ir];
    Ir1=[0 Irset(1);3 Irset(1)];
    Ir2=[0 Irset(2);3 Irset(2)];
    Ir3=[0 Irset(3);3 Irset(3)];
    Ir4=[0 Irset(4);3 Irset(4)];
    Ir5=[0 Irset(5);3 Irset(5)];
    Ir6=[0 Irset(6);3 Irset(6)];
    Ir7=[0 Irset(7);3 Irset(7)];
    Ir8=[0 Irset(8);3 Irset(8)];
    Ir9=[0 Irset(9);3 Irset(9)];
    for count2=5:0.5:50
    Temp=count2;
    Tempset=ones(1,9).*Temp;
    Tempset(k)=70;
    %Varying Temperature from count2 min to count2 max with kth panel having temperature 70 deg Centigrate
    Tmp1=[0 Tempset(1);3 Tempset(1)];
    Tmp2=[0 Tempset(2);3 Tempset(2)];
    Tmp3=[0 Tempset(3);3 Tempset(3)];
    Tmp4=[0 Tempset(4);3 Tempset(4)];
    Tmp5=[0 Tempset(5);3 Tempset(5)];
    Tmp6=[0 Tempset(6);3 Tempset(6)];
    Tmp7=[0 Tempset(7);3 Tempset(7)];
    Tmp8=[0 Tempset(8);3 Tempset(8)];
    Tmp9=[0 Tempset(9);3 Tempset(9)];
    sim('power_PVArray_PartialShading2')
    Data=[Data;Pmax Vmp Imp Tmp1(1,2) Tmp2(1,2) Tmp3(1,2) Tmp4(1,2) Tmp5(1,2) Tmp6(1,2) Tmp7(1,2) Tmp8(1,2) Tmp9(1,2) Ir1(1,2) Ir2(1,2) Ir3(1,2) Ir4(1,2) Ir5(1,2) Ir6(1,2) Ir7(1,2) Ir8(1,2) Ir9(1,2) Fault];
    
    end
end
end
%save('DataHS_Train.txt','Data','-ascii');