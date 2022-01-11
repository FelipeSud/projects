function getAdmins(map){
    let admins = [];
    for ([key, value] of map){
        if (value === 'Admin'){
            admins.push(key);
        }
    }
    return admins;
}

const usuarios = new Map();

usuarios.set('Felipe', 'Admin');
usuarios.set('Nathália', 'Admin');
usuarios.set('Camila', 'User');
usuarios.set('Karina', 'Admin');
usuarios.set('David', 'Admin');
usuarios.set('Douglas', 'User');
usuarios.set('Tanner', 'Admin');
usuarios.set('Nathan', 'Admin');
usuarios.set('Vinicius', 'User');
usuarios.set('Siblon', 'Admin');
usuarios.set('Moroni', 'User');
usuarios.set('Néfi', 'User');
usuarios.set('Joseph', 'User');
usuarios.set('Dallin', 'Admin');

console.log(getAdmins(usuarios));