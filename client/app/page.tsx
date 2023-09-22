"use client"

import React, { FormEvent } from 'react'

export default function Home() {
  const [data,setData] = React.useState<{message:string} | null>(null)


  function predictNews(event:FormEvent<HTMLFormElement>){
    event.preventDefault()
    
    const formData = new FormData(event.currentTarget)
    
    fetch(
      "http://localhost:8080/testPredict",{
        method:"POST",
        body:formData
      }
    ).then((response) => response.json()).then((data) => {
      setData(data)
    })
    
    // const response = await fetch(
    //   "http://localhost:8080/testPredict",{
    //     method:"POST",
    //     body:formData
    //   }
    // )
    // const data = await response.json()
  }

  // React.useEffect(()=>{
  //   fetch("http://localhost:8080/testPredict")
  //     .then((res)=> res.json())
  //     .then((data)=> {
  //       setData(data)
  //     })
  // },[])
  
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
        <form onSubmit={predictNews} method="post">
          <input type="text" name="article" id="" />

          <button type="submit">Submit</button>

        </form>

        
          {
            data ? (<p>{data["message"]}</p>) : ( <p>Loading</p> )
          }

      </div>
    </main>
  )
}
