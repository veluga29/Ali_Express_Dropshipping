import Image from 'next/image'


export default function Footer() {
  return (
    <footer className="text-center alert-danger py-1">
      <div className="py-4">    
        <a href="https://github.com/veluminous" target="_blank" rel="noreferrer">
          <Image 
            src="/images/github_logo.png"
            height={30}
            width={40}
            alt="Github"
          />    
        </a>
        <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <a href="https://dev-on-coffee.tistory.com/" target="_blank" rel="noreferrer">
          <Image 
            src="/images/tistory_logo.png"
            height={28}
            width={31}
            alt="Tistory"
          />
        </a>
      </div>
      <div>
        <h6>Personal project:</h6>
      </div>
      <div>
        <figure>
          <blockquote className="blockquote">
            <p>Ali Express Dropshipping (AED)</p>
          </blockquote>
          <figcaption className="blockquote-footer">
            made by <cite title="Developer">SungYoon Cho</cite>
          </figcaption>
        </figure>
      </div>
      <div>
        <p className="text-secondary">
          ⓒ Copyright 2021 - 2028.
          <br/>
          All rights reserved. Powered by Lucian.
        </p>
      </div>
    </footer>
  )
}