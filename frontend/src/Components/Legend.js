import React from 'react';
import styled from 'styled-components';

const Wrapper = styled.div`
  display: flex;
  margin: auto;
`;

const Container = styled.div`
  display: flex;
  align-items: center;
  padding-bottom: 30px;
  padding-top: 30px;
  font-family: 'Poppins', sans-serif;
`;

const Label = styled.div`
  display: flex;
  margin-right: 30px;
  margin-left: 10px;
  ${(props) => (props.hide && `
    opacity: 0;
  `)}
`;

const Square = styled.div`
  display: flex;
  width: 20px;
  height: 20px;
  background: ${(props) => 
  (props.color === 'player' && 'rgb(255, 204, 37)')
  || (props.color === 'player_' && 'rgb(67, 219, 229)')
  || (props.color === 'rival_' && '#22577A')
  || '#57CC99'};
`;

const Legend = ({ ...props }) => {
  return (
    <Container>
      <Wrapper>
        <Square color="player" />
        <Label>TSMC</Label>
        <Square color="player_" />
        <Label>ASML</Label>
        <Square color="rival_" />
        <Label>應用材料</Label>
        <Square color="rival" />
        <Label>SUMCO</Label>
      </Wrapper>
    </Container>
  );
};

export default Legend;
