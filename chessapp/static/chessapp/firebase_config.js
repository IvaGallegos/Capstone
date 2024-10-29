


import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app-compat.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore-compat.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-auth-compat.js";

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