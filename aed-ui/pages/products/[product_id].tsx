import Head from 'next/head'
import Layout from '../../src/components/layout'
import Image from 'next/image'
import styles from '/styles/products.module.css'

import axios from 'axios'

export default function ProductDetail( { productData } ) {
  let product;
  if (productData) {
    product = (
      <>
        <Image
            src={productData.productImages[0]}
            height={200}
            width={200}
            alt="Product Image" />
        <h1>{productData.title}</h1>
        <p>{productData}</p>
      </>
    )
  } else {
    product = (
        <h2>Sorry, there is no detail.</h2>
    )
  }

  return (
    <Layout>
      <Head>
        <title>Product Detail</title>
      </Head>
      <section>
        <form className={styles.search_bar}>
          <input className={styles.search_bar_content} name="search" type="text" placeholder="Search items you want" />
          <button className={styles.search_bar_content} type="submit">Search</button>
        </form>
      </section>
      <section>
        {product}
      </section>
    </Layout>
  )
}



export async function getStaticPaths() {
  try {
    const response = await axios.get('http://localhost:8000/products?text=doggy22&page=1', {
      headers: {  
        Authorization: "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNpYW5Aa2FrYW8uY29tIiwiZXhwIjoxNjMzMDIzMDU0fQ.6oatxthaqVmO9Gb1xqJigt2zvkQAAw95C4N-KcxGt7I"
      }
    });
    const productsInfo = response.data;
    const paths = productsInfo.information.items.map(item => {
      params: { product_id: item.productId }
    });
    
    return { paths, fallback: 'true' }
  } catch (error) {
    
  }
}

export async function getStaticProps({ params }) {
  
}