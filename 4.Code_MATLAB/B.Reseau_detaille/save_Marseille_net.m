
myfolder= 'C:\\Users\\AlexandreNicolas\\Documents\\C0709 DIRMED\\3_LOGICIELS\\DTA_KeHan\\DNL Marseille\\ReseauDetaille\\';

networkName= 'MarseilleAubagne';

% tail_node head_node capacity length free_flow_time other_info
%1: Marseille
%2: Aubagne

linkData= [
2 1 1.10 629.0000 25.2  1; % 1-th link (A50dp)
4 2 1.65 1421.1000 56.8  1; % 2-th link (A50dn)
5 4 1.65 1276.8000 51.1  1; % 3-th link (A50dm)
6 5 1.65 717.8000 28.7  1; % 4-th link (A50dl)
7 6 1.65 998.6000 39.9  1; % 5-th link (A50dk)
8 7 1.65 986.6000 39.5  1; % 6-th link (A50dj)
9 8 1.65 999.2000 40.0  1; % 7-th link (A50dh)
10 9 1.65 430.0000 17.2  1; % 8-th link (A50di)
11 10 1.65 581.1000 23.2  1; % 9-th link (A50dg)
12 11 1.65 1001.4000 40.1  1; % 10-th link (A50df)
13 12 1.65 1000.2000 40.0  1; % 11-th link (A50de)
14 13 1.65 990.5000 39.6  1; % 12-th link (A50dd)
15 14 1.65 1005.6000 40.2  1; % 13-th link (A50dc)
16 15 1.65 1253.7000 50.1  1; % 14-th link (A50db)
19 16 1.10 2035.3000 81.4  1; % 15-th link (A50da)
37 16 0.55 350.0000 14.0  1; % 16-th link (A501b2)
17 37 1.10 269.2000 10.8  1; % 17-th link (A501b1)
18 17 1.10 1612.1000 64.5  1; % 18-th link (A501a)
31 18 0.40 200.0000 14.4  1; % 19-th link (A501_E1)
20 19 1.10 557.3000 22.3  1; % 20-th link (A502_a)
21 20 1.10 571.7000 22.9  1; % 21-th link (A502_b)
22 21 1.10 466.8000 18.7  1; % 22-th link (A502_c)
32 21 0.40 200.0000 14.4  1; % 23-th link (A502_E1)
34 4 0.40 200.0000 14.4  1; % 24-th link (A50_E10)
27 9 0.40 200.0000 14.4  1; % 25-th link (A50_E6)
26 10 0.40 200.0000 14.4  1; % 26-th link (A50_E5)
28 13 0.40 200.0000 14.4  1; % 27-th link (A50_E8)
33 20 0.40 200.0000 14.4  1; % 28-th link (A502_E2)
2 23 0.40 200.0000 14.4  1; % 29-th link (A50_S2)
5 36 1.10 700.0000 28.0  1; % 30-th link (A50_L2)
13 28 0.40 200.0000 14.4  1; % 31-th link (A50_S8)
5 25 0.80 200.0000 14.4  1; % 32-th link (A50_S4)
5 35 0.80 200.0000 14.4  1; % 33-th link (A50_S11)
28 26 1.00 2900.0000 208.8  1; % 34-th link (D2c)
30 28 1.00 3200.0000 230.4  1; % 35-th link (D2a)
29 17 0.80 200.0000 14.4  1; % 36-th link (A501_E10)
29 30 1.00 110.0000 7.9  1; % 37-th link (D2b)
3 24 0.80 200.0000 14.4  1; % 38-th link (A50_S3)
];

nodeCoordinates= [ 
894302.02 6245561.92; % 1-th node (1: Noeud sans nom)
894914.80 6245670.49; % 2-th node (2: Noeud sans nom)
895229.47 6245744.10; % 3-th node (3: A50_PR1)
896307.82 6245858.19; % 4-th node (4: Noeud sans nom)
897568.34 6246090.05; % 5-th node (6: Noeud sans nom)
898258.41 6246275.91; % 6-th node (7: Noeud sans nom)
899149.05 6246752.52; % 7-th node (8: Noeud sans nom)
900061.78 6247080.07; % 8-th node (9: Noeud sans nom)
901049.96 6246910.77; % 9-th node (10: Noeud sans nom)
901467.68 6246805.88; % 10-th node (11: Noeud sans nom)
902032.61 6246675.23; % 11-th node (12: Noeud sans nom)
903007.91 6246432.33; % 12-th node (13: Noeud sans nom)
903983.20 6246204.14; % 13-th node (14: Noeud sans nom)
904964.02 6246143.42; % 14-th node (15: Noeud sans nom)
905948.51 6246355.04; % 15-th node (16: Noeud sans nom)
907164.87 6246708.35; % 16-th node (17: Noeud sans nom)
907567.87 6247138.96; % 17-th node (18: Noeud sans nom)
908620.45 6248324.03; % 18-th node (19: A501_Aubagne)
909047.37 6246121.34; % 19-th node (20: A50_Sud)
909547.90 6246077.17; % 20-th node (21: Noeud sans nom)
910122.04 6246172.86; % 21-th node (22: Noeud sans nom)
910593.12 6246209.67; % 22-th node (23: Noeud sans nom)
894799.72 6245684.90; % 23-th node (26: Noeud sans nom)
895077.45 6245722.43; % 24-th node (28: Bd_J_Moulin)
897488.63 6246142.78; % 25-th node (30: vers_D2_est_avant_L2)
901740.50 6246772.47; % 26-th node (33: Rd_Point_du_LC_Piollet)
901286.79 6246902.58; % 27-th node (34: La Valentine)
903735.49 6246352.12; % 28-th node (36: Saint-Menet)
907708.27 6247270.13; % 29-th node (37: D2_vers_A501)
906855.84 6246604.51; % 30-th node (38: Noeud sans nom)
908677.94 6248420.09; % 31-th node (39: A501_Aubagne_entree)
910576.19 6246246.62; % 32-th node (42: A502_vers_A50)
909731.32 6246169.89; % 33-th node (43: A502_vers_A50)
896904.81 6245960.76; % 34-th node (44: Noeud sans nom)
897379.37 6246075.43; % 35-th node (45: vers_D2_ouest_avant_L2)
896917.61 6246071.37; % 36-th node (46: L2)
907472.96 6246952.58; % 37-th node (175: Noeud sans nom)
];



monfichier= [myfolder,'Marseille_dat.mat'];      
%for OCTAVE: save('-mat7-binary', monfichier);
save(monfichier, 'networkName', 'linkData', 'nodeCoordinates');