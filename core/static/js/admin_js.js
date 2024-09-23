const open_profile_options = () => {
    const dropdown_activator = document.querySelector('#dropdown_activator');
    const dropdown = document.querySelector('#dropdown');

    dropdown_activator.addEventListener('click', () => {
        dropdown.classList.toggle('active');
        (dropdown.classList.contains('active')) ? dropdown_activator.classList.add('hover') : dropdown_activator.classList.remove('hover');
    });
}
open_profile_options();


const openImageDetail = () => {
    const images = document.querySelectorAll('#gallery .image');
    const modal = document.getElementById('modal');
    const modalImg = document.getElementById('modal-img');
    const captionText = document.getElementById('caption');
    const selectBtn = document.getElementById('select-image-btn');
    const span = document.getElementsByClassName('close')[0];

    images.forEach(image => {
        image.addEventListener('click', function() {
            modal.style.display = 'block';
            modalImg.src = this.querySelector('img').src;
            captionText.innerHTML = this.getAttribute('data-info');

            // Aquí puedes actualizar un campo oculto en el formulario con la URL de la imagen seleccionada
            const imageUrl = this.querySelector('img').src;
            selectBtn.addEventListener('click', function() {
                document.getElementById('id_photo').value = imageUrl; // Actualiza el campo 'photo' del formulario con la URL
                modal.style.display = 'none';
            });
        });
    });

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
}

// Inicializa la función al cargar la página
document.addEventListener('DOMContentLoaded', function() {
    openImageDetail();
});