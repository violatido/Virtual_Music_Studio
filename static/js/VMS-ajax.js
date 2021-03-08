"use strict"

//________________________________________Events for teacher login/registration______________________________________

// event handler for teacher login verification
$('#login_teacher').on('submit', (evt) => {
    // evt.preventDefault();
    // console.log("LOGIN FUCNTION WORKS")

    // const loginFormValues = {
    //     'teacher_login_email': $('#teacher_login_email').val(),
    //     'teacher_login_pw': $('#teacher_login_pw').val()
    // }

    // $.post("/teacher-portal", loginFormValues, (res) => {
    //     $('#teacher_added_response').text("is logged in!")
    //     console.log("HIIIIIIIIIIIII")
    
    // })
});


// event handler for new teacher registration 
$('#create_teacher').on('submit', (evt) => {
    evt.preventDefault();

    // converts teacher registration form into an object
    // const teacherFormValues = $('#teacher_reg_form').serialize();
    const teacherFormValues = { 
        'teacher_fname': $('#teacher_fname').val(),
        'teacher_lname': $('#teacher_lname').val(),
        'teacher_email': $('#teacher_email').val(),
        'teacher_phone': $('#teacher_phone').val(),
        'teacher_password': $('#teacher_password').val()
    } 

    $.post("/teacher-portal-create", teacherFormValues, (res) => {
        $('#teacher_added_response').text(`Teacher profile for ${res.teacher_fname} ${res.teacher_lname} has been created!`);
    });
});

//________________________________________Event for student login/registration______________________________________


// event handler for student login
$('#login_student').on('submit', (evt) => {
    // evt.preventDefault();
    // console.log("LOGIN FUCNTION WORKS")

    // const loginFormValues = {
    //     'student_login_email': $('#student_login_email').val(),
    //     'student_login_pw': $('#student_login_pw').val()
    // }

    // $.post("/student-portal", loginFormValues, (res) => {
    //     $('#student_login_response').text(`${res.student_login_email} is logged in!`)
    //     console.log("LOGIN FUNCTION STILL WORKS!")
    // })
});


// event handler for new student registration 
$('#create_student').on('submit', (evt) => {
    evt.preventDefault();

    // converts student registration form into an object
    // const studentFormValues = $('#student_reg_form').serialize();
    const studentFormValues = { 
        'student_fname': $('#student_fname').val(),
        'student_lname': $('#student_lname').val(),
        'student_email': $('#student_email').val(),
        'private_teacher_name': $('#private_teacher_name').val(),
        'private_teacher_email': $('#private_teacher_email').val(),
        'program_name': $('#program_name').val(),
        'instrument': $('#instrument').val(),
        'student_phone': $('#student_phone').val(),
        'student_password': $('#student_password').val()
    } 

    $.post("/student-portal-create", studentFormValues, (res) => {
        $('#student_added_response').text(
            `Student profile for ${res.student_fname} ${res.student_lname} has been created!`
        );
    });
});

//______________________________________Event for setting practice goals_________________________________________________
$('practice_goal').on('submit', (evt) => {
    evt.preventDefault();

    // converts student registration form into an object
    // const studentFormValues = $('#student_reg_form').serialize();
    const goalFormValues = { 
        'days_goal': $('#days_goal').val(),
        'total_practice_minutes': $('total_practice_minutes').val()
    } 

    $.post("/student-profile", goalFormValues, (res) => {
        $('#total_practice_days').text(
            `${res.days_goal}`
        );
    });
});


//_________________________________________Event for creating logs___________________________________________________

// event handler for creating new practice logs
$('#create_log').on('submit', (evt) => {
    evt.preventDefault();

    const logFormValues = { 
        "log_student_id": $('#log_student_id').val(),
        'log_date': $('#log_date').val(),
        'log_minutes_practiced': $('#log_minutes_practiced').val(),
        'log_pieces_practiced': $('#log_pieces_practiced').val(),
        'log_practice_notes': $('#log_practice_notes').val()
    } 
    console.log(logFormValues)
    $.post("/practice-log", logFormValues, (res) => {
        $('#log_added_response').text(
            `Log for ${res.log_date} has been saved!`
        )
    });
});

//_________________________________________Event for lesson notes___________________________________________________

// event handler for creating new lesson notes
$('#create_note').on('submit', (evt) => {
    console.log("HALPPPPPP");
    evt.preventDefault();

    const noteFormValues = { 
        "note_teacher_id": $('#note_teacher_id').val(),
        "note_student_name": $("#note_student_name").val(),
        'note_date': $('#note_date').val(),
        'note_time': $('#note_time').val(),
        'note_content': $('#note_content').val(),
    } 
    console.log(noteFormValues);
    $.post("/teacher-notes", noteFormValues, (res) => {
        $('#note_added_response').text(
            `note for lesson at ${res.note_time} on ${res.note_date} has been saved!`
        )
    });
});

//_________________________________________Event for sending a text_________________________________________________

$('#message-id').on('submit', (evt) => {
    evt.preventDefault();

    const myMessage = { "my_message": $('#my_message').val() }

    // console.log(myMessage)
    $.post("/api/messages", myMessage, (res) => {
        $('#sms-id').text(
            `Message sent! Reads: ${res.my_message}`
        )
    });
});


// $('.card-link-charts').on('click', (evt) => {
//     evt.preventDefault();
//     console.log(evt.currentTarget.value)

//     let sid = evt.currentTarget.value;
//     console.log(sid)

//     $.getJSON(`/teacher-chart/${sid}`, (res) => {
//         console.log('GET REQUEST 1 HAPPENED WOOOOO')
//         console.log(res.dates_formatted)
//         console.log(res.minutes_practiced)

//         const dates = res.dates_formatted; // give us a list of dates
//         // ["Feb 28", "Feb 27", "Feb 26", "Feb 25", "Feb 24", "Feb 23", "Feb 22"]
//         const practiceTimes = res.minutes_practiced; // associated practice minutes only
//         // [0, 0, 120, 12, 45, 35, 100]
    
//         let myChart2 = document.getElementById("bar-time").getContext('2d');
    
//         let colors2 = ['#FCD5BE;', '#F8B195', '#F67280', '#C06C84', '#A8A0B1', '#6C5B7B', '#355C7D', '#A8A0B1'];
//         let chart2 = new Chart(myChart2, {
//             type: 'bar',
//             data: {
//                 labels: dates.reverse(), 
//                 datasets: [ {
//                     data: practiceTimes.reverse(),
//                     backgroundColor: colors2
//                 }] 
//             },
//             options: {
//                 title: {
//                     text: "How many minutes did you practice per day this week?",
//                     display: true
//                 },
//                 legend: {
//                     display: false
//                 },
//                 scales: {
//                     yAxes: [{
//                         ticks: {
//                             suggestedMin: 0,
//                             suggestedMax: 150
//                         }
//                     }]
//                 }
//             },
//             scales: {
//                 xAxes: [
//                     {
//                         type: 'time',
//                         time: {
//                             unit: 'day',
//                             round: 'day',
//                             displayFormats: {
//                                 day: 'MMM D'
//                             },
//                         },
//                         distribution: 'series'
//                     }
//                 ],
//                 yAxes: [{
//                     ticks: {
//                         beginAtZero: true
//                     }
//                 }]
//             },
//             tooltips: {
//                 callbacks: {
//                     title: (tooltipItem) => {
//                         return moment(tooltipItem.label).format('MMM D');
//                     }
//                 }
//             }    
//         })
//     })
// });

