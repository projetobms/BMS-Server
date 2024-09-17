import React, { useEffect, useState } from 'react';
import FlexVertical from '../components/FlexVertical';
import FlexHorizontal from '../components/FlexHorizontal';
import PageTitle from '../components/PageTitle';
import LinkButton from '../components/LinkButton';
import '../styles/graphs.css'

function Webcam() {

  return (
        <FlexVertical>
          
        <FlexHorizontal>
          <div style={{marginLeft:"0px",marginRight:"auto"}}>
            <PageTitle>Projeto BMS</PageTitle>
          </div>
          <div style={{marginRight:"110px",marginLeft:"auto"}}>
            <LinkButton href={"/"}>Voltar</LinkButton>
          </div>
        </FlexHorizontal>
       
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh', width:"80vw" }}>
        <iframe
    src={"https://labnvh.online/webcam"}
    title="Espelho de Rota"
    height="480px"
    width="640px"
    style={{ margin:"auto",marginTop: '20px',border:"none",marginLeft:"500px"}}
        />
        </div>

        </FlexVertical>
  );
}

export default Webcam;
