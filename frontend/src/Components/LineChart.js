import React from 'react';
import { Line } from 'react-chartjs-2';

const LineChart = (props) => {
  const {
    data, time, company
  } = props;
  const colors = {
    'tsmc': 'rgb(255, 204, 37)',
    'asml': 'rgb(67, 219, 229)',
    'am': '#22577A',
    'sumco': '#57CC99'
} ;
  const labels = {
    'tsmc': 'TSMC',
    'asml': 'ASML',
    'am': '應用材料',
    'sumco': 'SUMCO'
  };
  const idxs = []
  const datasets = [];
  if (company === 'all') {
    Object.keys(data).forEach((key) => {
      datasets.push({
        label: labels[key],
        data: data[key],
        fill: false,
        borderColor: colors[key]
      });
      idxs.push(key);
    });
  }
  else {
    datasets.push({
      label: labels[company],
      data: data[company],
      fill: false,
      borderColor: colors[company]
    })
  }
  const lineData = {
    labels: time,
    datasets: datasets
  };
  const lineOptions = {
    // maintainAspectRatio: false,
    responsive: true,
    elements: {
      line: {
        tension: 0.1
      }
    },
    scales: {
      xAxes: [{
        type: 'time',
        time: {
          minUnit: 'month'
        },
        gridLines: {
          display: false
        }
      }],
      yAxes: [{
        scaleLabel: {
          display: true,
          labelString: 'Score',
          fontFamily: 'Poppins'
        },
        ticks: {
          suggestedMin: 1,
          stepSize: 5
        }
      }]
    },
    tooltips: {
      mode: 'index',
      intersect: true,
      callbacks: {
        title: (tooltipItem) => (tooltipItem[0].xLabel),
        labelColor: (tooltipItem) => {
          return { backgroundColor: colors[idxs[tooltipItem.datasetIndex]] };
        }
      }
    },
    title: {
      display: false,
      text: '熱度趨勢',
      fontSize: 20,
      fontFamily: 'Poppins'
    },
    legend: {
      display: false
    }
  };
  return (
    <Line
      data={lineData}
      options={lineOptions}
      getElementsAtEvent={(elements) => {
        if (elements.length > 0) {
          const id = elements[0]._index;
          props.handleClickScore(id);
        }
      }}
    />
  );
};

export default LineChart;
