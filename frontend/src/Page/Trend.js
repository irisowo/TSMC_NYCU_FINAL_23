import React, { Component } from 'react';
import LineChart from '../Components/LineChart';
import { withRouter } from "react-router";
import axios from 'axios';
import styled from 'styled-components';
import Title from '../Components/Title';
import Subtitle from '../Components/Subtitle';
import Legend from '../Components/Legend';


const Wrapper = styled.div`
  width: 80%;
  box-sizing: border-box;
  padding-top: 2%;
  padding-bottom: 20%;
  font-family: 'Poppins', sans-serif;
`;

const Info = styled.div`
  padding: 20px 0;
  display: flex;
  margin: auto;
`;

const Time = styled.div`
  font-size: 17px;
  background-color: #38A3A5;
  color: #fff;
  padding: 3px 10px;
  border-radius: 20px;
  width: fit-content;
  margin-right: 25px;
`;

const Name = styled.div`
  font-size: 18px;
  padding-right: 10px;
  color: #15545e;
`;

const Value = styled.div`
  font-size: 18px;
  padding-right: 25px;
`;

const InfoWrapper = styled.div`
  display: flex;
`;

class Trend extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {},
      time: [],
      showTime: '',
      showData: {}
    }
    this.labels = {
        'tsmc': 'TSMC',
        'asml': 'ASML',
        'am': '應用材料',
        'sumco': 'SUMCO'
    };
    this.company =  this.props.all ? 'all' : this.props.match.params.company;
    const params = this.props.all ?
      'getAll' : `getCompany?company=${this.props.match.params.company}`;
    this.api = `http://${window.location.hostname}/api/${params}`;
    this.handleClickInfo = this.handleClickInfo.bind(this);
    this.getData = this.getData.bind(this);
  }
  componentDidMount() {
    this.getData();
  }
  handleClickInfo(info_id) {
    const {
      data,
      time
    } = this.state;
    const showTime = time[info_id];
    const showData = {};
    Object.keys(data).forEach((key) => {
      showData[key] = data[key][info_id];
    });
    this.setState({ showTime: showTime, showData: showData });
  }
  async getData() {
    this.setState({ showTime: '', showData: {} });
    try {
      const response = await axios.get(this.api);
      if (response.status !== 200) {
        throw Error(response.statusText);
      } else {
        const newData = response.data.data;
        Object.keys(this.labels).forEach((key) => {
          if (this.company === 'all' || this.company === key) {
            newData[key].forEach((value, index) => {
              if (value === '<1') {
                newData[key][index] = '0.5'
              }
            });
          }
        });
        this.setState({ data: newData, time: response.data.time });
      }
    } catch (error) {
      console.log(error);
    }
  }
  render() {
    const {
      data,
      time,
      showTime,
      showData
    } = this.state;
    return (
      <Wrapper>
        <Title>聲量趨勢</Title>
        {
          this.company !== 'all' ?
            <Subtitle>{this.labels[this.company]}</Subtitle> :
            <Legend center />
        }
        <LineChart
          data={data}
          time={time}
          company={this.company}
          handleClickScore={this.handleClickInfo}
        />
        {
          showTime !== '' &&
          <InfoWrapper>
            <Info>
              <Time>{showTime}</Time>
              {
                Object.keys(this.labels).map((key) => {
                  if (this.company === 'all' || this.company === key) {
                    return (
                      <div style={{ display: 'flex', alignItems: 'center' }}>
                        <Name>{`${this.labels[key]}`}</Name>
                        <Value>{showData[key]}</Value>
                      </div>
                    );
                  } else {
                    return (<div key={`${showTime}-${key}`} />);
                  }
                })
              }
            </Info>
          </InfoWrapper>
        }
      </Wrapper>
    );
  }
}

export default withRouter(Trend);