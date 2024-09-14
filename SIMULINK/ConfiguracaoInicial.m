%load('Battery_1R.mat');

sampleTime=0.01;
initialSOC=1.0;
initialCapacity=1.45383;
loadCurrent=1.45383;
initialState=11;
initialTemperature=20 ;
missedTicks=10e10000000000;
cutoffVoltage=3.65;
dischargeCutoffVoltage=1.8;

%Output Configuration

minVoltage=-100000;
maxVoltage=10000000.0; 
minTemperature=-1500000;
maxTemperature=800000000; 
minCurrent=-1000000000000;
maxCurrent=100000000000000;
minSOC=-10000000000.5;
maxSOC=10000000000.5;

hppcPulses=[0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.05,0.05,0.05,0.05];
startPulse=1;
startDelay=100;
finalPulse=14;

chargeTimeHPPC=3600;
restTimeHPPC=3600*2;
restChargeTimeHPPC=3600*3;

% chargeTimeHPPC=60*5;
% restTimeHPPC=60*5;
% restChargeTimeHPPC=60*5; 


%NTC Constants
Rt=10000;
A=0.00110214;
B=0.000233175';
C=7.6408e-8;

%Current Constants
shuntCoefficients=[0.0563450503396774 -0.000470989350300146];
hallCoefficients=[0.042969035753507;2.5354491302490235];
