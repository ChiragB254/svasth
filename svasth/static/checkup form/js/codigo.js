const formulario = document.querySelector('.form-group')

cargarEventListeners()
function cargarEventListeners(){
    formulario.addEventListener('submit', EnviarForm);
}


function EnviarForm(e) {
    e.preventDefault();
    
    // Obtener datos del formulario
    const nombre = document.querySelector('#nombre-form').value;
    const email = document.querySelector('#email-form').value;

    // if (!nombre|| !email ) {
       
    //     Swal.fire({
    //         icon: 'error',
    //         title: 'Oops...',
    //         text: 'Form sdubmitted successfully',
    //       })
          
    // } else {
    //     if(/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(email)){
    //         Swal.fire({
    //             title: `Hello ${nombre} your form has been submitted successfully for checkup `,
    //             width: 600,
    //             padding: '3em',
    //             background: '#fff url(/images/trees.png)',
    //             backdrop: `
    //               rgba(0,0,123,0.4)
    //               url("../images/nyan-cat.gif")
    //               left top
    //               no-repeat
    //             `
    //           })
    //     }          
    // }

    formulario.reset();
}