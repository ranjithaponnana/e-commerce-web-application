import React,{useState} from "react";
import axios from "axios";


function Login(){


const[email,setEmail]=useState("");

const[password,setPassword]=useState("");



function login(){


axios.post(

"http://127.0.0.1:5000/login",

{
email,
password
}

)

.then(res=>{


localStorage.setItem(
"token",
res.data.token
);


alert("Login successful");


});


}



return(

<div>

<h2>
Login
</h2>


<input

placeholder="Email"

onChange={
e=>setEmail(e.target.value)
}

/>


<br/>


<input

type="password"

placeholder="Password"

onChange={
e=>setPassword(e.target.value)
}

/>


<br/>


<button onClick={login}>
Login
</button>


</div>

)

}


export default Login;
