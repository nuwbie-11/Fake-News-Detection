"use client"

import React, { FormEvent, useEffect } from 'react'

export default function Home() {
  const [data,setData] = React.useState<{message:string} | null>(null)


  function testFetch(){
    fetch(
      "https://nuwbie11.pythonanywhere.com/test",{
      }
    ).then((response) => response.json()).then((data) => {
      setData(data)
    })
  }

  function predictNews(event:FormEvent<HTMLFormElement>){
    event.preventDefault()
    
    const formData = new FormData(event.currentTarget)
    
    fetch(
      "https://nuwbie11.pythonanywhere.com/predictNews",{
        method:"POST",
        body:formData
      }
    ).then((response) => response.json()).then((data) => {
      setData(data)
    })
  
  }

  useEffect(()=>{
    testFetch()
  },[])

  
  return (
    <main className="flex flex-col items-center justify-between pt-12">
      <div className="form-wrapper">
        <form onSubmit={predictNews} method="post" className='flex flex-col gap-y-5'>
          <textarea name="article" id="" 
          className='sm:min-h-[24rem] sm:min-w-[35rem] px-2 py-3 rounded border border-black/[0.3rem] shadow shadow-black/[0.03]' 
          placeholder='Input Your News Article Here'/>

          <button type="submit" className='btn-rose py-2'>Submit</button>

        </form>

        
          {
            data ? (<p>{data["message"]}</p>) : ( null )
          }

      </div>
    </main>
  )
}
