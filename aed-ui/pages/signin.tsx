import Link from 'next/link'
import Head from 'next/head'
import Layout from '../src/components/layout'
import styles from '/styles/signin.module.css'

import { useState } from "react";
import { useCookies } from "react-cookie"
import axios from 'axios';
import FormData from 'form-data';

export default function Signin() {
  const [, setCookie] = useCookies(["access_token"]);

  const [ email, setEmail ] = useState("");
  const [ password, setPassword ] = useState("");

  const handleEmailChange = ({ target: { value } }) => setEmail(value);
  const handlePasswordChange = ({ target: { value } }) => setPassword(value);
  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);
    try {
      const response = await axios.post('http://localhost:8000/aaa/token',
      formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      if (response.status == 200) {
        const accessToken = response.data.access_token;
        setCookie(
          'access_token', 
          accessToken,
          // {
          //   secure: true,
          //   httpOnly: true
          // }
        );
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <Layout>
      <Head>
        <title>Signin</title>
      </Head>
      <div className={styles.signin_container}>
        <main>
          <form className={styles.login_form} onSubmit={handleSubmit}>
            <div className={styles.login_form_items}>
              <input 
                className={styles.login_input} 
                name="email" 
                type="email" 
                onChange={handleEmailChange}
                placeholder="Email" />
            </div>
            <div className={styles.login_form_items}>
              <input 
                className={styles.login_input} 
                name="password" 
                type="password" 
                onChange={handlePasswordChange}
                placeholder="Password" />
            </div>
            <div className={`${styles.login_form_items} ${styles.login_content}`}>
              <a id={styles.register_button} >
                <div>
                  Register
                </div>
              </a>
              <button id={styles.login_button} type="submit">Log-in</button>
            </div>
          </form>
        </main>
      </div>
    </Layout>
  )
}