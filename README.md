# Gestion PYME

>Alumno: Paolantonio Diego Gabriel
>Curso: Python
>Comision: 54140

## Descripcion de la aplicacion

>El objetivo de esta aplicacion es facilitar la gestion dentro de una PYME o para un Freelance, pudiendo llevar un control del personal que se utiliza, los clientes que se atienden, los proyectos, la facturacion y los gastos.

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
    | /personal/Area/list | Visualizar las **"Areas"**, y seleccionar la accion del CRUD para realizar |
    | /personal/Area/create | Crear un **"Area"** |
    | /personal/Area/delete/`id` | Eliminar el **"Area"** seleccionada por el `id` |
    | /personal/Area/update/`id` | Modificar el **"Area"** seleccionada por el `id` |
    | /personal/personal/list | Visualizar las **"Personal"**, y seleccionar la accion del CRUD para realizar |
    | /personal/personal/create | Crear un **"Personal"** |
    | /personal/personal/delete/`id` | Eliminar el **"Personal"** seleccionado por el `id` |
    | /personal/personal/update/`id` | Modificar el **"Personal"** seleccionado por el `id` |

    - Models
        - Area
            | Item | Descricion |
            | -----------  | ----------- |
            | nombre | Nombre del **"Area"** |
            | pais | Pais de la sucursal donde esta el **"Area"** |

        - Personal
            | Item | Descricion |
            | -----------  | ----------- |
            | Nombre | Nombre del personal |
            | Apellido | Apellido del personal |
            | DNI | DNI del personal agregado |
            | Area_id | Foreign Key de **"Area"** |

- Clientes:
    Visualizacion de los **"Clientes"** que esta cargado, y de las **"Ubicaciones"** donde se encuentran, ademas del manejo del CRUD de ambos models.

    | URLs | Descricion |
    | -----------  | ----------- |
    | /clientes | Seleccion entre visualizar **"Ubicacion"** y **"Cliente"** |
    | /clientes/ubicacion/list | Visualizar las **"Ubicacion"**, y seleccionar la accion del CRUD para realizar |
    | /clientes/ubicacion/create | Crear una **"Ubicacion"** |
    | /clientes/ubicacion/delete/`id` | Eliminar la **"Ubicacion"** seleccionada por el `id` |
    | /clientes/ubicacion/update/`id` | Modificar la **"Ubicacion"** seleccionada por el `id` |
    | /clientes/clientes/list | Visualizar las **"Cliente"**, y seleccionar la accion del CRUD para realizar |
    | /clientes/clientes/create | Crear un **"Cliente"** |
    | /clientes/clientes/delete/`id` | Eliminar el **"Cliente"** seleccionado por el `id` |
    | /clientes/clientes/update/`id` | Modificar el **"Cliente"** seleccionado por el `id` |

    - Models
        - Ubicacion
            | Item | Descricion |
            | -----------  | ----------- |
            | pais | Pais donde trabaja el **"cliente"** |
            | provincia | Provincia donde trabaja el **"cliente"** |

        - Cliente
            | Item | Descricion |
            | -----------  | ----------- |
            | RazonSocial | Nombre del **"cliente"** |
            | Cuit | Identificacion unica del **"cliente"** |
            | Ubicacion_id | Foreign Key de la **"ubicacion"** donde esta el **"cliente"** |

- Proyectos:
    Visualizacion de los **"Proyectos"** que estan cargados, ademas del manejo del CRUD de ambos models.

    | URLs | Descricion |
    | -----------  | ----------- |
    | /proyectos | Seleccion para visualizar **"Proyecto"** |
    | /proyectos/ubicacion/list | Visualizar las **"Proyecto"**, y seleccionar la accion del CRUD para realizar |
    | /proyectos/ubicacion/create | Crear una **"Proyecto"** |
    | /proyectos/ubicacion/delete/`id` | Eliminar la **"Proyecto"** seleccionada por el `id` |
    | /proyectos/ubicacion/update/`id` | Modificar la **"Proyecto"** seleccionada por el `id` |

    - Models
        - Proyecto
            | Item | Descricion |
            | -----------  | ----------- |
            | Nombre | Nombre del **"proyecto"** |
            | Pais | Pais en el que se ejecuta |
            | FechaInicio | Fecha de inicio del **"proyecto"** |
            | FechaFin | Fecha de finalizacion del **"proyecto"** |
            | Estado | Estado en el que se encuentra el **"proyecto"** |

- Administracion:
    Visualizacion de los **"Gastos"** que estan cargados, y de las **"Facturas"** emitidas, ademas del manejo del CRUD de ambos models.

    | URLs | Descricion |
    | -----------  | ----------- |
    | /administracion | Seleccion entre visualizar **"Gasto"** y **"Factura"** |
    | /administracion/gastos/list | Visualizar los **"Gastos"**, y seleccionar la accion del CRUD para realizar |
    | /administracion/gastos/create | Crear una **"Gasto"** |
    | /administracion/gastos/delete/`id` | Eliminar el **"Gasto"** seleccionado por el `id` |
    | /administracion/gastos/update/`id` | Modificar el **"Gasto"** seleccionado por el `id` |
    | /administracion/facturas/list | Visualizar las **"Facturas"**, y seleccionar la accion del CRUD para realizar |
    | /administracion/facturas/create | Crear una **"Factura"** |
    | /administracion/facturas/delete/`id` | Eliminar la **"Factura"** seleccionada por el `id` |
    | /administracion/facturas/update/`id` | Modificar la **"Factura"** seleccionada por el `id` |

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
            | Cliente | Cliente al que fue emitida |
            | Proyecto | Proyecto por el que se emite la **"factura"** |
            | FechaEmision | Fecha en que se realizo la **"factura"** |
            | FechaVencimiento | Fecha de vencimiento del pago |
            | Moneda | Moneda en la que esta emitida |
            | Monto | Monto total a cobrar |
            | Detalle | Detalle que se crea necesario aclarar de la **"factura"** |

## Mejoras futuras

- Mejorar la interface grafica.
- Mejorar la informacion que de los distintos models.
- Cruzar la informacion de los models, para poder realizar un analisis de los datos.
- Plantear mas secciones en la aplicacion.

## Problemas conocidos

- Al no tener un cruzamiento de informacion se presenta un posible foco de falla.
- No es una una interlaz intuitiva.