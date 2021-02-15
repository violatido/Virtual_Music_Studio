// event handler for teacher login verification
$('#teacher_login_form').on('submit', (evt) => {
    evt.preventDefault();

    const loginFormValues = {
        'teacher_login_email': $('#teacher_login_email').val(),
        'teacher_login_pw': $('#teacher_login_pw').val()
    }

    $.post("/teacher-portal", loginFormValues, (res) => {
        $('#teacher_added_response').text("Logged in!")
    })
})


// event handler for new teacher registration 
$('#teacher_reg_form').on('submit', (evt) => {
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
    $.post("/student-portal", teacherFormValues, (res) => {
        $('#teacher_added_response').text(
            `Teacher profile for ${res.teacher_fname} ${res.teacher_lname} has been created!`
        )
    })
})

// event handler for student login
$('#student_login_form').on('submit', (evt) => {
    evt.preventDefault();

    const loginFormValues = {
        'student_login_email': $('#student_login_email').val(),
        'student_login_pw': $('#student_login_pw').val()
    }

    $.post("/student-portal", loginFormValues, (res) => {
        $('#student_added_response').text("Logged in!")
    })
})



// event handler for new student registration 
$('#student_reg_form').on('submit', (evt) => {
    evt.preventDefault();

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

    $.post("/student-portal", studentFormValues, (res) => {
        $('#student_added_response').text(
            `student profile for ${res.student_fname} ${res.student_lname} has been created!`
        )
    })
})