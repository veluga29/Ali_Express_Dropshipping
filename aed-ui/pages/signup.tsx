import Link from 'next/link'
import Head from 'next/head'
import { useRouter } from 'next/router'
import Layout from '../src/components/layout'
import styles from '/styles/signin.module.css'

import { useState } from "react";
import axios from 'axios';

export default function Signup() {
  const router = useRouter();
  const [ user, setUser ] = useState({});

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
      const response = await axios.post('http://localhost:8000/me', user);
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