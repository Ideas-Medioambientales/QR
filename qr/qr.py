import reflex as rx

class Estado(rx.State):
    mostrar_qr_grande: bool = False

def tarjeta():
    return rx.box(
        # Contenedor general
        rx.vstack(
            # Logo fijo arriba
            rx.image(src="Logotipo.png", width="90%", margin_top="10px"),
            
            # Contenedor animado
            rx.box(
                rx.cond(
                    Estado.mostrar_qr_grande,
                    # Vista del QR en grande
                    rx.vstack(
                        rx.image(
                            src="output.png",
                            width="250px",
                            cursor="pointer",
                            border_radius="10px",
                            box_shadow="lg",
                            on_click=lambda: Estado.set_mostrar_qr_grande(False)
                        ),
                        rx.text(
                            "JUAN JOSÉ SEGUÍ BORJA",
                            font_size="22px",
                            font_weight="bold",
                            color="#3C403E",
                            margin_top="10px"
                        ),
                        rx.badge("Developer",
                            background_color="#86A789",
                            padding="6px 15px",
                            border_radius="8px",
                            color="#F1F1F1",
                            font_size="14px"
                        ),
                        rx.hstack(
                            rx.image("email.svg"),
                            rx.text("jjsegui@ideasmedioambientales.com", font_size="16px", color="#3C403E"),
                            spacing="2",
                            align_items="center"
                        ),
                        rx.hstack(
                            rx.image("phone.svg"),
                            rx.text("+34 647 71 85 85", font_size="16px", color="#3C403E"),
                            spacing="2",
                            align_items="center"
                        ),
                        height="100%",
                        width="100%",
                        display="flex",
                        justify_content="center",
                        align_items="center",
                        transition="all 0.5s ease-in-out"
                    ),
                    # Vista normal
                    rx.vstack(
                        rx.image(
                            src="unnamed.jpg",
                            border_radius="10px", 
                            width="180px", 
                            height="180px", 
                            object_fit="cover",
                            border="3px solid #86A789",
                            box_shadow="md"
                        ),
                        rx.text(
                            "JUAN JOSÉ SEGUÍ BORJA",
                            font_size="22px",
                            font_weight="bold",
                            color="#3C403E",
                            margin_top="10px"
                        ),
                        rx.badge("Developer",
                            background_color="#86A789",
                            padding="6px 15px",
                            border_radius="8px",
                            color="#F1F1F1",
                            font_size="14px"
                        ),
                        rx.hstack(
                            rx.image("email.svg"),
                            rx.text("jjsegui@ideasmedioambientales.com", font_size="16px", color="#3C403E"),
                            spacing="2",
                            align_items="center"
                        ),
                        rx.hstack(
                            rx.image("phone.svg"),
                            rx.text("+34 647 71 85 85", font_size="16px", color="#3C403E"),
                            spacing="2",
                            align_items="center"
                        ),
                        rx.box(
                            rx.image(
                                src="output.png",
                                width="90px",
                                cursor="pointer",
                                border_radius="10px",
                                box_shadow="lg",
                            ),
                            padding="10px",
                            on_click=lambda: Estado.set_mostrar_qr_grande(True)
                        ),
                        spacing="4",
                        align_items="center",
                        transition="all 0.5s ease-in-out"
                    )
                ),
                height="100%",
                width="100%",
                display="flex",
                justify_content="center",
                align_items="center",
                transition="all 0.5s ease-in-out"
            ),
        ),
        padding="20px",
        background_color="#F1F1F1",
        border_radius="18px",
        box_shadow="lg",
        width="375px",  
        height="667px",  
        display="flex",
        flex_direction="column",
        justify_content="flex-start",
        align_items="center",
    )

def index() -> rx.Component:
    return rx.box(
        # Contenedor general con imagen de fondo
        rx.fragment(
            # Imagen de fondo ocupando toda la pantalla
            rx.image(
                src="Imagen4.png",  # Cambia esto por tu imagen real
                position="absolute",
                top="0",
                left="0",
                width="100%",
                height="100%",
                object_fit="cover",
                z_index="0",
            ),
            # Tarjeta centrada por encima
            rx.center(
                tarjeta(),
                style={
                    "position": "relative",
                    "zIndex": 1,
                    "height": "100vh",
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center"
                }
            )
        ),
        style={
            "position": "relative",
            "backgroundColor": "#3E665C",
            "height": "100vh",
            "overflow": "hidden",
            "fontFamily": "Poppins, sans-serif"
        }
    )


app = rx.App()
app.add_page(index)
