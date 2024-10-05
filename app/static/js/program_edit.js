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

document.addEventListener('DOMContentLoaded', function() {
    const searchField = document.getElementById('search_field');
    const searchInput = document.getElementById('search_input');
    const table = document.getElementById('program_table');
    const rows = table.getElementsByTagName('tr');

    function filterTable() {
        const filter = searchInput.value.toUpperCase();
        const fieldIndex = searchField.value;

        for (let i = 1; i < rows.length; i++) {
            const row = rows[i];
            const cells = row.getElementsByTagName('td');
            let match = false;

            if (fieldIndex === 'all') {
                const codeMatch = cells[0].textContent.toUpperCase().startsWith(filter);
                const nameMatch = cells[1].textContent.toUpperCase().includes(filter);
                match = codeMatch || nameMatch;
            } else if (fieldIndex === '0') {
                match = cells[0].textContent.toUpperCase().startsWith(filter);
            } else if (fieldIndex === '1') {
                match = cells[1].textContent.toUpperCase().includes(filter);
            }
              else if (fieldIndex === '2'){
                match = cells[2].textContent.toUpperCase().startsWith(filter);
            }


            row.style.display = match ? '' : 'none';
        }
    }

    searchInput.addEventListener('input', filterTable);
    searchField.addEventListener('change', filterTable);
});
