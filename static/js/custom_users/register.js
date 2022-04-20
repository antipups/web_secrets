const key_generate_buttom = document.querySelector('div.key_generate')
const keys_div = document.querySelector('div.keys')
const keys_popup = document.querySelector('div.keys_popup')
const keys_divs = [document.querySelector('div.public_key'),
                   document.querySelector('div.private_key'),]
const open_popup_class_name = 'open_popup'
const key_paste_button = document.querySelector('div.keys___paste_keys')


key_generate_buttom.addEventListener('click', (event) => {
    keys_div.style.display = 'flex'
    window.scrollTo({ left: 0, top: document.body.scrollHeight, behavior: "smooth" });
    setTimeout(() => {
        keys_div.children[0].classList.add('swing')
    }, 300)
})


for (const key of keys_divs) {
    key.addEventListener('click', (event) => {
        navigator.clipboard.writeText(key.textContent)
        open_keys_popup()
    })
}


function open_keys_popup() {
    keys_popup.classList.add(open_popup_class_name)
    setTimeout(close_keys_popup, 5000)
}


function close_keys_popup() {
    if (keys_popup.classList.contains(open_popup_class_name))
        keys_popup.classList.remove(open_popup_class_name)
}


keys_popup.addEventListener('click', (event) => {
    close_keys_popup()
})


key_paste_button.addEventListener('click', (event) => {
    const private_key = document.querySelector('#id_private_key')
    private_key.value = keys_divs[1].textContent
    const public_key = document.querySelector('#id_public_key')
    public_key.value = keys_divs[0].textContent
    window.scrollTo({ left: 0, top: 0, behavior: "smooth" });
    navigator.clipboard.writeText(keys_divs[0].textContent)
    open_keys_popup()
})