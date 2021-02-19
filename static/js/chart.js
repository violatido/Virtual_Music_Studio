// the answers to the question (passed to line 15)
let labels1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
// the values of the answers (passed to line 17)
let data1 = [30, 10, 62, 15, 5, 97, 25];
// data representation colors (passed to line 18)
let colors1 = ['#FCD5BE;', '#F8B195', '#F67280', '#C06C84', '#A8A0B1', '#6C5B7B', '#355C7D'];

// myChart1 = the query in 2D context
let myChart1 = document.getElementById("myChart").getContext('2d');

// renders the chart
let chart1 = new Chart(myChart1, {
    type: 'doughnut',
    data: {
        labels: labels1, 
        datasets: [ {
            data: data1,
            backgroundColor: colors1
        }] 
    },
    options: {
        // title = the question we are asking
        title: {
            text: "How many minutes did your practice this week?",
            display: true
        }
    }
});

//________________________________________________________________________________________

// the answers to the question (passed to line 15)
let labels2 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
// the values of the answers (passed to line 17)
let data2 = [30, 10, 62, 15, 5, 97, 25];
// data representation colors (passed to line 18)
let colors2 = ['#FCD5BE;', '#F8B195', '#F67280', '#C06C84', '#A8A0B1', '#6C5B7B', '#355C7D'];

// myChart1 = the query in 2D context
let myChart2 = document.getElementById("myChart2").getContext('2d');

// renders the chart
let chart = new Chart(myChart2, {
    type: 'bar',
    data: {
        labels: labels2, 
        datasets: [ {
            data: data2,
            backgroundColor: colors2
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


//________________________________________________________________________________________

let labels3 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

// myChart1 = the query in 2D context
let myChart3 = document.getElementById("myChart3").getContext('2d');

// renders the chart
let chart3 = new Chart(myChart3, {
    type: 'radar',
    data: {
        labels: labels3, 
        datasets: [
            {
                label: 'Student week 1',
                fill: true,
                backgroundColor: "rgba(179, 181, 198, 0.2)", 
                borderColor: "rgba(179, 181, 198, 1)",
                pointBorderColor: "#FFF",
                pointBackgroundColor: "rgba(179, 181, 198, 1)",
                data: [30, 10, 62, 15, 5, 97, 25]
            },
            {
                label: 'Student week 2',
                fill: true,
                backgroundColor: "rgba(255, 99, 132, 0.2)", 
                borderColor: "rgba(255, 99, 132, 1)",
                pointBorderColor: "#FFF",
                pointBackgroundColor: "rgba(255, 99, 132, 1)",
                data: [50, 0, 12, 25, 0, 160, 30]
            },
        ] 
    },
    options: {
        // title = the question we are asking
        title: {
            text: "Minutes of practice day this week and last week",
            display: true
        },
    }
});


//________________________________________________________________________________________
// the answers to the question (passed to line 15)
let labels4 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
// the values of the answers (passed to line 17)
let data4 = [30, 10, 62, 15, 5, 97, 25];
// data representation colors (passed to line 18)
let colors4 = ['#FCD5BE;', '#F8B195', '#F67280', '#C06C84', '#A8A0B1', '#6C5B7B', '#355C7D'];

// myChart1 = the query in 2D context
let myChart4 = document.getElementById("myChart4").getContext('2d');

// renders the chart
let chart4 = new Chart(myChart4, {
    type: 'pie',
    data: {
        labels: labels4, 
        datasets: [ {
            data: data4,
            backgroundColor: colors4
        }] 
    },
    options: {
        // title = the question we are asking
        title: {
            text: "How many minutes did your practice this week?",
            display: true
        }
    }
});
