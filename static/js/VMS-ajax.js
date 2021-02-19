//______________________________________Event for homepage redirects________________________________________________
$('#homepage-button').on('submit', (evt) => {
    evt.preventDefault();
});

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
    console.log("!!!!!!************");

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
        console.log("HEWOOOOOOOOOO!!!!")
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
    console.log("!!!!!!************");

    // converts student registration form into an object
    // const studentFormValues = $('#student_reg_form').serialize();
    const studentFormValues = { 
        'student_fname': $('#student_fname').val(),
        'student_lname': $('#student_lname').val(),
        'student_email': $('#student_email').val(),
        'private_teacher': $('#private_teacher').val(),
        'program_name': $('#program_name').val(),
        'instrument': $('#instrument').val(),
        'student_password': $('#student_password').val()
    } 

    $.post("/student-portal-create", studentFormValues, (res) => {
        $('#student_added_response').text(
            `Student profile for ${res.student_fname} ${res.student_lname} has been created!`
        );
    });
});


//_________________________________________Event for creating logs___________________________________________________

// event handler for creating new practice logs
$('#create_log').on('submit', (evt) => {
    evt.preventDefault();
    console.log("BLAHHHHH")

    const logFormValues = { 
        'log_date': $('#log_date').val(),
        'log_start_time': $('#log_start_time').val(),
        'log_end_time': $('#log_end_time').val(),
        'log_pieces_practiced': $('#log_pieces_practiced').val(),
        'log_practice_notes': $('#log_practice_notes').val()
    } 

    $.post("/practice-log", logFormValues, (res) => {
        $('#log_added_response').text(
            `Log for ${res.log_date} has been saved!`
        )
        console.log("UGHHHHHHHH")
    });
});