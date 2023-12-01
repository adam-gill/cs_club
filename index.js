function openMenu() {
    document.body.classList += " menu--open"
    console.log("open")
}

function closeMenu() {  
    document.body.classList.remove('menu--open')
    console.log("close")
}