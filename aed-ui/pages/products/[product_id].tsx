import Head from 'next/head'
import Image from 'next/image'

import Layout from '../../src/components/layout'
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
        <p>
          {/* {productData.price.web.display || 0} <br /> */}
          {/* {productData.reviewsRatings.averageRating || 0} */}
        </p>
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

export async function getServerSideProps({ params }) {
  let props = {};
  try {
    const response = await axios.get(`http://localhost:8000/products/${params.product_id}`, {
      headers: {  
        Authorization: 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNpYW5Aa2FrYW8uY29tIiwiZXhwIjoxNjMzMzY1NDcwfQ.K4lFI-zsdfA4ESv7Gg2R6rqw78hj81tRGDncCTFXnxg'
      }
    });
    const productData = response.data
    return {
      props: {
        productData,
      }
    }
  } catch {
    props.productData = null;
  }
}