import React from 'react';
import styled from 'styled-components';

const Link = styled.a`
  color: #fff;
  padding: 20px 10px;
  font-size: 20px;
  text-decoration: none;
  display: block;
  width: fit-content;
  ${(props) => props.highlight && `
    color: #ebff78;
    font-size: 22px;
    font-weight: 600;
    padding: 7px 16px;
  `}
  :hover{
    color: #ebff78;
    transition: all 0.4s;
  }
`;

const Select = ({ to, text, exact }) => (
    <Link href={to}>
      {text}
    </Link>
)

export default Select;
