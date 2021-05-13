"use strict"

const urlArr = window.location.href.split('/');
const studentId = urlArr[urlArr.length - 1];

// _________________________________________Chart 1_______________________________________________________________
$.get(`/charts/1.json/${studentId}`, (res) => {

    /* This Chart Shows Minutes per day over the course of this last week
        x-axis: the date (ex: Apr 1)
        y-axis min/max: 0 - 150 minutes (ex: 50) */

    const dates = res.dates_practiced;
    const practiceTimes = res.minutes_practiced;

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
    });
});


// ___________________________________________Chart 2_____________________________________________________________________________
$.get(`/charts/2.json/${studentId}`, (res) => {

    /* This Chart Shows number of days practiced per week over four weeks
        x-axis: the date (ex: Apr 1)
        y-axis min/max: 0 - 7 days in a week (ex: 6) */

    const datesInMonth = res.dates_in_month;
    let datesPracticedInMonth = res.log_date;

    // divide the 28 days into four weeks
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
                emptylist.push(count);
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
            labels: viewDates.reverse(),
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
    });
});



// ___________________________________________Chart 3_____________________________________________________________________________
$.get(`/charts/3.json/${studentId}`, (res) => {

    /* This Chart Shows minutes practiced per week over four weeks
        x-axis: the date (ex: Apr 1)
        y-axis min/max: 0 - 450 minutes in a week (ex: 126) */

    const datesInMonth = res.dates_in_month; 
    let minutesPerWeek = res.minutes_practiced; // practice minutes per date in datesInMonth

    // divide the 28 days into four weeks
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

        if (i % 7 === 0) {
            emptylist.push(count);
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
    });
});
