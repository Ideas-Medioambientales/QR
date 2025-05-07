/** @jsxImportSource @emotion/react */


import { Fragment, useContext, useEffect } from "react"
import { Badge as RadixThemesBadge, Box as RadixThemesBox, Flex as RadixThemesFlex, Link as RadixThemesLink, Text as RadixThemesText } from "@radix-ui/themes"
import { EventLoopContext, StateContexts } from "$/utils/context"
import { Event } from "$/utils/state"
import NextLink from "next/link"
import NextHead from "next/head"



export function Img_7cd87397767f7ef062fb5ea1df190754 () {
  
  const reflex___state____state__qr___qr____estado = useContext(StateContexts.reflex___state____state__qr___qr____estado)





  
  return (
    <img css={({ ["borderRadius"] : "10px", ["width"] : "180px", ["height"] : "180px", ["objectFit"] : "cover", ["border"] : "3px solid #86A789", ["boxShadow"] : "md" })} src={reflex___state____state__qr___qr____estado.avatar}/>
  )
}

export function Text_633166697e2626cd45872e2a5afb3957 () {
  
  const reflex___state____state__qr___qr____estado = useContext(StateContexts.reflex___state____state__qr___qr____estado)





  
  return (
    <RadixThemesText as={"p"} css={({ ["fontSize"] : "16px", ["color"] : "#3C403E" })}>

{reflex___state____state__qr___qr____estado.telefono}
</RadixThemesText>
  )
}

export function Text_19bb880e3b3ee07d1ea7e5e0c014149e () {
  
  const reflex___state____state__qr___qr____estado = useContext(StateContexts.reflex___state____state__qr___qr____estado)





  
  return (
    <RadixThemesText as={"p"}>

{reflex___state____state__qr___qr____estado.posicion}
</RadixThemesText>
  )
}

export function Link_effb4bc4dbfaa80fd7e376ae28e6748d () {
  
  const reflex___state____state__qr___qr____estado = useContext(StateContexts.reflex___state____state__qr___qr____estado)





  
  return (
    <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["textDecoration"] : "none" }) })} target={(true ? "_blank" : "")}>

<NextLink href={("https://fichaje.ideasmedioambientales.com/qr/vcard/"+reflex___state____state__qr___qr____estado.QR)} passHref={true}>

{"Guardar Contacto"}
</NextLink>
</RadixThemesLink>
  )
}

export function Box_8801916c46984de73077033fb14986e4 () {
  
  
                useEffect(() => {
                    ((...args) => (addEvents([(Event("reflex___state____state.qr___qr____estado.cargar_nombre", ({  }), ({  })))], args, ({  }))))()
                    return () => {
                        
                    }
                }, []);
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <RadixThemesBox css={({ ["position"] : "relative", ["backgroundColor"] : "#3E665C", ["height"] : "100vh", ["overflow"] : "hidden", ["fontFamily"] : "Poppins, sans-serif", ["--default-font-family"] : "Poppins, sans-serif" })}>

<Fragment>

<img css={({ ["position"] : "absolute", ["top"] : "0", ["left"] : "0", ["width"] : "100%", ["height"] : "100%", ["objectFit"] : "cover", ["zIndex"] : "0" })} src={"/Imagen4.png"}/>
<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["position"] : "relative", ["zIndex"] : 1, ["height"] : "100vh" })}>

<RadixThemesBox css={({ ["padding"] : "20px", ["backgroundColor"] : "#F1F1F1", ["borderRadius"] : "18px", ["boxShadow"] : "lg", ["width"] : "376px", ["height"] : "700px", ["display"] : "flex", ["flexDirection"] : "column", ["justifyContent"] : "flex-start", ["alignItems"] : "center" })}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["height"] : "100%", ["width"] : "100%", ["display"] : "flex", ["justifyContent"] : "center", ["alignItems"] : "center", ["transition"] : "all 0.5s ease-in-out" })} direction={"column"} gap={"3"}>

<img css={({ ["width"] : "90%", ["marginTop"] : "10px" })} src={"/Logotipo.png"}/>
<RadixThemesBox>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center", ["transition"] : "all 0.5s ease-in-out" })} direction={"column"} gap={"3"}>

<Img_7cd87397767f7ef062fb5ea1df190754/>
<Text_4cc7ffa2f94cbcfd226a283b082bb538/>
<RadixThemesBadge css={({ ["backgroundColor"] : "#86A789", ["padding"] : "6px 15px", ["borderRadius"] : "8px", ["color"] : "#F1F1F1", ["fontSize"] : "14px" })}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"column"} gap={"0"}>

<Text_19bb880e3b3ee07d1ea7e5e0c014149e/>
</RadixThemesFlex>
</RadixThemesBadge>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} gap={"2"}>

<img src={"/email.svg"}/>
<Text_fc2c866d0e306f54faf0682ec930cd68/>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} gap={"2"}>

<img src={"/phone.svg"}/>
<Text_633166697e2626cd45872e2a5afb3957/>
</RadixThemesFlex>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["textDecoration"] : "none" }) })} target={(true ? "_blank" : "")}>

<NextLink href={"https://ideasmedioambientales.com"} passHref={true}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} gap={"0"}>

<img css={({ ["width"] : "20px", ["height"] : "20px", ["marginRight"] : "8px" })} src={"/web.svg"}/>
<RadixThemesText as={"p"} css={({ ["fontSize"] : "16px", ["color"] : "#3C403E" })}>

{"www.ideasmedioambientales.com"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} gap={"3"}>

<img src={"/home.svg"}/>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"column"} gap={"0"}>

<RadixThemesText as={"p"} css={({ ["fontSize"] : "16px", ["color"] : "#3C403E" })}>

{"Calle San Sebastian 19"}
</RadixThemesText>
<RadixThemesText as={"p"} css={({ ["fontSize"] : "16px", ["color"] : "#3C403E" })}>

{"02005 Albacete"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
<RadixThemesBadge css={({ ["spacing"] : "0", ["backgroundColor"] : "#86A789", ["padding"] : "6px 15px", ["borderRadius"] : "8px", ["color"] : "#F1F1F1", ["fontSize"] : "14px" })}>

<Link_effb4bc4dbfaa80fd7e376ae28e6748d/>
</RadixThemesBadge>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
</Fragment>
</RadixThemesBox>
  )
}

export function Text_4cc7ffa2f94cbcfd226a283b082bb538 () {
  
  const reflex___state____state__qr___qr____estado = useContext(StateContexts.reflex___state____state__qr___qr____estado)





  
  return (
    <RadixThemesText as={"p"} css={({ ["fontSize"] : "22px", ["fontWeight"] : "bold", ["color"] : "#3C403E", ["marginTop"] : "10px" })}>

{reflex___state____state__qr___qr____estado.nombre}
</RadixThemesText>
  )
}

export function Text_fc2c866d0e306f54faf0682ec930cd68 () {
  
  const reflex___state____state__qr___qr____estado = useContext(StateContexts.reflex___state____state__qr___qr____estado)





  
  return (
    <RadixThemesText as={"p"} css={({ ["fontSize"] : "16px", ["color"] : "#3C403E" })}>

{reflex___state____state__qr___qr____estado.email}
</RadixThemesText>
  )
}

export default function Component() {
    




  return (
    <Fragment>

<Box_8801916c46984de73077033fb14986e4/>
<NextHead>

<title>

{"Qr | Index"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
