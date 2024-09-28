create table cancion(
idCancion int auto_increment primary key,
artista varchar(45) not null,
imagen varchar(2080),
audio varchar(2080),
name_cancion varchar(45),
tiempo int(5)
);

create table lista_reproduccion(
idlistaR int auto_increment primary key,
nombre varchar(45) not null,
descripcion varchar(45)  null,
fecha_creacion datetime
);

create table reproductor(
id int auto_increment primary key,
idlistaR int,
idCancion int,
posicion int not null,
foreign key (idlistaR) references lista_reproduccion(idlistaR),
foreign key (idCancion) references cancion(idCancion),
unique(idlistaR,idCancion)
);

create table cola(
idcola int  auto_increment primary key,
idlistaR int,
idCancion int,
posicion int not null,
foreign key (idlistaR) references lista_reproduccion(idlistaR),
foreign key (idCancion) references cancion(idCancion)
);