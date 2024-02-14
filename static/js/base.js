// expands navbar
console.log('loaded')
const expandNavbar = () => {
	const burgerMenu = document.querySelector('.navbar-burger');
	burgerMenu.addEventListener('click', (e) => {
		const menuDropdown = document.getElementById('generalNavBar');
		burgerMenu.classList.toggle('is-active');
		menuDropdown.classList.toggle('is-active');
	});
}
document.addEventListener('DOMContentLoaded', expandNavbar);