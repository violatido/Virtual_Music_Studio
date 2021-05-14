"use strict"


function isEmptyObject(o, q='any') {
    /*
        This function will return true
        if none of the attributes of the
        provided obj are null.

        Parameters:
        o: object
        q: str, default = 'any'
            query, either 'all' or 'any'

        Examples:
        ```js
        >> z = {'x':'abc', 'y':123, 'z':null}
        >> isEmptyObject(z, 'all')
        false

        >> isEmptyObject(z, 'any')
        true

        // By default, q='any' so
        >> isEmptyObject(z)
        true
        ```
    */

  // If all are null
    if (q==='all'){
        return Object.keys(o).every(function(x) {
            return o[x]===''||o[x]===null;  // or just "return o[x];" for falsy values
        });
    }

    // If any are null
    else if (q==='any'){
        // Iterate through elements
        for (let key of Object.keys(o)){
            let val = o[key];

            if (val==='' || val===null){
                return true;
            }
        }
    return false;
    }

}


// Form submission only allowed once the page is finished loading...
document.addEventListener("DOMContentLoaded", function() {

    //________________________________________Events for teacher registration______________________________________
// event handler for new teacher registration

    $('#create_teacher__submit').on('click', (evt) => {

        evt.preventDefault();

        // converts teacher registration form into an object
        const teacherFormValues = {
            'teacher_fname': $('#teacher_fname').val(),
            'teacher_lname': $('#teacher_lname').val(),
            'teacher_email': $('#teacher_email').val(),
            'teacher_phone': $('#teacher_phone').val(),
            'teacher_password': $('#teacher_password').val()
        }

        //  If not attr, do nothing
        if (isEmptyObject(teacherFormValues, 'any')){

            $.post('/teacher-portal', teacherFormValues, (res) => {
                $('#teacher_reg_buttonTitle').text(
                    `Registration Unsuccessful!`
                );

                $('#teacher_added_response_p1').text(
                    `No values provided.`
                );
            });

        // Return to escape the other stuff
        return
        }

        //  The following code isn't working – Reset each input on its own
        // document.getElementById('#create_teacher').reset()
        $('#teacher_fname').val('');
        $('#teacher_lname').val('');
        $('#teacher_email').val('');
        $('#teacher_phone').val('');
        $('#teacher_password').val('');

        $.post('/teacher-portal-create', teacherFormValues, (res) => {
            if (res.status === 'ok') {
                $('#teacher_reg_buttonTitle').text(
                    `Teacher profile for ${res.full_name} has been created!`
                );
                $('#teacher_added_response_p2').text(
                    `Please sign in (from the current page you're on). (We know this is a bit cumbersome.)`
                );
                // Populate the sign in form
                $('#teacher_login_email').val(res.email);
                $('#teacher_login_pw').val(res.pw);
            }
            else if (res.status === 'error- email already in use') {
                $('#teacher_reg_buttonTitle').text(
                    `Registration Unsuccessful!`
                );
                $('#teacher_added_response_p2').text(
                    `Email already in use.)`
                );
            }
            else if (res.status === 'error- no teacher in database') {
                $('#teacher_reg_buttonTitle').text(
                    `Registration Unsuccessful!`
                );
                $('#teacher_added_response_p2').text(
                    `No teacher is signed up with that email. 
                    Please wait until your teacher makes a virtual studio before signing up!.`
                );
            }
        });
    });


    //________________________________________Event for student registration______________________________________

    // event handler for new student registration
    $('#create_student__submit').on('click', (evt) => {
        evt.preventDefault();

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
        //  If not attr, do nothing
        if (isEmptyObject(studentFormValues, 'any')){

        $.post('/student-portal', studentFormValues, (res) => {

            $('#student_reg_buttonTitle').text(
                `Registration Unsuccessful!`
            );

            $('#student_added_response').text(
                `No values provided.`
            );
        });
        // Return to escape the other stuff
        return
    }
        // Set values to null
        $('#student_fname').val('');
        $('#student_lname').val('');
        $('#student_email').val('');
        $('#private_teacher_name').val('');
        $('#private_teacher_email').val('');
        $('#program_name').val('');
        $('#instrument').val('');
        $('#student_phone').val('');
        $('#student_password').val('');

        $.post('/student-portal-create', studentFormValues, (res) => {
            if (res.status === 'ok') {
                $('#student_reg_buttonTitle').text(
                    `Student profile for ${res.full_name} has been created!`
                );
                $('#student_added_response_p2').text(
                    `Please sign in (from the current page you're on). (We know this is a bit cumbersome.)`
                );
                // Populate the sign in form
                $('#student_login_email').val(res.email);
                $('#student_login_pw').val(res.pw);
            }
            else if (res.status === 'error') {
                $('#student_reg_buttonTitle').text(
                    `Registration unsuccessful!`
                );
                $('#student_added_response_p2').text(
                    `Email already in use.)`
                ); 
            }
        });

    });

    //_________________________________________Event for creating logs___________________________________________________

    // event handler for creating new practice logs
    $('#create_log').on('submit', (evt) => {
        evt.preventDefault();

        const logFormValues = {
            'log_student_id': $('#log_student_id').val(),
            'log_date': $('#log_date').val(),
            'log_minutes_practiced': $('#log_minutes_practiced').val(),
            'log_pieces_practiced': $('#log_pieces_practiced').val(),
            'log_practice_notes': $('#log_practice_notes').val()
        }
        //  If not attr, do nothing
        if (isEmptyObject(logFormValues, 'any')){
            $.post('/student-profile', logFormValues, (res) => {
                $('#log_added_response').text(
                    `Empty values... Log has not been saved.`
                );
            });
        
        return

    }

        $.post('/practice-log', logFormValues, (res) => {
            $('#log_added_response').text(
                `A new practice log has been submitted!`
            );
        });

        // Reset (manually)
        $('#log_date').val('');
        $('#log_minutes_practiced').val('');
        $('#log_pieces_practiced').val('');
        $('#log_practice_notes').val('');

    });


    //_________________________________________Event for lesson notes___________________________________________________

    // event handler for creating new lesson notes
    $('#create_note').on('submit', (evt) => {
        evt.preventDefault();

        const noteFormValues = {
            'note_teacher_id': $('#note_teacher_id').val(),
            'note_student_name': $("#note_student_name").val(),
            'note_date': $('#note_date').val(),
            'note_time': $('#note_time').val(),
            'note_content': $('#note_content').val(),
        }


        //  If not attr, do nothing
        if (isEmptyObject(noteFormValues, 'any')){

        $.post('/teacher-notes', logFormValues, (res) => {
            $('#note_added_response').text(
                `Empty values... Note has not been saved.`
            );
        });
        
        return {}
        }

        $.post('/teacher-notes', noteFormValues, (res) => {
            $('#note_added_response').text(
                `New lesson note has been submitted!`
            );
        });

        document.getElementById('#create_note').reset()
    });

    //_________________________________________Event for sending a text_________________________________________________

    $('#message-id').on('submit', (evt) => {
        evt.preventDefault();

        const studentTexted = {
            'phone_dropdown_id': $('#phone_dropdown_id').val(),
            'message_content': $('#message_content').val()
        }

        $.post('/api/messages', studentTexted, (res) => {
            $('#sms-id').text(
                `Your message: ${res.message_content}`);
        });

        document.getElementById('message-id').reset()

    });

});
