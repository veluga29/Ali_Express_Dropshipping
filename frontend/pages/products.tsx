import Link from 'next/link'
import Head from 'next/head'
import Layout from '../src/components/layout'
import Autocomplete from '../src/components/autocomplete'
import Pagination from '../src/components/pagination'
import Image from 'next/image'
import styles from '/styles/products.module.css'

import { useState, useEffect } from "react";
import { useCookies } from "react-cookie"
import axios from 'axios';
import router from 'next/router'

export default function Products({ productsData }: any) {
  const [cookies, , removeCookie] = useCookies(["access_token"]);
  let access_token = cookies.access_token;
  
  useEffect(() => {
    if (!access_token) {
      router.push('/signin');
      return;
    }
    const verifyToken = async () => { 
      try{
        await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/aaa/token`, {withCredentials: true}); 
      } catch (error) {
        // Delete access token cookie
        removeCookie('access_token');
        router.push('/signin');
      }
    }
    verifyToken();
  })


  const [searchText, setSearchText] = useState("");
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
      const productsInfo = response.data
      setTotalPages(productsInfo.information.numberOfPages)
      setProductList(productsInfo.information.items.slice(0, 12))
    } catch (e) {
      console.log(e);
      setProductList(null);
    }
  }

  let products;
  if (productList) {
    const productListArray = productList.map((product: any) => {
      return (
        <li className={styles.product_box} key={product.productId}>
          <Link href={`/product/${product.productId}`}>
            <a>
              <Image
                src={product.imageUrl}
                height={200}
                width={200}
                alt="Product Image" />
              <h3>{product.title}</h3>
              <p>
                Total Orders: {product.totalOrders || 0}<br/>
                Average Rating: {product.averageRating || 0}
              </p>
            </a>
          </Link>
        </li>
      )
    });
    products = (
      <div>
        <ul className={styles.product_list}>
          {productListArray}          
        </ul>
        <Pagination searchText={searchText} totalPages={totalPages} setProductList={setProductList} />
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
        <form className="offset-2 col-md-4 d-flex" onSubmit={handleSubmit}>
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
          <button className="btn btn-outline-primary fs-5" type="submit">Search</button>
        </form>
      </section>
      <section className="row">
        {products}
      </section>
    </Layout>
    // <Layout>
    //   <Head>
    //     <title>Products</title>
    //   </Head>
    //   <section>
    //     <form className={styles.search_bar} onSubmit={handleSubmit}>
    //       <input 
    //         className={styles.search_bar_content}
    //         name="search" 
    //         type="text" 
    //         value={searchText} 
    //         autoComplete="off"
    //         list="datalistOptions"
    //         onChange={handleChange} 
    //         placeholder="Search items you want" />
    //       <Autocomplete searchText={searchText} />
    //       <button className={styles.search_bar_content} type="submit">Search</button>
    //     </form>
    //   </section>
    //   <section>
    //     {products}
    //   </section>
    // </Layout>
  )
}

export async function getStaticProps() {
    let props = {}
    try {      
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/products?text=doggy22&page=1`, {
        headers: {  
            Authorization: `bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNpYW5Aa2FrYW8uY29tIiwiZXhwIjoxNjMzNjM0NTQzfQ.5GTM9T1MlH7mIiCzFP4wVyyRNCAZBZkF54N5E3Ef1-Q`
        }
      });
      
      const productsInfo = response.data
      return {
        props: {
          productsData: productsInfo.information.items.slice(0, 8),
        }
      }
    } catch (error) {
      props.productsData = null;
    }
    return {
      props
    }
}