import reflex as rx
from reflex import State
import requests
import qr.styles.styles as styles

# @rx.page(route="/[nameQR]", title="Tarjeta QR")
class Estado(State):
    nombre: str = "Cargando..."
    email: str = ""
    telefono: str = ""
    departamento: str = ""
    posicion: str = ""
    QR : str
    async def cargar_nombre(self):
        try:
            response = requests.get(
                f"https://fichaje.ideasmedioambientales.com/api/getQR/{self.nameQR}"
            )
            print(response.url)
            print(f"Respuesta HTTP = {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"Respuesta JSON = {data}")
                self.nombre = data.get("name", "Nombre no encontrado")
                self.email = data.get("email", "Email no encontrado")
                self.telefono = data.get("phone", "Teléfono no encontrado")
                self.departamento = data.get("department", "Departamento no encontrado")
                self.posicion = data.get("position_department", "Posición no encontrada")
                self.QR = data.get("nameQR", "QR no encontrado")
            else:
                self.nombre = f"Error HTTP {response.status_code}"
                self.email = f"Error HTTP {response.status_code}"
                self.telefono = f"Error HTTP {response.status_code}"
                self.departamento = f"Error HTTP {response.status_code}"
                self.posicion = f"Error HTTP {response.status_code}"
        except Exception as e:
            print(f"Excepción al cargar: {e}")
            self.nombre = "Error al cargar"
            self.email = "Error al cargar"
            self.telefono = "Error al cargar"
            self.departamento = "Error al cargar"
            self.posicion = "Error al cargar"
            
def tarjeta():
    return rx.box(
        # Contenedor general
        rx.vstack(
            # Logo fijo arriba
            rx.image(src="/Logotipo.png", width="90%", margin_top="10px"), 
            # Contenedor animado
            rx.box(
                rx.vstack(
                    rx.image(
                        src=f"/images/employees/empleado_{Estado.QR}.png",
                        border_radius="10px", 
                        width="180px", 
                        height="180px", 
                        object_fit="cover",
                        border="3px solid #86A789",
                        box_shadow="md"
                    ),
                    rx.text(
                        Estado.nombre,
                        font_size="22px",
                        font_weight="bold",
                        color="#3C403E",
                        margin_top="10px"
                    ),
                    rx.badge(
                        rx.vstack(
                            rx.text(Estado.posicion),
                            spacing="0",  
                            align_items="center" 
                        ),
                        background_color="#86A789",
                        padding="6px 15px",
                        border_radius="8px",
                        color="#F1F1F1",
                        font_size="14px"
                    ),
                    rx.hstack(
                        rx.image("/email.svg"),
                        rx.text(Estado.email, font_size="16px", color="#3C403E"),
                        spacing="2",
                        align_items="center"
                    ),
                    rx.hstack(
                        rx.image("/phone.svg"),
                        rx.text(Estado.telefono, font_size="16px", color="#3C403E"),
                        spacing="2",
                        align_items="center"
                    ),
                    rx.link(
                        rx.hstack(
                            rx.image(
                                src="/web.svg",
                                width="20px",  # Ajusta el tamaño según necesites
                                height="20px",
                                margin_right="8px"  # Espacio entre icono y texto
                            ),
                            rx.text(
                                "www.ideasmedioambientales.com", 
                                font_size="16px", 
                                color="#3C403E"
                            ),
                            align_items="center",  # Centra verticalmente
                            spacing="0"  # Elimina espacio adicional
                        ),
                        href="https://ideasmedioambientales.com",
                        is_external=True,  # Para que abra en nueva pestaña
                        _hover={"text_decoration": "none"}  # Opcional: quita subrayado al pasar el mouse
                    ),  
                    rx.hstack(
                        rx.image("/home.svg"),
                        rx.vstack(
                            rx.text("Calle San Sebastian 19", font_size="16px", color="#3C403E"),
                            rx.text("02005 Albacete", font_size="16px", color="#3C403E" ),
                            align_items="center",
                            spacing="0",
                        ),
                        align_items="center"
                    ),
                    rx.badge(
                        rx.link("Guardar Contacto", 
                                href=f"https://fichaje.ideasmedioambientales.com/qr/vcard/{Estado.QR}",                            
                                is_external=True,  # Para que abra en nueva pestaña
                                _hover={"text_decoration": "none"} 
                                ),
                        spacing="0",  
                        background_color="#86A789",
                        padding="6px 15px",
                        border_radius="8px",
                        color="#F1F1F1",
                        font_size="14px"
                    ),
                    spacing="3",
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
        padding="20px",
        background_color="#F1F1F1",
        border_radius="18px",
        box_shadow="lg",
        width="376px",  
        height="700px",  
        display="flex",
        flex_direction="column",
        justify_content="flex-start",
        align_items="center",
    )
@rx.page(route="/[nameQR]")
def index(nameQR: str = "") -> rx.Component:
    return rx.box(
        rx.fragment(
            rx.image(
                src="/Imagen4.png",
                position="absolute",
                top="0",
                left="0",
                width="100%",
                height="100%",
                object_fit="cover",
                z_index="0",
            ),
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
            "fontFamily": "Poppins, sans-serif",
        },
        on_mount=lambda: Estado.cargar_nombre(nameQR)
    )


app = rx.App(
    stylesheets=styles.STYLESHEET,
)
app.add_page(index)