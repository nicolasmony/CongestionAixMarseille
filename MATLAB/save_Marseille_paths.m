
myfolder= 'D:\\Projets_EXPLAIN\\AMO Meso Aix-Marseille\\DNL Marseille\\';



pathList= [
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 64 65 66 67 68 69 70 71 72 73 74 76 75 77 78 79 30 0 0 ; % path 1
48 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 25 24 26 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; % path 2
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 27 28 29 30 0 0 0 0 0 0 0 0 0 ; % path 3
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 64 65 66 67 68 69 70 71 72 73 74 76 75 77 78 79 30 31 32 ; % path 4
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 25 24 26 0 0 0 0 0 0 0 0 0 0 ; % path 5
1 3 2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 27 28 29 30 31 32 0 0 0 0 0 0 0 ; % path 6
];
            
            
            
monfichier = [myfolder,'Marseille_paths.mat'];
%for OCTAVE: save('-mat7-binary', monfichier)
save(monfichier)