import React from 'react';
import { noop } from 'lodash';
import styled from 'styled-components';

const Main = styled.button`
  cursor: pointer;
  position: relative;
  overflow: hidden;
  outline: none;
  border: none;
  height: ${(props) => props.size}px;
  line-height: ${(props) => props.size}px;
  width: ${(props) => props.size * 4.5}px;
  padding: 5px 20px;
  color: '#fff';
  background-color: '#3fbbc3';
  border-radius: 5px;
  font-size: 1em;
  font-weight: 500;
  letter-spacing: normal;

  ${(props) => props.oval && `
    border-radius: ${props.size ? props.size * 0.618 : 25}px;
  `}

  :hover{
    opacity: 0.9;
    transition: all 0.5s;
  }

  :focus{
    outline: none;
  }
`;

const Button = ({ children, onClick = noop, ...props }) => (
  <Main onClick={onClick} {...props}>
    {children}
  </Main>
);

export default Button;
