Data=[];

%Running multiple script files
RunHS
Run
RunPS
RunS

%Saving the Data in .txt file
save('Data.txt','Data','-ascii');
