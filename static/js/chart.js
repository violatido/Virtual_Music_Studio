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
