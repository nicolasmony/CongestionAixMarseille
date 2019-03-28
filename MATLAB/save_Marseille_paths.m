
myfolder= 'C:\\Users\\Alexandre\\Documents\\C0709 DIRMED\\3_LOGICIELS\\DTA_KeHan\\DNL Marseille\\';


pathList= [
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 27 28 29 30 0 0 0 0 0 0 0 0 0 ; % path 1
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 25 24 26 0 0 0 0 0 0 0 0 0 0 ; % path 2
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 27 28 29 30 31 32 0 0 0 0 0 0 0 ; % path 3
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 53 54 55 56 57 58 59 60 61 62 63 65 64 66 67 68 30 0 0 ; % path 4
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 53 54 55 56 57 58 59 60 61 62 63 65 64 66 67 68 30 31 32 ; % path 5
];
            
            
            
monfichier = [myfolder,'Marseille_paths.mat'];
%for OCTAVE: save('-mat7-binary', monfichier)
save(monfichier)