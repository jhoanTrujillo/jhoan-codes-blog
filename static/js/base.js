// expands navbar
const expandNavbar = () => {
	const burgerMenu = document.querySelector('.navbar-burger');
	burgerMenu.addEventListener('click', () => {
		const menuDropdown = document.getElementById('generalNavBar');
		burgerMenu.classList.toggle('is-active');
		menuDropdown.classList.toggle('is-active');
	});
};

document.addEventListener('DOMContentLoaded', expandNavbar);

const toggleModal = () => {
	let toggleButtons = document.querySelectorAll('[data-close-modal]');
	for (let button of toggleButtons) {
		button.addEventListener("click", () => {
			button.closest(".modal").classList.toggle("is-active")
		});
	}
}

document.addEventListener('DOMContentLoaded', toggleModal);