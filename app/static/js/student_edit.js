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
    const deleteForm = document.getElementById('deleteStudentForm');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const studentId = this.getAttribute('data-id');
            deleteForm.action = `/delete_student/${studentId}`;
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const searchField = document.getElementById('search_field');
    const searchInput = document.getElementById('search_input');
    const table = document.getElementById('student_table');
    const rows = table.getElementsByTagName('tr');

    function filterTable() {
        const filter = searchInput.value.toUpperCase();
        const fieldIndex = searchField.value;

        for (let i = 1; i < rows.length; i++) {
            const row = rows[i];
            const cells = row.getElementsByTagName('td');
            let match = false;

            if (fieldIndex === 'all') {
                const IDMatch = cells[0].textContent.toUpperCase().includes(filter);
                const FirstNameMatch = cells[1].textContent.toUpperCase().includes(filter);
                const LastNameMatch = cells[2].textContent.toUpperCase().includes(filter);
                const ProgramMatch = cells[3].textContent.toUpperCase().startsWith(filter);
                const YearMatch = cells[4].textContent.toUpperCase().startsWith(filter);
                const GenderMatch = cells[5].textContent.toUpperCase().startsWith(filter);
                
                match = IDMatch || FirstNameMatch || LastNameMatch || ProgramMatch || YearMatch || GenderMatch;
            } else if (fieldIndex === '0') {
                match = cells[0].textContent.toUpperCase().includes(filter);
            } else if (fieldIndex === '1') {
                match = cells[1].textContent.toUpperCase().includes(filter);
            }
              else if (fieldIndex === '2'){
                match = cells[2].textContent.toUpperCase().includes(filter);
            }
            else if (fieldIndex === '3'){
                match = cells[3].textContent.toUpperCase().startsWith(filter);
            }
            else if (fieldIndex === '4'){
                match = cells[4].textContent.toUpperCase().startsWith(filter);
            }
            else if (fieldIndex === '5'){
                match = cells[5].textContent.toUpperCase().startsWith(filter);
            }

            row.style.display = match ? '' : 'none';
        }
    }

    searchInput.addEventListener('input', filterTable);
    searchField.addEventListener('change', filterTable);
});