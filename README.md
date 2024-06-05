# Gestion PYME

>Alumno: Paolantonio Diego Gabriel
>Curso: Python
>Comision: 54140

## Descripcion de la aplicacion

>El objetivo de esta aplicacion es facilitar la gestion dentro de una PYME o para un Freelance, pudiendo llevar un control del personal que se utiliza, los clientes que se atienden, los proyectos, la facturacion y los gastos.

## Video de muestra de funcionamiento

[Gestion PYME](https://drive.google.com/drive/folders/1QA1rmgzZ3gfZURd4FtequOAPjxvTfnEp?usp=sharing)

## Descripcion tecnica

### Secciones

- Core:
    Informacion sobre la aplicacion

| URLs | Descricion |
| -----------  | ----------- |
| / | Pagina principal |
| /nosotros | Informacion de la empresa |

- Personal:
    Visualizacion del **"Personal"** que esta cargado y de las **"Areas"** de trabajo definidas, ademas del manejo del CRUD de ambos models.

    | URLs | Descricion |
    | -----------  | ----------- |
    | /personal | Seleccion entre visualizar **"Personal"** y **"Area"** |
    | /personal/area/list | Visualizar las **"Areas"**, y seleccionar la accion del CRUD para realizar |
    | /personal/area/create | Crear un **"Area"** |
    | /personal/area/update/`id` | Modificar el **"Area"** seleccionada por el `id` |
    | /personal/area/delete/`id` | Eliminar el **"Area"** seleccionada por el `id` |
    | /personal/personal/list | Visualizar las **"Personal"**, y seleccionar la accion del CRUD para realizar |
    | /personal/personal/create | Crear un **"Personal"** |
    | /personal/personal/detail/`id` | Visualiza el detallde del **"Personal"** seleccionado por el `id` |
    | /personal/personal/update/`id` | Modificar el **"Personal"** seleccionado por el `id` |
    | /personal/personal/delete/`id` | Eliminar el **"Personal"** seleccionado por el `id` |
    
    - Models
        - Area
            | Item | Descricion |
            | -----------  | ----------- |
            | nombre | Nombre del **"Area"** |
            | sede | Sede de la sucursal donde esta el **"Area"** |

        - Personal
            | Item | Descricion |
            | -----------  | ----------- |
            | nombre | Nombre del personal |
            | apellido | Apellido del personal |
            | dni | DNI del personal agregado |
            | area_id | Foreign Key de **"Area"** |
            | usuario | Usuario del sistema al que esta vinculado el personal |
            | avatar | Imagen de perfil del personal seleccionado |

- Clientes:
    Visualizacion de los **"Clientes"** que esta cargado, y de las **"Ubicaciones"** donde se encuentran, ademas del manejo del CRUD de ambos models.

    | URLs | Descricion |
    | -----------  | ----------- |
    | /clientes | Seleccion entre visualizar **"Ubicacion"** y **"Cliente"** |
    | /clientes/ubicacion/list | Visualizar las **"Ubicacion"**, y seleccionar la accion del CRUD para realizar |
    | /clientes/ubicacion/create | Crear una **"Ubicacion"** |
    | /clientes/ubicacion/update/`id` | Modificar la **"Ubicacion"** seleccionada por el `id` |
    | /clientes/ubicacion/delete/`id` | Eliminar la **"Ubicacion"** seleccionada por el `id` |
    | /clientes/cliente/list | Visualizar las **"Cliente"**, y seleccionar la accion del CRUD para realizar |
    | /clientes/cliente/create | Crear un **"Cliente"** |
    | /clientes/cliente/detail/`id` | Vizualiza el detalle del **"Cliente"** seleccionado por el `id` |
    | /clientes/cliente/update/`id` | Modificar el **"Cliente"** seleccionado por el `id` |
    | /clientes/cliente/delete/`id` | Eliminar el **"Cliente"** seleccionado por el `id` |

    - Models
        - Ubicacion
            | Item | Descricion |
            | -----------  | ----------- |
            | pais | Pais donde trabaja el **"cliente"** |
            | provincia | Provincia donde trabaja el **"cliente"** |

        - Cliente
            | Item | Descricion |
            | -----------  | ----------- |
            | razonSocial | Nombre del **"cliente"** |
            | cuit | Identificacion unica del **"cliente"** |
            | ubicacion_id | Foreign Key de la **"ubicacion"** donde esta el **"cliente"** |

- Proyectos:
    Visualizacion de los **"Proyectos"** que estan cargados, ademas del manejo del CRUD de ambos models.

    | URLs | Descricion |
    | -----------  | ----------- |
    | /proyectos | Seleccion para visualizar **"Proyecto"** |
    | /proyectos/proyecto/list | Visualizar las **"Proyecto"**, y seleccionar la accion del CRUD para realizar |
    | /proyectos/proyecto/create | Crear una **"Proyecto"** |
    | /proyectos/proyecto/detail/`id` | Visualiza el detalle del **"Proyecto"** seleccionado por el `id` |
    | /proyectos/proyecto/update/`id` | Modificar la **"Proyecto"** seleccionado por el `id` |
    | /proyectos/proyecto/delete/`id` | Eliminar la **"Proyecto"** seleccionado por el `id` |

    - Models
        - Proyecto
            | Item | Descricion |
            | -----------  | ----------- |
            | nombre | Nombre del **"proyecto"** |
            | cliente | Cliente al que se le esta desarrollando el **proyecto** |
            | pais | Pais en el que se ejecuta |
            | fechaInicio | Fecha de inicio del **"proyecto"** |
            | fechaFin | Fecha de finalizacion del **"proyecto"** |
            | estado | Estado en el que se encuentra el **"proyecto"** |

- Administracion:
    Visualizacion de los **"Gastos"** que estan cargados, y de las **"Facturas"** emitidas, ademas del manejo del CRUD de ambos models.

    | URLs | Descricion |
    | -----------  | ----------- |
    | /administracion | Seleccion entre visualizar **"Gasto"** y **"Factura"** |
    | /administracion/gasto/list | Visualizar los **"Gastos"**, y seleccionar la accion del CRUD para realizar |
    | /administracion/gasto/create | Crear una **"Gasto"** |
    | /administracion/gasto/detail/`id` | Visualiza el detalle del **"Gasto"** seleccionado por el `id` |
    | /administracion/gasto/update/`id` | Modificar el **"Gasto"** seleccionado por el `id` |
    | /administracion/gasto/delete/`id` | Eliminar el **"Gasto"** seleccionado por el `id` |
    | /administracion/factura/list | Visualizar las **"Facturas"**, y seleccionar la accion del CRUD para realizar |
    | /administracion/factura/create | Crear una **"Factura"** |
    | /administracion/factura/detail/`id` | Visualiza el detalle de la **"Factura"** seleccionada por el `id` |
    | /administracion/factura/update/`id` | Modificar la **"Factura"** seleccionada por el `id` |
    | /administracion/factura/delete/`id` | Eliminar la **"Factura"** seleccionada por el `id` |

    - Models
        - Gasto
            | Item | Descricion |
            | -----------  | ----------- |
            | Referencia | Referencia unica del **"gasto"** |
            | FechaEmision | Fecha en la que se realiza el **"gasto"** |
            | FechaVencimiento | Fecha de vencimiento del pago del mismo |
            | Moneda | Moneda en la que se realiza |
            | Monto | Monto total del **"gasto"** |
            | Detalle | Detalle que se considere oportuno aclarar |

        - Factura
            | Item | Descricion |
            | -----------  | ----------- |
            | Numero | Numero de la **"factura"** emitida |
            | Proyecto | Proyecto por el que se emite la **"factura"** |
            | FechaEmision | Fecha en que se realizo la **"factura"** |
            | FechaVencimiento | Fecha de vencimiento del pago |
            | Moneda | Moneda en la que esta emitida |
            | Monto | Monto total a cobrar |
            | Detalle | Detalle que se crea necesario aclarar de la **"factura"** |

## Mejoras futuras

- Mejorar la interface grafica.
- Plantear mas secciones en la aplicacion.

## Problemas conocidos

- No es una una interlaz intuitiva.