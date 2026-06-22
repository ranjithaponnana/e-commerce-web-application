import React,{useEffect,useState} from "react";
import axios from "axios";


function Orders(){


const [orders,setOrders]=useState([]);



useEffect(()=>{


const token =
localStorage.getItem("token");


axios.get(

"http://127.0.0.1:5000/orders",

{
headers:{
Authorization:`Bearer ${token}`
}
}

)

.then(res=>{

setOrders(res.data);

});


},[]);




return(

<div>

<h2>
My Orders
</h2>


{

orders.map(order=>(

<div key={order[0]}>

<p>
Order ID: {order[0]}
</p>


<p>
Status: {order[3]}
</p>


</div>

))

}


</div>

)

}


export default Orders;
