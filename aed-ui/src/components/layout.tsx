import Header from './header'
import styles from '/styles/layout.module.css'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className={styles.layout_container}>
      <div>
        <Header />
      </div>
      <div>{children}</div>
    </div>
  )
}