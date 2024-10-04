document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.edit-btn');
    
    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const program_code = this.getAttribute('data-code');
            const program_name = this.getAttribute('data-name');
            const college = this.getAttribute('data-    college')
            
            document.getElementById('edit_program_code').value = program_code;
            document.getElementById('edit_program_name').value = program_name;
            document.getElementById('college_code').value = college;

            const form = document.getElementById('editProgramForm');
            form.action = `/edit_program/${program_code}`;
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
