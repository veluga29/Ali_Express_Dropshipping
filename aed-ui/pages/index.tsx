import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import { useRouter } from 'next/router'
import styles from '../styles/Home.module.css'

import { useEffect } from 'react'
import { useCookies } from "react-cookie"

const Home: NextPage = () => {
  const router = useRouter();
  const [ cookies ] = useCookies(["access_token"]);

  useEffect(() => {
    if (!cookies.access_token) {
      router.push('/signin');
    } else {
      router.push('/products');
    }
  });

  return (
    <div className={styles.container}>
      <Head>
        <title>Index</title>
      </Head>
      <h1>Loading...</h1>
    </div>
  )
}

export default Home
