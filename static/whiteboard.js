'use strict';

// const saveNote = document.querySelector("#save-note");

// saveNote.addEventListener('click', (evt) => {
//     evt.preventDefault();
//     const id = document.querySelector("#id").value;
//     const title = document.querySelector("#title").value;
//     const body = document.querySelector("#body").innerHTML;               
//     console.log(id, title, body);

//     fetch('/update-note')
//     .then((response) => response.text())
//     .then((info) => {
//         const nInfo = JSON.parse(info);
//         console.log(nInfo);
//     });
// });
const allNotes = document.querySelectorAll("#note-forms form")
for (const noteForm of allNotes) {
    
    noteForm.addEventListener('submit', (evt) => {
        evt.preventDefault();
        const noteId = evt.target.id;
        // const id = document.querySelector("#note-id").value;
        // console.log(id)
    
        const formInputs = {
          id: noteId,
          title: document.querySelector(`#n-title${noteId}`).value,
          body: document.querySelector(`#n-body${noteId}`).value,
        };
        console.log(formInputs)
      
        fetch('/update-note', {
          method: 'POST',
          body: JSON.stringify(formInputs),
          headers: {
            'Content-Type': 'application/json',
          },
        })
          .then((response) => response.json())
          .then((responseJson) => {
            alert(responseJson.status);
          });
      });

}
// document.querySelector('form').addEventListener('submit', (evt) => {
//     evt.preventDefault();
//     console.log(evt.target)
//     // const id = document.querySelector("#note-id").value;
//     // console.log(id)

//     const formInputs = {
//       id: document.querySelector("#note-id").value,
//       title: document.querySelector("#n-title").value,
//       body: document.querySelector("#n-body").innerHTML,
//     };
//     console.log(formInputs)
  
//     fetch('/update-note', {
//       method: 'POST',
//       body: JSON.stringify(formInputs),
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     })
//       .then((response) => response.json())
//       .then((responseJson) => {
//         alert(responseJson.status);
//       });
//   });