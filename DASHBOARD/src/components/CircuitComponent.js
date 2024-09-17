import React from 'react';

const CircuitComponent = ({
    SoC,
    BatteryVoltage,
    BatteryTemperature,
    BatteryCurrent,
    ChargerEnable,
    DischargerEnable,
    BatteryCapacity,
    DischargerCurrent,
    ChargerVoltage,
    ChamberSetpoint,
    ChamberTemperature,
    SimulationTime
  }) => (
    <div style={{ position: 'relative', width: '1000px', height: '600px' }}>
    <svg width="1000" height="600" viewBox="0 0 1366 682" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="60" y="224" width="64" height="26" fill="white"/>
    <rect x="2" y="250.267" width="178.54" height="276.465" rx="16" stroke="white" stroke-width="4"/>
    <rect x="4" y={252+273*(1-SoC)} width="174.5" height={273*SoC} rx="12" fill="#226927"/>
    <rect x="1144.31" y="582.992" width="117.546" height="62.3711" rx="8" fill="white"/>
    <path d="M91.2701 225.449V54H351M1283.45 94.2483V100M1283.45 395.63V100M1040.71 395.63V288.197V113.5H897M91.2701 528.732V678.948H1040.71M1283.45 558.205V678.948H1040.71M1040.71 678.948V558.205M1283.45 100V10H897M734.5 54H537" stroke="white" stroke-width="5"/>
    <path d="M1121.75 478.819C1121.75 521.731 1086.77 556.557 1043.58 556.557C1000.39 556.557 965.417 521.731 965.417 478.819C965.417 435.907 1000.39 401.081 1043.58 401.081C1086.77 401.081 1121.75 435.907 1121.75 478.819Z" stroke="white" stroke-width="9"/>
    <path d="M1360.66 478.819C1360.66 521.731 1325.69 556.557 1282.5 556.557C1239.3 556.557 1204.33 521.731 1204.33 478.819C1204.33 435.907 1239.3 401.081 1282.5 401.081C1325.69 401.081 1360.66 435.907 1360.66 478.819Z" stroke="white" stroke-width="9"/>
    <path d="M1279.19 523.955C1280.75 525.517 1283.28 525.517 1284.85 523.955L1310.3 498.499C1311.86 496.937 1311.86 494.404 1310.3 492.842C1308.74 491.28 1306.21 491.28 1304.65 492.842L1282.02 515.469L1259.39 492.842C1257.83 491.28 1255.3 491.28 1253.73 492.842C1252.17 494.404 1252.17 496.937 1253.73 498.499L1279.19 523.955ZM1278.02 435.561V521.126H1286.02V435.561H1278.02Z" fill="white"/>
    <path d="M1041.72 451.603V429.103H1045.54V451.603H1041.72ZM1032.38 442.262V438.444H1054.88V442.262H1032.38Z" fill="white"/>
    <path d="M1051.27 522.714V526.464H1036V522.714H1051.27Z" fill="white"/>
    <path d="M290.586 82.9142C291.367 82.1332 291.367 80.8668 290.586 80.0858L277.858 67.3579C277.077 66.5768 275.81 66.5768 275.029 67.3579C274.248 68.1389 274.248 69.4052 275.029 70.1863L286.343 81.5L275.029 92.8137C274.248 93.5948 274.248 94.8611 275.029 95.6421C275.81 96.4232 277.077 96.4232 277.858 95.6421L290.586 82.9142ZM196 83.5H289.172V79.5H196V83.5Z" fill="white"/>
    <path d="M509.276 321.133C510.104 321.286 510.718 321.492 511.484 321.878C513.756 323.02 515.332 324.978 516 327.476L516.205 328.23L516.249 366.252L516.294 404.274L517.051 404.777C520.943 407.401 523.41 411.129 524.363 415.855C524.603 417.023 524.683 419.655 524.532 420.976C523.695 428.137 518.422 434.021 511.431 435.585C502.614 437.552 493.779 432.126 491.499 423.321C491.053 421.605 491 421.102 491 418.928C491 416.78 491.071 416.223 491.543 414.445C492.354 411.417 494.206 408.398 496.531 406.332C497.288 405.649 498.428 404.795 499.033 404.454L499.416 404.238V399.584V394.939H496.522H493.627V393.861V392.783H496.522H499.416V385.91V379.037H496.522H493.627V377.959V376.881H496.522H499.416V370.008V363.135H496.522H493.627V362.057V360.978L496.495 360.961L499.372 360.934L499.399 354.078L499.416 347.232H496.522H493.627V346.109V344.986H496.522H499.416V336.784C499.416 329.147 499.434 328.536 499.586 327.781C499.924 326.11 500.717 324.682 501.99 323.424C503.941 321.51 506.657 320.648 509.276 321.133ZM506.248 324.268C504.564 324.807 503.219 326.146 502.64 327.862L502.4 328.59L502.373 367.33L502.355 406.071L501.305 406.691C498.544 408.344 496.834 410.114 495.551 412.657C493.289 417.131 493.529 422.351 496.192 426.52C498.223 429.709 501.358 431.865 505.143 432.692C506.479 432.979 509.115 432.979 510.487 432.692C514.798 431.775 518.235 429.107 520.213 425.136C522.083 421.371 522.065 416.628 520.168 412.809C518.903 410.249 517.024 408.281 514.343 406.7L513.221 406.044V367.717C513.221 343.198 513.186 329.183 513.132 328.787C512.945 327.53 512.464 326.55 511.547 325.625C510.95 325.023 509.953 324.43 509.213 324.25C508.991 324.196 508.732 324.125 508.634 324.107C508.296 324.026 506.675 324.134 506.248 324.268Z" fill="white"/>
    <circle cx="508" cy="419" r="12" fill="#FF3838"/>
    <rect x="504.8" y={327+90*(1-(ChamberTemperature+10)/80)} width="6.6" height={90*((ChamberTemperature+10)/80)} rx="3.3" fill="#FF3838"/>
    <rect x="539" y="381" width="108" height="50" rx="9" fill="white"/>
    <circle cx="351" cy="54" r="10" fill="white"/>
    <circle cx="543" cy="54" r="10" fill="white"/>
    <circle cx="737" cy="54" r="10" fill="white"/>
    <circle cx="892" cy="113" r="10" fill="white"/>
    <circle cx="892" cy="10" r="10" fill="white"/>
    <path d={(DischargerEnable || ChargerEnable)?"M320 54H543":"M350 55L534.5 1.5"} stroke="white" stroke-width="5"/>
    <path d={DischargerEnable?"M738.5 55L894.5 9.5":"M738.5 55L894.5 112.5"} stroke="white" stroke-width="5"/>
    <text x="92" y="400" font-size="40" font-family='Arial' text-anchor="middle" fill="white">
        {(SoC*100).toFixed(1)}%
    </text>
    <text x="240" y="140" font-size="25" font-family='Arial' text-anchor="middle" fill="white">
        {BatteryCurrent.toFixed(2)} A
    </text>
    <text x="595" y="360" font-size="25" font-family='Arial' text-anchor="middle" fill="white">
        {(ChamberTemperature).toFixed(1)} ºC
    </text>
    <text x="620" y="415" font-size="25" font-family='Arial' text-anchor="middle" fill="#40454E">
        ºC
    </text>
    <text x="965" y="630" font-size="25" font-family='Arial' text-anchor="middle" fill="white">
        {ChargerVoltage.toFixed(2)} V
    </text>
    <text x="1240" y="625" font-size="25" font-family='Arial' text-anchor="middle" fill="#40454E">
        A
    </text>
    <text x="500" y="625" font-size="25" font-family='Arial' text-anchor="middle" fill="white">
        Tempo de simulação: {SimulationTime.toFixed(0)} s
    </text>
    <text x="250" y="340" font-size="25" font-family='Arial' text-anchor="middle" fill="white">
        <tspan x="280" dy="0" >{BatteryVoltage.toFixed(2)} V</tspan>
        <tspan x="280" dy="1.2em">{BatteryTemperature.toFixed(1)} ºC</tspan>
        <tspan x="280" dy="1.2em">{BatteryCapacity.toFixed(2)} Ah</tspan>
    </text>
</svg>
<input
      type="text"
      defaultValue={ChamberSetpoint}
      style={{
        position: 'absolute',
        top: '335px',
        left: '395px',
        background: 'transparent',
        border: 'none',
        color: '#40454E',
        fontSize: '20px',
        textAlign: 'center',
        width: '45px',
      }}
    />
    <input
      type="text"
      defaultValue={DischargerCurrent}
      style={{
        position: 'absolute',
        top: '490px',
        left: '840px',
        background: 'transparent',
        border: 'none',
        color: '#40454E',
        fontSize: '20px',
        textAlign: 'center',
        width: '50px',
      }}
    />
    </div>
);

export default CircuitComponent;
