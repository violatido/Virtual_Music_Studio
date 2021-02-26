"use strict"

let labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
let data = [30, 10, 62, 15, 5, 97, 25];
let colors = ['#FCD5BE;', '#F8B195', '#F67280', '#C06C84', '#A8A0B1', '#6C5B7B', '#355C7D'];

// myChart1 = the query in 2D context
let myChart = document.getElementById("myChart").getContext('2d');

// render the chart
let chart = new Chart(myChart, {
    type: 'bar',
    data: {
        labels: labels, 
        datasets: [ {
            data: data,
            backgroundColor: colors
        }] 
    },
    options: {
        // title = the question we are asking
        title: {
            text: "How many minutes did you practice per day this week?",
            display: true
        },
        legend: {
            display: false
        }
    }
});
// ________________________________________________________________________________________________________________________
$.get('/charts.json', (res) => {
    const dates = res.dates_practiced; // give us a list of dates
    const practice_times = res.minutes_practiced; // associated practice times
    let myChart = document.getElementById("bar-time").getContext('2d');

    let colors = ['#FCD5BE;', '#F8B195', '#F67280', '#C06C84', '#A8A0B1', '#6C5 B7B', '#355C7D', '#A8A0B1'];
    let chart = new Chart(myChart, {
        type: 'bar',
        data: {
            labels: dates, 
            datasets: [ {
                data: practice_times,
                backgroundColor: colors
            }] 
        },
        options: {
            title: {
                text: "How many minutes did you practice per day this week?",
                display: true
            },
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        suggestedMin: 0,
                        suggestedMax: 150
                    }
                }]
            }
        },
        scales: {
            xAxes: [
                {
                    type: 'time',
                    time: {
                        unit: 'day',
                        round: 'day',
                        displayFormats: {
                            day: 'MMM D'
                        },
                    },
                    distribution: 'series'
                }
            ],
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        tooltips: {
            callbacks: {
                title: (tooltipItem) => {
                    return moment(tooltipItem.label).format('MMM D');
                }
            }
        }    
    })
});
