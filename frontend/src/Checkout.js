import React from "react";
import axios from "axios";


function Checkout(){


function placeOrder(productId){


const token = localStorage.getItem("token");


axios.post(

"http://127.0.0.1:5000/orders",

{
product_id: productId
},

{
headers:{
Authorization:`Bearer ${token}`
}
}

)

.then(res=>{

alert(res.data.message);

});


}



return(

<div>

<h2>
Checkout
</h2>


<p>
Proceed with your order
</p>


<button
onClick={()=>placeOrder(1)}
>

Place Order

</button>


</div>

)

}


export default Checkout;
