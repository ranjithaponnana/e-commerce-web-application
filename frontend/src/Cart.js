import React,{useEffect,useState} from "react";
import axios from "axios";


function Cart(){


const [cart,setCart]=useState([]);



function getCart(){


const token = localStorage.getItem("token");


axios.get(

"http://127.0.0.1:5000/cart",

{
headers:{
Authorization:`Bearer ${token}`
}
}

)

.then(res=>{

setCart(res.data);

});


}



useEffect(()=>{

getCart();

},[]);




return(

<div>


<h2>
My Cart
</h2>



{

cart.map((item,index)=>(

<div key={index}>


<h3>
{item[0]}
</h3>


<p>
Price: ₹{item[1]}
</p>


</div>


))

}



</div>

)

}


export default Cart;
