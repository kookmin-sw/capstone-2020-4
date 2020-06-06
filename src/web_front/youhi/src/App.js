import React, { Component } from 'react';
import './App.css';
import Home from './Home';

import { BrowserRouter as Router, Route } from 'react-router-dom';
import styled from 'styled-components';
import Navbar from './component/navbar/Navbar';


const StyledWrapper = styled.div`
  display: flex;
  justify-content: center;
  .innerDiv {
    width: 100%;
  }
`;
class App extends Component {
  render() {
    return (
      <Router>
      <Navbar />
        <StyledWrapper>
          <div className="innerDiv">
            <Route exact path ='/' component = { Home }/>
          </div>
        </StyledWrapper>
      </Router>
    )
  }
}

export default App;
