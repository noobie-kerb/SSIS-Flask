document.addEventListener('DOMContentLoaded', function () {
    const editModal = document.getElementById('editCollege');
    
    if (editModal) {
        editModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            
            const college_code = button.getAttribute('data-code');
            const college_name = button.getAttribute('data-name');
            
            const modalForm = editModal.querySelector('#editCollegeForm');
            
            if (modalForm) {
                modalForm.querySelector('#edit_college_code').value = college_code || '';
                modalForm.querySelector('#edit_college_name').value = college_name || '';
                
                modalForm.action = `/edit_college/${college_code}`;
            }
        });
    } else {
        console.error('Edit College Modal not found');
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.delete-btn');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const collegeCode = this.getAttribute('data-code');
         
            const deleteForm = document.getElementById('deleteCollegeForm');
            deleteForm.action = `/delete_college/${collegeCode}`;
        });
    });
});
