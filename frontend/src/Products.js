import React, {useEffect, useState} from "react";
import axios from "axios";


function Products(){


const [products,setProducts] = useState([]);



function getProducts(){


axios.get(
"http://127.0.0.1:5000/products"
)

.then(res=>{

setProducts(res.data);

});


}



useEffect(()=>{

getProducts();

},[]);




function addCart(id){


const token = localStorage.getItem("token");


axios.post(

"http://127.0.0.1:5000/cart",

{
product_id:id
},

{
headers:{
Authorization:`Bearer ${token}`
}
}

)

.then(()=>{

alert("Product added to cart");

});


}




return(

<div>


<h2>
Products
</h2>



{

products.map(product=>(

<div key={product[0]}>


<h3>
{product[1]}
</h3>


<p>
{product[2]}
</p>


<p>
Price: ₹{product[3]}
</p>



<button
onClick={
()=>addCart(product[0])
}
>

Add To Cart

</button>


</div>


))

}


</div>

)

}


export default Products;
