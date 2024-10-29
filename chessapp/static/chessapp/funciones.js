import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app-compat.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore-compat.js";
import { getAuth, signOut } from 'https://www.gstatic.com/firebasejs/10.14.0/firebase-auth.js';


//Configuración de firebase
const firebaseApp = firebase.initializeApp({
    apiKey: "AIzaSyB2_bx_Cik5pDrL5GhS5mSUMve13BLtqV0",
    authDomain: "chess-8911b.firebaseapp.com",
    projectId: "chess-8911b",
    storageBucket: "chess-8911b.appspot.com",
    messagingSenderId: "928989868620",
    appId: "1:928989868620:web:07ff1cc1c2ff08e382fae9",
    measurementId: "G-3LHBN4WTVE"});

const db = firebaseApp.firestore();
const auth = firebaseApp.auth();


//Funcion para cerrar funcion en firebase
function logout() {
    // Cerrar sesión en Firebase
    firebase.auth().signOut().then(() => {
        alert("Sesión cerrada con éxito.");
        window.location.href = "/"; // Redirige a la página de inicio
    }).catch((error) => {
        alert("Error al cerrar sesión: " + error.message);
    });
}

//Funcion para ingreso de usuario registrado
function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
        alert("Bienvenido: " + email);
        window.location.href = "/menu/"; // Redirige al menú
    })
    .catch((error) => {
        var errorMessage = error.message;
        alert("Error: " + errorMessage);
    });
}
//Funcion para registro en firebase
function register() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    if (name === "") {
        alert("Por favor, ingrese su nombre");
        return;
    }

    var emailPattern = /[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,3}$/;
    if (!emailPattern.test(email)) {
        alert("Por favor, ingrese un correo electrónico válido");
        return;
    }

    var passwordPattern = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}/;
    if (!passwordPattern.test(password)) {
        alert("La contraseña debe tener al menos 8 caracteres, una letra mayúscula y un número");
        return;
    }

    firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
        var user = userCredential.user;
        alert("Usuario registrado con éxito: " + user.email);
        window.location.href = "/menu/";
    })
    .catch((error) => {
        var errorMessage = error.message;
        alert("Error: " + errorMessage);
    });
}