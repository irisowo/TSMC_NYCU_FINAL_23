import React, { Component } from 'react';
import {
  BrowserRouter, Switch, Route
} from 'react-router-dom';
import styled from 'styled-components';

import Trend from './Page/Trend';
import NavBar from './Components/NavBar';

const Main = styled.div`
  display: flex;
  width: 100%;
  box-sizing: border-box;
`;

const Wrapper = styled.div`
  padding-left: 300px;
  width: 100%;
`;

class Router extends Component {
  render() {
    return (
      <div>
      <BrowserRouter>
        <Main>
          <Route path="/" component={NavBar} />
          <Wrapper>
            <Switch>
              <Route exact path="/trend" render={(props) => (
                <Trend {...props} all={true} />
              )}/>
              <Route exact path="/trend/:company" component={Trend} />
            </Switch>
          </Wrapper>
        </Main>
      </BrowserRouter>
      </div>
    );
  }
}

export default Router;
