let theme = localStorage.getItem('theme')
if (theme) {
    document.querySelector('body').classList.add(theme)
}
const btn = document.querySelector('#btn');
btn.addEventListener('click', () => {
    document.querySelector('body').classList.toggle('dark-mode');
    if (theme === 'dark-mode') {
        localStorage.setItem('theme', 'light-mode')
    } else {
        localStorage.setItem('theme', 'dark-mode')
    }
})