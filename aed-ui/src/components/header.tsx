import Link from 'next/link'
import Image from 'next/image'
import { useRouter } from 'next/router'

import styles from '/styles/header.module.css'

export default function Header() {
  const router = useRouter();

  return (
    <header className={styles.header_container}>
      <div className={styles.logo}>
        <Link href="/">
          <a>
            <Image 
              src="/images/logo.jpg"
              height={80}
              width={80}
              alt="logo of ali express dropshipping"
            />
          </a>
        </Link>
      </div>
      <nav>
        <ul className={styles.nav_ul}>
          <li className={styles.nav_li}>
            <Link href="/products">
              <a>Products</a>
            </Link>
          </li>
          <li className={styles.nav_li}>
            <Link href="/">
              <a>About us</a>
            </Link>
          </li>
          {router.pathname === '/products' &&
            <li className={styles.nav_li}>
              <Link href="/signin">
                <a>Sign in</a>
              </Link>
            </li>
          }
        </ul>
      </nav>
    </header>
  )
}