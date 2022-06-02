import React from 'react';
import styled from 'styled-components';

const Main = styled.div`
  width: 100%;
  text-align: center;
  font-size: 1.2em;
  padding-bottom: 30px;
  font-weight: bold;
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
`;

const Subtitle = ({
  children, ...props
}) => (
  <Main {...props}>
    {children}
  </Main>
);

export default Subtitle;
