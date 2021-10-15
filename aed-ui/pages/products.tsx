import Link from 'next/link'
import Head from 'next/head'
import Layout from '../src/components/layout'
import Autocomplete from '../src/components/autocomplete'
import Image from 'next/image'
import styles from '/styles/products.module.css'

import { useState } from "react";
import { useCookies } from "react-cookie"
import axios from 'axios';

export default function Products({ productsData }: any) {
  const [cookies] = useCookies(["access_token"]);
  const [searchText, setSearchText] = useState("");
  const [productList, setProductList] = useState(productsData);
  const handleChange = ({ target: { value } }) => setSearchText(value);
  const handleSubmit = async (event) => {
    // after submit, we can get final searching text
    // we call API to get the list of searching text products
    // Store the updated list to state so we can apply on the UI (JSX component)
    event.preventDefault();
    try {
      const response = await axios.get(`http://localhost:8000/products?text=${searchText}&page=1`, {
        headers: {  
            Authorization: `bearer ${cookies.access_token}`
        }
      });
      const productsInfo = response.data
      setProductList(productsInfo.information.items.slice(0, 8))
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
      <ul className={styles.product_list}>
        {productListArray}          
      </ul>);
    
  } else {
    products = (
      <h2>Please search your products</h2>
    )
  }

  return (
  <Layout>
    <Head>
      <title>Products</title>
    </Head>
    <section>
      <form className={styles.search_bar} onSubmit={handleSubmit}>
        <input 
          className={styles.search_bar_content}
          name="search" 
          type="text" 
          value={searchText} 
          autoComplete="off"
          list="datalistOptions"
          onChange={handleChange} 
          placeholder="Search items you want" />
        <Autocomplete searchText={searchText} />
        <button className={styles.search_bar_content} type="submit">Search</button>
      </form>
    </section>
    <section>
      {products}
    </section>
  </Layout>
  )
}

export async function getStaticProps() {
    let props = {}
    try {      
      const response = await axios.get('http://localhost:8000/products?text=doggy22&page=1', {
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