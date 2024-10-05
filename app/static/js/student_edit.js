document.addEventListener('DOMContentLoaded', function () {
    const editModal = document.getElementById('editStudentModal');
    
    if (editModal) {
        editModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
        
            const student_id = button.getAttribute('data-id');
            const first_name = button.getAttribute('data-first-name');
            const last_name = button.getAttribute('data-last-name');
            const program = button.getAttribute('data-program');
            const year = button.getAttribute('data-year');
            const gender = button.getAttribute('data-gender');
            
            const modalForm = editModal.querySelector('#editStudentForm');
            
            if (modalForm) {
                modalForm.action = `/edit_student/${student_id}`;
                modalForm.querySelector('#edit_student_id').value = student_id || '';
                modalForm.querySelector('#edit_first_name').value = first_name || '';
                modalForm.querySelector('#edit_last_name').value = last_name || '';
                modalForm.querySelector('#course').value = program || '';
                modalForm.querySelector('#edit_year').value = year || '';
                modalForm.querySelector('#edit_gender').value = gender || '';
            }
        });
    } else {
        console.error('Edit Student Modal not found');
    }
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
