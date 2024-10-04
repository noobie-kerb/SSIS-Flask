document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.edit-btn');
    
    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const college_code = this.getAttribute('data-code');
            const college_name = this.getAttribute('data-name');
            
            document.getElementById('edit_college_code').value = college_code;
            document.getElementById('edit_college_name').value = college_name;

            const form = document.getElementById('editCollegeForm');
            form.action = `/edit_college/${college_code}`;
        });
    });
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
