document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.edit-btn');
    
    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const student_id = this.getAttribute('data-id');
            const first_name = this.getAttribute('data-first-name');
            const last_name = this.getAttribute('data-last-name')
            const program = this.getAttribute('data-program');
            const year = this.getAttribute('data-year');
            const gender = this.getAttribute('data-gender');
            
            document.getElementById('student_id').value = student_id;
            document.getElementById('first_name').value = first_name;
            document.getElementById('last_name').value = last_name;
            document.getElementById('course').value = program;
            document.getElementById('year').value = year;
            document.getElementById('gender').value = gender;

            const form = document.getElementById('editStudentForm');
            form.action = `/edit_student/${student_id}`;
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.delete-btn');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const program_code = this.getAttribute('data-code');
            
            const deleteForm = document.getElementById('deleteProgramForm');
            deleteForm.action = `/delete_program/${program_code}`;
        });
    });
});
