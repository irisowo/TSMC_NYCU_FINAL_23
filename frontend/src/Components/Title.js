import React from 'react';
import styled from 'styled-components';

const Main = styled.div`
  width: 100%;
  text-align: center;
  font-size: 2.1em;
  font-weight: 600;
  font-family: 'Poppins', sans-serif;
`;

const Title = ({
  children, ...props
}) => (
  <Main {...props}>
    {children}
  </Main>
);

export default Title;
