
myfolder= 'C:\\Users\\Alexandre\\Documents\\C0709 DIRMED\\3_LOGICIELS\\DTA_KeHan\\DNL Marseille\\';


pathList= [
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 27 28 29 30 ; % path 1
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 25 24 26 0 ; % path 2
];
            
            
            
monfichier = [myfolder,'Marseille_paths.mat'];
save('-mat7-binary', monfichier)