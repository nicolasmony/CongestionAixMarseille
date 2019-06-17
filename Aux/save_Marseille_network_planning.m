
myfolder= 'D:\\Projets_EXPLAIN\\AMO Meso Aix-Marseille\\DNL Marseille\\';


OD_demand= [
0.090;0.500;0.040;];

T_A= [ 9.000 9.000 9.000 ];
            
            
monfichier = [myfolder,'Network_planning_parameters.mat'];
%for OCTAVE: save('-mat7-binary', monfichier)
save(monfichier)