import React,{useState} from "react";
import axios from "axios";


function Register(){


const[username,setUsername]=useState("");

const[email,setEmail]=useState("");

const[password,setPassword]=useState("");




function register(){


axios.post(

"http://127.0.0.1:5000/register",

{
username,
email,
password
}

)

.then(res=>{

alert(res.data.message);

});


}




return(

<div>


<h2>
Register
</h2>


<input

placeholder="Username"

onChange={
e=>setUsername(e.target.value)
}

/>


<br/>


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


<button onClick={register}>
Register
</button>


</div>

)

}


export default Register;
