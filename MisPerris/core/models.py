from django.db import models
from django import forms

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=25)
    clave = models.CharField(max_length=25)
    pregunta_secreta = models.CharField(max_length=100)
    respuesta_secreta = models.CharField(max_length=50)
    
    def __str__(self):
        return self.usuario

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    # nRegion = models.IntegerField()

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

class Persona(models.Model):
    rut = models.IntegerField()
    rut_dv = models.CharField(max_length=1)
    email = models.EmailField( max_length=254)
    nombreCompleto = models.CharField(max_length=150)
    fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)
    telefono = models.IntegerField()
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipoVivienda = models.CharField( max_length=50)
    # nombre = models.CharField(max_length=50)
    # apellido = models.CharField(max_length=50)
    # direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Suscripcion(models.Model):
    n_suscripcion = models.AutoField(primary_key=True)
    abono = models.IntegerField()
    fechaPago = models.DateField()

    def __str__(self):
        return self.n_suscripcion

    class Meta:
        verbose_name = "Suscripcion"
        verbose_name_plural = "Suscripciones"

class Campania(models.Model):
    identificador = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    slogan = models.CharField(max_length=150)

    def __str__(self):
        return self.identificador


class Publicidad(models.Model):
    identificador = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='publi')
    logo = models.CharField(max_length=50)

    def __str__(self):
        return self.identificador

    class Meta:
        verbose_name = "Publicidad"
        verbose_name_plural = "Publicidad"

class Refugio(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

class GastoMensual(models.Model):
    nombre = models.CharField(max_length=50)
    fechaPago = models.DateField()
    tipo = models.CharField(max_length=50)

class Suministro(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    tipo = models.CharField(max_length=50)

class Raza(models.Model):
    nombre = models.CharField( max_length=50)

class Estado(models.Model):
    nombre = models.CharField( max_length=50)


GENERO_RADIO = (
        (1,'Macho'),
        (2,'Hembra'),
    )

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    
    genero = forms.ChoiceField(choices = GENERO_RADIO, widget=forms.RadioSelect())
    fechaIngreso = models.DateField()
    fechaNacimiento = models.DateField(null=True)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='pets')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    # rut_m = models.CharField(max_length=15)
    # edad = models.IntegerField()
    # raza = models.CharField(max_length=25)
    # chip = models.BooleanField()
    # n_chip = models.IntegerField()
    # tipo = models.CharField(max_length=50)


class AtencionMascota(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    diagnostico = models.CharField(max_length=150)

# class Comuna(models.Model):
    # NOMBRE_COMUNA = (
    #     (1401,'Pozo Almonte'),
    #     (1405,'Pica'),
    #     (1101,'Iquique'),
    #     (1404,'Huara'),
    #     (1403,'Colchane'),
    #     (1402,'Camiña'),
    #     (1107,'Alto Hospicio'),
    #     (2301,'Tocopilla'),
    #     (2104,'Taltal'),
    #     (2103,'Sierra Gorda'),
    #     (2203,'San Pedro de Atacama'),
    #     (2202,'Ollague'),
    #     (2102,'Mejillones'),
    #     (2302,'María Elena'),
    #     (2201,'Calama'),
    #     (2101,'Antofagasta'),
    #     (3301,'Vallenar'),
    #     (3103,'Tierra Amarilla'),
    #     (3304,'Huasco'),
    #     (3303,'Freirina'),
    #     (3202,'Diego de Almagro'),
    #     (3101,'Copiapó'),
    #     (3201,'Chañaral'),
    #     (3102,'Caldera'),
    #     (3302,'Alto del Carmen'),
    #     (4106,'Vicuña'),
    #     (4204,'Salamanca'),
    #     (4305,'Río Hurtado'),
    #     (4304,'Punitaqui'),
    #     (4105,'Paihuano'),
    #     (4301,'Ovalle'),
    #     (4303,'Monte Patria'),
    #     (4203,'Los Vilos'),
    #     (4101,'La Serena'),
    #     (4104,'La Higuera'),
    #     (4201,'Illapel'),
    #     (4102,'Coquimbo'),
    #     (4302,'Combarbalá'),
    #     (4202,'Canela'),
    #     (4103,'Andacollo'),
    #     (5405,'Zapallar'),
    #     (5109,'Viña del Mar'),
    #     (5108,'Villa Alemana'),
    #     (5101,'Valparaíso'),
    #     (5606,'Santo Domingo'),
    #     (5706,'Santa María'),
    #     (5701,'San Felipe'),
    #     (5304,'San Esteban'),
    #     (5601,'San Antonio'),
    #     (5303,'Rinconada'),
    #     (5107,'Quintero'),
    #     (5106,'Quilpué'),
    #     (5501,'Quillota'),
    #     (5705,'Putaendo'),
    #     (5105,'Puchuncaví'),
    #     (5404,'Petorca'),
    #     (5403,'Papudo'),
    #     (5704,'Panquehue'),
    #     (5507,'Olmué'),
    #     (5506,'Nogales'),
    #     (5301,'Los Andes'),
    #     (5703,'Llay Llay'),
    #     (5505,'Limache'),
    #     (5401,'La Ligua'),
    #     (5504,'La Cruz'),
    #     (5104,'Juan Fernández'),
    #     (5201,'Isla de Pascua'),
    #     (5503,'Hijuelas'),
    #     (5605,'El Tabo'),
    #     (5604,'El Quisco'),
    #     (5103,'Con Cón'),
    #     (5702,'Catemu'),
    #     (5102,'Casablanca'),
    #     (5603,'Cartagena'),
    #     (5302,'Calle Larga'),
    #     (5502,'Calera'),
    #     (5402,'Cabildo'),
    #     (5602,'Algarrobo'),
    #     (6310,'Santa Cruz'),
    #     (6117,'San Vicente'),
    #     (6301,'San Fernando'),
    #     (6116,'Requínoa'),
    #     (6115,'Rengo'),
    #     (6101,'Rancagua'),
    #     (6114,'Quinta de Tilcoco'),
    #     (6309,'Pumanque'),
    #     (6308,'Placilla'),
    #     (6201,'Pichilemu'),
    #     (6113,'Pichidegua'),
    #     (6112,'Peumo'),
    #     (6307,'Peralillo'),
    #     (6206,'Paredones'),
    #     (6306,'Palmilla'),
    #     (6111,'Olivar'),
    #     (6205,'Navidad'),
    #     (6305,'Nancagua'),
    #     (6110,'San Francisco de Mostazal'),
    #     (6204,'Marchigüe'),
    #     (6109,'Malloa'),
    #     (6108,'Machalí'),
    #     (6304,'Lolol'),
    #     (6203,'Litueche'),
    #     (6107,'Las Cabras'),
    #     (6202,'La Estrella'),
    #     (6106,'Graneros'),
    #     (6105,'Doñihue'),
    #     (6104,'Coltauco'),
    #     (6103,'Coinco'),
    #     (6102,'Codegua'),
    #     (6303,'Chimbarongo'),
    #     (6302,'Chépica'),
    #     (7408,'Yerbas Buenas'),
    #     (7407,'Villa Alegre'),
    #     (7309,'Vichuquén'),
    #     (7308,'Teno'),
    #     (7101,'Talca'),
    #     (7110,'San Rafael'),
    #     (7406,'San Javier'),
    #     (7109,'San Clemente'),
    #     (7307,'Sagrada Familia'),
    #     (7306,'Romeral'),
    #     (7108,'Río Claro'),
    #     (7405,'Retiro'),
    #     (7305,'Rauco'),
    #     (7107,'Pencahue'),
    #     (7203,'Pelluhue'),
    #     (7106,'Pelarco'),
    #     (7404,'Parral'),
    #     (7304,'Molina'),
    #     (7105,'Maule'),
    #     (7403,'Longaví'),
    #     (7401,'Linares'),
    #     (7303,'Licantén'),
    #     (7302,'Hualañé'),
    #     (7104,'Empedrado'),
    #     (7301,'Curicó'),
    #     (7103,'Curepto'),
    #     (7102,'Constitución'),
    #     (7402,'Colbún'),
    #     (7202,'Chanco'),
    #     (7201,'Cauquenes'),
    #     (8421,'Yungay'),
    #     (8313,'Yumbel'),
    #     (8312,'Tucapel'),
    #     (8420,'Trehuaco'),
    #     (8111,'Tomé'),
    #     (8207,'Tirúa'),
    #     (8110,'Talcahuano'),
    #     (8109,'Santa Juana'),
    #     (8311,'Santa Bárbara'),
    #     (8310,'San Rosendo'),
    #     (8108,'San Pedro de la Paz'),
    #     (8419,'San Nicolás'),
    #     (8418,'San Ignacio'),
    #     (8417,'San Fabián'),
    #     (8416,'San Carlos'),
    #     (8415,'Ránquil'),
    #     (8414,'Quirihue'),
    #     (8413,'Quillón'),
    #     (8309,'Quilleco'),
    #     (8308,'Quilaco'),
    #     (8412,'Portezuelo'),
    #     (8411,'Pinto'),
    #     (8107,'Penco'),
    #     (8410,'Pemuco'),
    #     (8409,'Ñiquén'),
    #     (8408,'Ninhue'),
    #     (8307,'Negrete'),
    #     (8306,'Nacimiento'),
    #     (8305,'Mulchén'),
    #     (8106,'Lota'),
    #     (8301,'Los Ángeles'),
    #     (8206,'Los Álamos'),
    #     (8201,'Lebu'),
    #     (8304,'Laja'),
    #     (8105,'Hualqui'),
    #     (8112,'Hualpén'),
    #     (8104,'Florida'),
    #     (8407,'El Carmen'),
    #     (8205,'Curanilahue'),
    #     (8102,'Coronel'),
    #     (8204,'Contulmo'),
    #     (8101,'Concepción'),
    #     (8405,'Coihueco'),
    #     (8404,'Coelemu'),
    #     (8403,'Cobquecura'),
    #     (8406,'Chillán Viejo'),
    #     (8401,'Chillán'),
    #     (8103,'Chiguayante'),
    #     (8203,'Cañete'),
    #     (8303,'Cabrero'),
    #     (8402,'Bulnes'),
    #     (8202,'Arauco'),
    #     (8302,'Antuco'),
    #     (8314,'Alto Bío Bío'),
    #     (9120,'Villarrica'),
    #     (9119,'Vilcún'),
    #     (9211,'Victoria'),
    #     (9210,'Traiguén'),
    #     (9118,'Toltén'),
    #     (9117,'Teodoro Schmidt'),
    #     (9101,'Temuco'),
    #     (9116,'Saavedra'),
    #     (9209,'Renaico'),
    #     (9208,'Purén'),
    #     (9115,'Pucón'),
    #     (9114,'Pitrufquén'),
    #     (9113,'Perquenco'),
    #     (9112,'Padre Las Casas'),
    #     (9111,'Nueva Imperial'),
    #     (9110,'Melipeuco'),
    #     (9207,'Lumaco'),
    #     (9206,'Los Sauces'),
    #     (9205,'Lonquimay'),
    #     (9109,'Loncoche'),
    #     (9108,'Lautaro'),
    #     (9107,'Gorbea'),
    #     (9106,'Galvarino'),
    #     (9105,'Freire'),
    #     (9204,'Ercilla'),
    #     (9104,'Curarrehue'),
    #     (9203,'Curacautín'),
    #     (9103,'Cunco'),
    #     (9202,'Collipulli'),
    #     (9121,'Cholchol'),
    #     (9102,'Carahue'),
    #     (9201,'Angol'),
    #     (10307,'San Pablo'),
    #     (10306,'San Juan de la Costa'),
    #     (10305,'Río Negro'),
    #     (10210,'Quinchao'),
    #     (10209,'Quemchi'),
    #     (10208,'Quellón'),
    #     (10207,'Queilén'),
    #     (10304,'Puyehue'),
    #     (10303,'Purranque'),
    #     (10206,'Puqueldón'),
    #     (10109,'Puerto Varas'),
    #     (10302,'Puerto Octay'),
    #     (10101,'Puerto Montt'),
    #     (10404,'Palena'),
    #     (10301,'Osorno'),
    #     (10108,'Maullín'),
    #     (10106,'Los Muermos'),
    #     (10107,'Llanquihue'),
    #     (10403,'Hualaihué'),
    #     (10402,'Futaleufú'),
    #     (10105,'Frutillar'),
    #     (10104,'Fresia'),
    #     (10205,'Dalcahue'),
    #     (10204,'Curaco de Vélez'),
    #     (10103,'Cochamó'),
    #     (10203,'Chonchi'),
    #     (10401,'Chaitén'),
    #     (10201,'Castro'),
    #     (10102,'Calbuco'),
    #     (10202,'Ancud'),
    #     (11303,'Tortel'),
    #     (11402,'Río Ibáñez'),
    #     (11302,"O'Higgins"),
    #     (11102,'Lago Verde'),
    #     (11203,'Guaitecas'),
    #     (11101,'Coihaique'),
    #     (11301,'Cochrane'),
    #     (11202,'Cisnes'),
    #     (11401,'Chile Chico'),
    #     (11201,'Aysén'),
    #     (12202,'Antartica'),
    #     (12402,'Torres del Paine'),
    #     (12303,'Timaukel'),
    #     (12104,'San Gregorio'),
    #     (12103,'Río Verde'),
    #     (12101,'Punta Arenas'),
    #     (12302,'Primavera'),
    #     (12301,'Porvenir'),
    #     (12401,'Natales'),
    #     (12102,'Laguna Blanca'),
    #     (12201,'Cabo de Hornos'),
    #     (13135,'Santiago Sur'),
    #     (13134,'Santiago Oeste'),
    #     (14202,'Lampa'),
    #     (13132,'Vitacura'),
    #     (13303,'Til-Til'),
    #     (13601,'Talagante'),
    #     (13101,'Santiago'),
    #     (13131,'San Ramón'),
    #     (13505,'San Pedro'),
    #     (13130,'San Miguel'),
    #     (13203,'San José de Maipo'),
    #     (13129,'San Joaquín'),
    #     (13401,'San Bernardo'),
    #     (13128,'Renca'),
    #     (13127,'Recoleta'),
    #     (13126,'Quinta Normal'),
    #     (13125,'Quilicura'),
    #     (13201,'Puente Alto'),
    #     (13124,'Pudahuel'),
    #     (13123,'Providencia'),
    #     (13202,'Pirque'),
    #     (13122,'Peñalolén'),
    #     (13605,'Peñaflor'),
    #     (13121,'Pedro Aguirre Cerda'),
    #     (13404,'Paine'),
    #     (13604,'Padre Hurtado'),
    #     (13120,'Ñuñoa'),
    #     (13501,'Melipilla'),
    #     (13504,'María Pinto'),
    #     (13119,'Maipú'),
    #     (13118,'Macul'),
    #     (13117,'Lo Prado'),
    #     (13116,'Lo Espejo'),
    #     (13115,'Lo Barnechea'),
    #     (13114,'Las Condes'),
    #     (13113,'La Reina'),
    #     (13112,'La Pintana'),
    #     (13111,'La Granja'),
    #     (13110,'La Florida'),
    #     (13109,'La Cisterna'),
    #     (13603,'Isla de Maipo'),
    #     (13108,'Independencia'),
    #     (13107,'Huechuraba'),
    #     (13106,'Estación Central'),
    #     (13602,'El Monte'),
    #     (13105,'El Bosque'),
    #     (13503,'Curacaví'),
    #     (13104,'Conchalí'),
    #     (13301,'Colina'),
    #     (13103,'Cerro Navia'),
    #     (13102,'Cerrillos'),
    #     (13403,'Calera de Tango'),
    #     (13402,'Buin'),
    #     (13502,'Alhué'),
    #     (14101,'Valdivia'),
    #     (14204,'Río Bueno'),
    #     (14108,'Panguipulli'),
    #     (14107,'Paillaco'),
    #     (14106,'Mariquina'),
    #     (14105,'Máfil'),
    #     (14104,'Los Lagos'),
    #     (14103,'Lanco'),
    #     (14203,'Lago Ranco'),
    #     (14201,'La Unión'),
    #     (14202,'Futrono'),
    #     (14102,'Corral'),
    #     (15201,'Putre'),
    #     (15202,'General Lagos'),
    #     (15102,'Camarones'),
    #     (15101,'Arica'),
    # )
    # id = models.IntegerField(choices=NOMBRE_COMUNA, primary_key=True )
    # nombre = models.CharField(max_length=50, choices=NOMBRE_COMUNA)

# class Region(models.Model):
    # NOMBRE_REGION = (
    #     (1,'Tarapacá'),
    #     (2,'Antofagasta'),
    #     (3,'Atacama'),
    #     (4,'Coquimbo'),
    #     (5,"Valparaíso"),
    #     (6,"O'Higgins"),
    #     (7,"Maule"),
    #     (8,"Bío Bío"),
    #     (9,"Araucanía"),
    #     (10,"Los Lagos"),
    #     (11,"Aysén"),
    #     (12,"Magallanes"),
    #     (13,"Región Metropolitana Santiago"),
    #     (14,"Los Ríos"),
    #     (15,"Arica y Parinacota"),
    # )
    # id = models.IntegerField(choices=NOMBRE_REGION    , primary_key=True )
    # nombre = models.CharField(max_length=50, choices=NOMBRE_REGION)
    # comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    # def __str__(self):
        # return self.nombre

    # class Meta:
    #     verbose_name = "Region"
    #     verbose_name_plural = "Regiones"




