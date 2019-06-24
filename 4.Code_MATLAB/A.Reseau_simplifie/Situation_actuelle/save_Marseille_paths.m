
myfolder= 'C:\\Users\\AlexandreNicolas\\Documents\\C0709 DIRMED\\3_LOGICIELS\\DTA_KeHan\\DNL Marseille\\Modele_simplifie_NxM\\ReseauSimplifie\\';


% Each line represents a different path and is made of the labels of the successive links
% that the path follows.
% The lines are filled up with 0s in order to have the same length
pathList= [
18 17 25 16 15 14 13 0 0 0 0 0 0 0 0 0 0 ; % path 1
18 17 25 16 15 14 12 11 10 9 8 7 6 5 2 0 0 ; % path 2
18 17 25 16 15 14 12 11 10 9 8 7 6 5 3 0 0 ; % path 3
18 17 25 16 15 14 12 11 10 9 8 7 6 5 4 27 0 ; % path 4
18 17 25 16 15 14 12 11 10 9 8 7 6 5 4 26 1 ; % path 5
19 16 15 14 13 0 0 0 0 0 0 0 0 0 0 0 0 ; % path 6
19 16 15 14 12 11 10 9 8 7 6 5 2 0 0 0 0 ; % path 7
19 16 15 14 12 11 10 9 8 7 6 5 3 0 0 0 0 ; % path 8
19 16 15 14 12 11 10 9 8 7 6 5 4 27 0 0 0 ; % path 9
19 16 15 14 12 11 10 9 8 7 6 5 4 26 1 0 0 ; % path 10
23 17 25 16 15 14 13 0 0 0 0 0 0 0 0 0 0 ; % path 11
23 17 25 16 15 14 12 11 10 9 8 7 6 5 2 0 0 ; % path 12
23 17 25 16 15 14 12 11 10 9 8 7 6 5 3 0 0 ; % path 13
23 17 25 16 15 14 12 11 10 9 8 7 6 5 4 27 0 ; % path 14
23 17 25 16 15 14 12 11 10 9 8 7 6 5 4 26 1 ; % path 15
22 12 11 10 9 8 7 6 5 2 0 0 0 0 0 0 0 ; % path 16
22 12 11 10 9 8 7 6 5 3 0 0 0 0 0 0 0 ; % path 17
22 12 11 10 9 8 7 6 5 4 27 0 0 0 0 0 0 ; % path 18
22 12 11 10 9 8 7 6 5 4 26 1 0 0 0 0 0 ; % path 19
20 9 8 7 6 5 2 0 0 0 0 0 0 0 0 0 0 ; % path 20
20 9 8 7 6 5 3 0 0 0 0 0 0 0 0 0 0 ; % path 21
20 9 8 7 6 5 4 27 0 0 0 0 0 0 0 0 0 ; % path 22
20 9 8 7 6 5 4 26 1 0 0 0 0 0 0 0 0 ; % path 23
21 8 7 6 5 2 0 0 0 0 0 0 0 0 0 0 0 ; % path 24
21 8 7 6 5 3 0 0 0 0 0 0 0 0 0 0 0 ; % path 25
21 8 7 6 5 4 27 0 0 0 0 0 0 0 0 0 0 ; % path 26
21 8 7 6 5 4 26 1 0 0 0 0 0 0 0 0 0 ; % path 27
24 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; % path 28
];
            
            
            
monfichier = [myfolder,'Marseille_paths.mat'];
%for OCTAVE: save('-mat7-binary', monfichier)
save(monfichier)