import Link from 'next/link'
import Head from 'next/head'
import Layout from '../src/components/layout'
import Image from 'next/image'
import styles from '/styles/products.module.css'

import axios from 'axios';

export default function Products({ productsData }: any) {
  let products;
  if (productsData) {
    const productList = productsData.map((product: any) => {
      return (
        <li className={styles.product_box} key={product.productId}>
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
        </li>
      )
    });
    products = (
      <ul className={styles.product_list}>
        {productList}
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
      <form className={styles.search_bar}>
        <input className={styles.search_bar_content} name="search" type="text" placeholder="Search items you want" />
        <button className={styles.search_bar_content} type="submit">Search</button>
      </form>
    </section>
    <section>
      {products}
    </section>
  </Layout>
  )
}

// export async function getStaticPaths() {
//   try {
//     const response = axios.
//   } catch (error) {
    
//   }
// }

export async function getStaticProps() {
  // const authData = await fetch("http://localhost:8000/aaa/token", {
  //   method: "POST",
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  //   body: JSON.stringify({
  //     username: "lucian@kakao.com",
  //     password: "secret",
  //   })
  // })
  //   .then((response) => {
  //     return response.json()
  //   })
  //   .catch((error) => console.log(error));
    let props = {}
    try {
      // fetch style
      // const res = await fetch("http://localhost:8000/products?text=doggy22&page=1", {
      //   headers: {  
      //     Authorization: "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNpYW5Aa2FrYW8uY29tIiwiZXhwIjoxNjMyOTIzOTkxfQ.TEDjerFtEBqWxUh4ie773Hl20qCreF1DmNy9EM3qkfw"
      //   }
      // });
      // const productsInfo = await res.json();
      // return {
      //   props: {
      //     productsData: productsInfo.information.items.slice(0, 8)
      //   }
      // }
      
      // axios style
      const response = await axios.get('http://localhost:8000/products?text=doggy22&page=1', {
        headers: {  
            Authorization: "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNpYW5Aa2FrYW8uY29tIiwiZXhwIjoxNjMzMDIzMDU0fQ.6oatxthaqVmO9Gb1xqJigt2zvkQAAw95C4N-KcxGt7I"
        }
      });
      const productsInfo = response.data
      return {
        props: {
          productsData: productsInfo.information.items.slice(0, 8)
        }
      }
    } catch (error) {
      props.productsData = null;
    }
    return {
      props
    }
}