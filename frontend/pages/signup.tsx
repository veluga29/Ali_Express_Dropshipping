import Link from 'next/link'
import Head from 'next/head'
import { useRouter } from 'next/router'
import Layout from '../src/components/layout'
import styles from '/styles/signin.module.css'

import { useState } from "react";
import { useEffect } from 'react'
import axios from 'axios';
import { useCookies } from "react-cookie"

export default function Signup() {
  const router = useRouter();
  const [ user, setUser ] = useState({});
  const [ cookies, ,removeCookie ] = useCookies();
  let access_token = cookies.access_token;

  useEffect(() => {
    if (!access_token) {
      return;
    }
    const verifyToken = async () => { 
      try{
        const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/aaa/token`, {withCredentials: true}); 
        if (response.data.valid) {
          router.push('/products');
        }
      } catch (error) {
        // Delete access token cookie
        removeCookie('access_token');
      }
    }
    verifyToken();
  })


  const handleChange = ({ target }) => {
    const { name, value } = target;
    setUser({
      ...user,
      [name]: value
    });
  };
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/me`, user);
      if (response.status == 200) {
        router.push('/signin');
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <Layout>
      <Head>
        <title>Signup</title>
      </Head>
      <div className={styles.signin_container}>
        <main>
          <form className={styles.login_form} onSubmit={handleSubmit}>
            <div className={styles.login_form_items}>
              <input 
                className={styles.login_input} 
                name="email" 
                type="email" 
                onChange={handleChange}
                placeholder="Email" />
            </div>
            <div className={styles.login_form_items}>
              <input 
                className={styles.login_input} 
                name="password" 
                type="password" 
                onChange={handleChange}
                placeholder="Password" />
            </div>
            <div className={styles.login_form_items}>
              <input 
                className={styles.login_input} 
                name="last_name" 
                type="text" 
                onChange={handleChange}
                placeholder="Last name" />
            </div>
            <div className={styles.login_form_items}>
              <input 
                className={styles.login_input} 
                name="first_name" 
                type="text" 
                onChange={handleChange}
                placeholder="First name" />
            </div>
            <div className={`${styles.login_form_items} ${styles.login_content}`}>
              <button id={styles.login_button} type="submit">Sign-up</button>
            </div>
          </form>
        </main>
      </div>
    </Layout>
  )
}