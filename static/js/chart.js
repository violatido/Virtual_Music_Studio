"use strict"

/*
The code below appears to be the culprit of your issue with callbacks...

*/
const urlArr = window.location.href.split('/');
const studentId = urlArr[urlArr.length - 1];

// _________________________________________Chart 1_______________________________________________________________
$.get(`/charts/1.json/${studentId}`, (res) => {

    // Minutes per day over the course of this last week
    // x-axis: the date (ex: Apr 1)
    // y-axis min/max: 0 - 150 minutes in a day

    const dates = res.dates_practiced;
    // ex: ["Feb 28", "Feb 27", "Feb 26", "Feb 25", "Feb 24", "Feb 23", "Feb 22"]
    const practiceTimes = res.minutes_practiced;
    // ex: [0, 0, 120, 12, 45, 35, 100]

    let myChart2 = document.getElementById("bar-time");

    let colors2 = ['#424B54', '#F8B195', '#F67280', '#C06C84', '#A8A0B1', '#6C5B7B', '#355C7D'];
    let chart2 = new Chart(myChart2, {
        type: 'bar',
        data: {
            labels: dates.reverse(),
            datasets: [ {
                data: practiceTimes.reverse(),
                backgroundColor: colors2,
                borderWidth: 5,
            }]
        },
        options: {
            title: {
                text: "How many minutes did you practice per day this week?",
                display: true,
                fontSize: 18,
                fontColor: '#424B54'
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
                }],
            }
        },
        scales: {
            xAxes: [
                {
                ticks: {
                    fontSize: 14
                },
                type: 'time',
                time: {
                    unit: 'day',
                    round: 'day',
                    displayFormats: {
                        day: 'MMM D'
                    },
                },
                distribution: 'series',
                }],
            },
            tooltips: {
                titleFontSize: 20,
                callbacks: {
                    title: (tooltipItem) => {
                        return moment(tooltipItem.label).format('MMM D');
                    }
                }
        }
    })
});


// ___________________________________________Chart 2_____________________________________________________________________________
$.get(`/charts/2.json/${studentId}`, (res) => {
    const datesInMonth = res.dates_in_month;
    // ["Feb 28", "Feb 27", "Feb 26", "Feb 25", "Feb 24", "Feb 23", "Feb 22", "Feb 21", "Feb 20", "Feb 19", "Feb 18", "Feb 17", "Feb 16", "Feb 15", "Feb 14", "Feb 13", "Feb 12", "Feb 11", "Feb 10", "Feb  9", "Feb  8", "Feb  7", "Feb  6", "Feb  5", "Feb  4", "Feb  3", "Feb  2", "Feb  1"]
    let datesPracticedInMonth = res.log_date;
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


    let myChart3 = document.getElementById("chart-3");


    let colors = ['#C06C84', '#6C5B7B', '#355C7D', '#F8B195'];
    let chart3 = new Chart(myChart3, {
        type: 'bar',
        data: {
            labels: viewDates.reverse(), //datesPracticedInMonth.reverse()
            datasets: [ {
                data: weeks.reverse(),
                backgroundColor: colors,
                borderWidth: 5
            }]
        },
        options: {
            title: {
                fontSize: 18,
                fontColor: '#424B54',
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
$.get(`/charts/3.json/${studentId}`, (res) => {
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

    minutesPerWeek.unshift(0);

    const countDates = (numList) => {
        let emptylist = [];
        let count = 0;

    for (let i = 1; i < numList.length; i ++) {
        count += numList[i];
        // i + 1  % 7 === 0
        if (i % 7 === 0) {
            emptylist.push(count)
            count = 0;
        }
    }
    return emptylist
    };

    let minutesWeek =  countDates(minutesPerWeek);


    let colors = ['#355C7D', '#F67280', '#A8A0B1', '#424B54'];
    let myChart4 = document.getElementById("myChart4");

    let chart4 = new Chart(myChart4, {
        type: 'bar',
        data: {
            labels: viewDates.reverse(),
            datasets: [ {
                data: minutesWeek.reverse(),
                backgroundColor: colors,
                borderWidth: 5,
            }]
        },
        options: {
            title: {
                fontSize: 18,
                fontColor: '#424B54',
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
                        suggestedMax: 450
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
