import Link from 'next/link'
import Image from 'next/image'
import styles from '/styles/header.module.css'

export default function Header() {
  return (
    <header className={styles.header_container}>
      <div className={styles.logo}>
        <Image 
          src="/images/logo.jpg"
          height={80}
          width={80}
          alt="logo of ali express dropshipping"
        />
      </div>
      <nav>
        <ul className={styles.nav_ul}>
          <li className={styles.nav_li}>
            <Link href="/products">
              <a>Products</a>
            </Link>
          </li>
          <li className={styles.nav_li}>
            <Link href="/products">
              <a>About us</a>
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  )
}