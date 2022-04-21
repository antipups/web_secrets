const file_input = document.querySelector('#file_load')
const label_to_fileuploader = document.querySelector('.label_file_load')

const submit_file_form = document.querySelector('.submit_file')

file_input.addEventListener('change', (event) => {
    const file = file_input.files[0]
    if (file.size > max_file_size) {
        label_to_fileuploader.textContent = 'Размер файла слишком большой (больше 100МБ)'
        file_input.value = ''
        submit_file_form.disabled = true
    } else {
        label_to_fileuploader.textContent = file.name.length > 20 ? file.name.slice(0, 20) + '...' : file.name
        // label_to_fileuploader.style.color = 'black'
        submit_file_form.disabled = false
    }
})




