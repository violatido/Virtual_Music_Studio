"use strict"

// _________________________________________Chart 1_______________________________________________________________
$.get('/charts.json', (res) => {
    const dates = res.dates_practiced; // give us a list of dates
    // ["Feb 28", "Feb 27", "Feb 26", "Feb 25", "Feb 24", "Feb 23", "Feb 22"]
    const practiceTimes = res.minutes_practiced; // associated practice minutes only
    // [0, 0, 120, 12, 45, 35, 100]

    let myChart2 = document.getElementById("bar-time").getContext('2d');

    let colors2 = ['#FCD5BE;', '#F8B195', '#F67280', '#C06C84', '#A8A0B1', '#6C5 B7B', '#355C7D', '#A8A0B1'];
    let chart2 = new Chart(myChart2, {
        type: 'bar',
        data: {
            labels: dates.reverse(), 
            datasets: [ {
                data: practiceTimes.reverse(),
                backgroundColor: colors2
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



// ___________________________________________Chart 2_____________________________________________________________________________
$.get('/charts/2.json', (res) => {
    const datesInMonth = res.dates_in_month; // give us a list of dates over 4 weeks
    // ["Feb 28", "Feb 27", "Feb 26", "Feb 25", "Feb 24", "Feb 23", "Feb 22", "Feb 21", "Feb 20", "Feb 19", "Feb 18", "Feb 17", "Feb 16", "Feb 15", "Feb 14", "Feb 13", "Feb 12", "Feb 11", "Feb 10", "Feb  9", "Feb  8", "Feb  7", "Feb  6", "Feb  5", "Feb  4", "Feb  3", "Feb  2", "Feb  1"]
    let datesPracticedInMonth = res.log_date; // associated dates on which student practiced
    //[0, 1, 1, 1, 1, 1, 1 | 1, 1, 1, 0, 1, 1, 1 | 1, 0, 1, 0, 1, 0, 1 | 0, 1, 1, 1, 1, 1, 1]    
    //[6, 6, 4, 6]

    let viewDates = [
                        `${datesInMonth[6]} - ${datesInMonth[0]}`, // Feb 28 - Feb 21
                        `${datesInMonth[13]} - ${datesInMonth[7]}`, 
                        `${datesInMonth[20]} - ${datesInMonth[14]}`, 
                        `${datesInMonth[27]} - ${datesInMonth[21]}`
                    ];
    
    datesPracticedInMonth.unshift(0)

    const countDates = (numList) => {
        let emptylist = [];
        let count = 0;
        
        for (let i = 1; i < numList.length; i ++) {
            count += numList[i];
        
            if (i % 7 === 0) {
                emptylist.push(count)
                count = 0;
            }
        }
        return emptylist;
    }
    
    let weeks = countDates(datesPracticedInMonth);


    let myChart3 = document.getElementById("chart-3").getContext('2d');


    let colors = ['#F8B195', '#F67280', '#A8A0B1', '#6C5B7B', '#355C7D', '#A8A0B1'];
    let chart3 = new Chart(myChart3, {
        type: 'bar',
        data: {
            labels: viewDates.reverse(), //datesPracticedInMonth.reverse()
            datasets: [ {
                data: weeks.reverse(),
                backgroundColor: colors
            }] 
        },
        options: {
            title: {
                text: "How many days did you practice per week this past month?",
                display: true
            },
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        suggestedMin: 0,
                        suggestedMax: 7
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



// ___________________________________________Chart 3_____________________________________________________________________________


$.get('/charts/3.json', (res) => {
    const datesInMonth = res.dates_in_month; // give us a list of dates over 4 weeks
    // ["Feb 28", "Feb 27", "Feb 26", "Feb 25", "Feb 24", "Feb 23", "Feb 22", "Feb 21", "Feb 20", "Feb 19", "Feb 18", "Feb 17", "Feb 16", "Feb 15", "Feb 14", "Feb 13", "Feb 12", "Feb 11", "Feb 10", "Feb  9", "Feb  8", "Feb  7", "Feb  6", "Feb  5", "Feb  4", "Feb  3", "Feb  2", "Feb  1"]
    let minutesPerWeek = res.minutes_practiced; // practice minutes per date
    // [0, 45, 98, 50, 120, 12, 45, 35, 100, 22, 0, 45, 22, 23, 45, 0, 10, 0, 72, 0, 42, 0, 50, 65, 35, 122, 40, 25]

    let viewDates = [
        `${datesInMonth[6]} - ${datesInMonth[0]}`, // Feb 28 - Feb 21
        `${datesInMonth[13]} - ${datesInMonth[7]}`, 
        `${datesInMonth[20]} - ${datesInMonth[14]}`, 
        `${datesInMonth[27]} - ${datesInMonth[21]}`
    ];

    // minutesPerWeek.unshift(0)

    // const countDates = (numList) => {
    // let emptylist = [];
    // let count = 0;

    // for (let i = 1; i < numList.length; i ++) {
    //     count += numList[i];

    //     if (i % 7 === 0) {
    //     emptylist.push(count)
    //     count = 0;
    //     }
    // }
    // return emptylist
    // };

    // let minutesWeek =  countDates(minutesPerWeek);
    // console.log(minutesWeek)

//    
    const countMinutes = function(num_list) {
        let count = 0;
    
        for (let num of num_list) {
            count += num;
        }
        return count;
    };

    let week1 = countMinutes(minutesPerWeek.slice(0, 7));
    let week2 = countMinutes(minutesPerWeek.slice(7, 14));
    let week3 = countMinutes(minutesPerWeek.slice(14, 21));
    let week4 = countMinutes(minutesPerWeek.slice(21, 28));

    let minutesWeek = [week1, week2, week3, week4];
    
    let colors = ['#FCD5BE;', '#A8A0B1', '#F67280', '#355C7D'];
    let myChart4 = document.getElementById("myChart4").getContext('2d');

    let chart4 = new Chart(myChart4, {
        type: 'bar',
        data: {
            labels: viewDates.reverse(), 
            datasets: [ {
                data: minutesWeek.reverse(),
                backgroundColor: colors
            }] 
        },
        options: {
            title: {
                text: "How many minutes did you practice each week this month?",
                display: true
            },
            legend: {
                display: false
            }
        },
        options: {
            title: {
                text: "How many minutes did you practice per week this past month?",
                display: true
            },
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        suggestedMin: 0,
                        suggestedMax: 350
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


// ___________________________________________Chart 4_____________________________________________________________________________
$.get('/charts/4.json', (res) => {
    // const dates_in_month = res.dates_in_month; // give us a list of dates over 4 weeks
    const dates = res.dates_in_month;
    // console.log(dates);
});
