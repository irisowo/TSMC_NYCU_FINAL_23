import React, { PureComponent } from 'react';
import styled from 'styled-components';
import NavItem from './NavItem';

const Wrapper = styled.div`
  padding: .5rem 3%;
  box-sizing: border-box;
  width: 250px;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  background-color: #2e3638;
  box-shadow: 0px 5px 6px 3px #666;
  overflow: auto;
  font-family: 'Poppins', sans-serif;
`;


export default class NavBar extends PureComponent {
  render() {
    return (
      <Wrapper>
        <NavItem
          to={"/trend"}
          text={"All"}
          exact
        />
        <NavItem
          to={"/trend/tsmc"}
          text={"TSMC"}
        />
        <NavItem
          to={"/trend/asml"}
          text={"ASML"}
        />
        <NavItem
          to={"/trend/am"}
          text={"應用材料"}
        />
        <NavItem
          to={"/trend/sumco"}
          text={"SUMCO"}
        />
      </Wrapper>
    )
  }
}
