
// event handler for new teacher registration 
$('#teacher-reg-form').on('submit', (evt) => {
    evt.preventDefault();

    // converts teacher registration form into an object
    // const teacherFormValues = $('#teacher-reg-form').serialize();
    const teacherFormValues = { 
        'teacher-fname': $('#teacher-fname').val(),
        'teacher-lname': $('#teacher-lname').val(),
        'teacher-email': $('#teacher-email').val(),
        'teacher-phone': $('#teacher-phone').val(),
        'teacher-password': $('#teacher-password').val()
    } 
    $.post("/sign-up", teacherFormValues, (res) => {
        $('#teacher-added-response').text(`Teacher profile for ${res.teacher-fname} ${res.teacher-lname} has been created!`)
    })
})

// event handler for new student registration 
$('#student-reg-form').on('submit', (evt) => {
    evt.preventDefault();

    // converts student registration form into an object
    // const studentFormValues = $('#student-reg-form').serialize();
    const studentFormValues = { 
        'student-fname': $('#student-fname').val(),
        'student-lname': $('#student-lname').val(),
        'student-email': $('#student-email').val(),
        'private-teacher': $('#private-teacher').val(),
        'program-name': $('#program-name').val(),
        'instrument': $('#instrument').val(),
        'student-password': $('#student-password').val()
    } 
    $.post("/sign-up", studentFormValues, (res) => {
        $('#student-added-response').text(`student profile for ${res.student-fname} ${res.student-lname} has been created!`)
    })
})