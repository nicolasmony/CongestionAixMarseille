
myfolder= 'C:\\Users\\AlexandreNicolas\\Documents\\C0709 DIRMED\\3_LOGICIELS\\DTA_KeHan\\DNL Marseille\\Modele_simplifie_NxM\\ReseauSimplifie\\';

networkName= 'AubagneMarseille';


% Features of the links of the network
% Each line represents a different link (labelled by the line number) and the columns are:
% 1) tail_node 2) head_node 3) capacity 4) length 5) free_flow_time 6) other_info
linkData= [
2 1 1.58 1421.1 56.844  1 ; % link 1
3 18 0.4 200 14.4  1 ; % link 2
3 24 0.4 200 14.4  1 ; % link 3
3 26 1.5 1276.8 51.072  1 ; % link 4
4 3 1.58 717.8 28.712  1 ; % link 5
5 4 1.58 998.6 39.944  1 ; % link 6
6 5 1.58 986.6 39.464  1 ; % link 7
7 6 1.58 999.2 39.968  1 ; % link 8
8 7 1.58 430 17.2  1 ; % link 9
9 8 1.58 581.1 23.244  1 ; % link 10
10 9 1.58 1001.4 40.056  1 ; % link 11
11 10 1.58 1000.2 40.008  1 ; % link 12
11 28 0.42 200 14.4  1 ; % link 13
12 11 1.5 990.5 39.62  1 ; % link 14
13 12 1.5 1005.6 40.224  1 ; % link 15
14 13 1.5 1253.7 50.148  1 ; % link 16
15 25 1.2 269.2 10.768  1 ; % link 17
16 15 1.2 1612.1 64.484  1 ; % link 18
17 14 1.2 2035.3 81.412  1 ; % link 19
19 8 0.4 200 14.4  1 ; % link 20
20 7 0.4 200 14.4  1 ; % link 21
21 11 0.42 200 14.4  1 ; % link 22
22 15 0.4 200 14.4  1 ; % link 23
23 2 0.4 200 14.4  1 ; % link 24
25 14 0.55 350 14  1 ; % link 25
26 2 1.3 1276.8 51.072  1 ; % link 26
26 27 1.3 1276.8 65.664  1 ; % link 27
];

% Coordinates of the nodes 
% Each line represents a different node (labelled by the node number) and the columns are
% 1) X 2) Y
nodeCoordinates= [ 
894914.801 6245670.492 ; % node 1
896307.816 6245858.19 ; % node 2
897568.338 6246090.053 ; % node 3
898258.405 6246275.911 ; % node 4
899149.051 6246752.517 ; % node 5
900061.78 6247080.069 ; % node 6
901049.956 6246910.772 ; % node 7
901467.676 6246805.882 ; % node 8
902032.611 6246675.23 ; % node 9
903007.905 6246432.326 ; % node 10
903983.2 6246204.144 ; % node 11
904964.015 6246143.418 ; % node 12
905948.511 6246355.039 ; % node 13
907164.868 6246708.353 ; % node 14
907567.868 6247138.955 ; % node 15
908620.45 6248324.03 ; % node 16
909047.371 6246121.336 ; % node 17
897488.627 6246142.782 ; % node 18
901740.5 6246772.473 ; % node 19
901286.789 6246902.581 ; % node 20
903735.493 6246352.123 ; % node 21
907656.0742 6247292.823 ; % node 22
896895.4746 6245991.111 ; % node 23
897379.37 6246075.435 ; % node 24
907472.958 6246952.585 ; % node 25
897093.5958 6245997.958 ; % node 26
896971.7144 6246619.554 ; % node 27
903745.493 6246362.123 ; % node 28
];



monfichier= [myfolder,'Marseille_dat.mat'];      
%for OCTAVE: save('-mat7-binary', monfichier);
save(monfichier);