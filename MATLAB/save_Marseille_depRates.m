myfolder= 'C:\\Users\\Alexandre\\Documents\\C0709 DIRMED\\3_LOGICIELS\\DTA_KeHan\\DNL Marseille\\';

dt=10 %time step



pathDepartures= [
0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 0.890 ; % path 1
0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 ; % path 2
0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 0.250 ; % path 3
0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 ; % path 4
0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 0.020 ; % path 5
];





monfichier= [myfolder,'Marseille_depRates.mat'];      
%for OCTAVE: save('-mat7-binary', monfichier);
save(monfichier);





