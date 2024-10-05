document.addEventListener('DOMContentLoaded', function () {
    const editModal = document.getElementById('editProgram');
    
    if (editModal) {
        editModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            
            const program_code = button.getAttribute('data-code');
            const program_name = button.getAttribute('data-name');
            const college = button.getAttribute('data-college');

            const modalForm = editModal.querySelector('#editProgramForm');
            
            if (modalForm) {
                modalForm.querySelector('#edit_program_code').value = program_code || '';
                modalForm.querySelector('#edit_program_name').value = program_name || '';
                modalForm.querySelector('#college_code').value = college || '';
                
                modalForm.action = `/edit_program/${program_code}`;
            }
        });
    } else {
        console.error('Edit Program Modal not found');
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
