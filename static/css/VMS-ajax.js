
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