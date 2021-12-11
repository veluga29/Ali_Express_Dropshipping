import Link from 'next/link'
import Head from 'next/head'
import Layout from '../src/components/layout'
import Autocomplete from '../src/components/autocomplete'
import Pagination from '../src/components/pagination'
import Image from 'next/image'

import { useState, useEffect } from "react";
import { useCookies } from "react-cookie"
import axios from 'axios';
import router from 'next/router'


export default function Products({ productsData }) {
  const [cookies, , removeCookie] = useCookies(["access_token"]);
  let access_token = cookies.access_token;
  const [searchText, setSearchText] = useState("");

  useEffect(() => {
    if (!access_token) {
      router.push('/signin');
      return;
    }
    const verifyToken = async () => { 
      try{
        await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/aaa/token`, {
          headers: {
              Authorization: `bearer ${cookies.access_token}`
          }
        });
        let searchText = localStorage.getItem("latestSearchText")
        if (searchText) {
          setSearchText(searchText);
          const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/products?text=${searchText}&page=1`, {
            headers: {  
                Authorization: `bearer ${cookies.access_token}`
            }
          });
          const productsInfo = response.data;
          setTotalPages(productsInfo.information.numberOfPages);
          setProductList(productsInfo.information.items.slice(0, 12)); 
        }
      } catch (error) {
        // Delete access token cookie
        removeCookie('access_token');
        router.push('/signin');
      }
    }
    verifyToken();
  }, [])


  
  const [totalPages, setTotalPages] = useState(null);
  const [productList, setProductList] = useState(productsData);
  const handleChange = ({ target: { value } }) => setSearchText(value);
  const handleSubmit = async (event) => {
    // after submit, we can get final searching text
    // we call API to get the list of searching text products
    // Store the updated list to state so we can apply on the UI (JSX component)
    event.preventDefault();
    try {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/products?text=${searchText}&page=1`, {
        headers: {  
            Authorization: `bearer ${cookies.access_token}`
        }
      });
      const productsInfo = response.data;
      setTotalPages(productsInfo.information.numberOfPages);
      setProductList(productsInfo.information.items.slice(0, 12));
      localStorage.setItem('latestSearchText', searchText);
    } catch (e) {
      console.log(e);
      setProductList(null);
    }
  }

  let products;
  if (productList) {
    const productListArray = productList.map((product: any) => {
      return (
        <li className="col-3" key={product.productId}>
          <div className="card">  
            <Link href={`/product/${product.productId}`}>
              <a>
                <Image
                  className="card-img-top"
                  src={product.imageUrl}
                  height={300}
                  width={315}
                  alt="Product Image" />
              </a>
            </Link>
            <div className="card-body d-flex flex-column justify-content-between">
              <h5 className="card-title">{product.title}</h5>
              <div>
                <p className="card-text">
                  Total Orders: {product.totalOrders || 0}<br/>
                  Average Rating: {product.averageRating || 0}
                </p>
                <Link href={`/product/${product.productId}`}>
                  <a className="btn btn-warning alert-warning">See item detail</a>
                </Link>
              </div>
            </div>
          </div>
        </li>
      )
    });
    products = (
      <div className="container-fluid">
        <div >
          <ul className="list-unstyled row g-5">
            {productListArray}          
          </ul>
        </div>
        <div className="row">
          <Pagination searchText={searchText} totalPages={totalPages} setProductList={setProductList} />
        </div>
      </div>
    );
    
  } else {
    products = (
      <div className="d-flex justify-content-center align-items-center" style={{height: "580px"}}>
        <h2>Please search your products</h2>
      </div>
    )
  }

  return (
    <Layout>
      <Head>
        <title>Products</title>
      </Head>
      <section className="container-fluid">
        <form className="offset-2 col-md-4 d-flex mb-5" onSubmit={handleSubmit}>
          <input 
            className="form-control form-control-lg me-2"
            name="search" 
            type="text" 
            value={searchText} 
            autoComplete="off"
            list="datalistOptions"
            onChange={handleChange} 
            placeholder="Search items you want" />
          <Autocomplete searchText={searchText} />
          <button className="btn btn-warning text-white fs-5" type="submit">Search</button>
        </form>
      </section>
      <section>
        {products}
      </section>
    </Layout>
  )
}
