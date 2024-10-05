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

document.addEventListener('DOMContentLoaded', function() {
    const searchField = document.getElementById('search_field');
    const searchInput = document.getElementById('search_input');
    const table = document.getElementById('college_table');
    const rows = table.getElementsByTagName('tr');

    function filterTable() {
        const filter = searchInput.value.toUpperCase();
        const fieldIndex = searchField.value;

        for (let i = 1; i < rows.length; i++) {
            const row = rows[i];
            const cells = row.getElementsByTagName('td');
            let match = false;

            if (fieldIndex === 'all') {
                // Search all fields
                const codeMatch = cells[0].textContent.toUpperCase().startsWith(filter);
                const nameMatch = cells[1].textContent.toUpperCase().includes(filter);
                match = codeMatch || nameMatch;
            } else if (fieldIndex === '0') {
                match = cells[0].textContent.toUpperCase().startsWith(filter);
            } else if (fieldIndex === '1') {
                match = cells[1].textContent.toUpperCase().includes(filter);
            }

            row.style.display = match ? '' : 'none';
        }
    }

    searchInput.addEventListener('input', filterTable);
    searchField.addEventListener('change', filterTable);
});