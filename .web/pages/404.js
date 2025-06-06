/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { isTrue } from "$/utils/state"
import Error from "next/error"
import { useClientSideRouting } from "$/utils/client_side_routing"
import NextHead from "next/head"



export function Fragment_4d5c309f6c2a2b60979d7921552e7404 () {
  

  const routeNotFound = useClientSideRouting()




  
  return (
    <Fragment>

{isTrue(routeNotFound) ? (
  <Fragment>

<Error statusCode={404}/>
</Fragment>
) : (
  <Fragment>


</Fragment>
)}
</Fragment>
  )
}

export default function Component() {
    




  return (
    <Fragment>

<Fragment_4d5c309f6c2a2b60979d7921552e7404/>
<NextHead>

<title>

{"404 - Not Found"}
</title>
<meta content={"The page was not found"} name={"description"}/>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
