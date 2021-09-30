import Link from 'next/link'
import Head from 'next/head'
import Layout from '../src/components/layout'
import styles from '/styles/signin.module.css'


export default function Signin() {
  return (
    <Layout>
      <Head>
        <title>Signin</title>
      </Head>
      <div className={styles.signin_container}>
        <main>
          <form className={styles.login_form}>
            <div className={styles.login_form_items}>
              <input className={styles.login_input} name="email" type="email" placeholder="Email" />
            </div>
            <div className={styles.login_form_items}>
              <input className={styles.login_input} name="password" type="password" placeholder="Password" />
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