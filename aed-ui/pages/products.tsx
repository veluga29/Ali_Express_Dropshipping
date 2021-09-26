import Link from 'next/link'
import Head from 'next/head'
import Layout from '../src/components/layout'
import Image from 'next/image'
import styles from '/styles/products.module.css'


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
  
    const productsInfo = await fetch("http://localhost:8000/products?text=doggy20&page=1", {
    headers: {
      Authorization: "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNpYW5Aa2FrYW8uY29tIiwiZXhwIjoxNjMyNzE2MDA5fQ.yAkO-PbkCAkRmNkSZVIV9FLFoC7ZPcM00l3fOiB-akM"
    }
  })
    .then((response) => {
      return response.json()
    })
    .catch((error) => console.log(error));

  return {
    props: {
      productsData: productsInfo.information.items.slice(0, 8)
    }
  }
}

export default function Products({ productsData }: any) {
  const productList = productsData.map((product: any) => {
    return (
      <li className={styles.product_box} key={product.productId}>
        <Image
          src="/images/logo.jpg"
          height={200}
          width={200}
          alt="Product Image" />
        <h3>{product.title}</h3>
        <p>Short Description</p>
      </li>
    )
  })
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
      <ul className={styles.product_list}>
        {productList}
      </ul>
    </section>
  </Layout>
  )
}