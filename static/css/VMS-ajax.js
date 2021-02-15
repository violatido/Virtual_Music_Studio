// event handler for login verification
$('#login_form').on('submit', (evt) => {
    evt.preventDefault();

    const loginFormValues = {
        'login_email': $('#login_email').val(),
        'login_password': $('#login_password').val()
    }

    $.post("/", loginFormValues, (res))
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
    $.post("/register-teacher", teacherFormValues, (res) => {
        $('#teacher_added_response').text(
            `Teacher profile for ${res.teacher_fname} ${res.teacher_lname} has been created!`
        )
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

    $.post("/register-student", studentFormValues, (res) => {
        $('#student_added_response').text(
            `student profile for ${res.student_fname} ${res.student_lname} has been created!`
        )
    })
})