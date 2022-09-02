create database ProjetoQuiz;

use ProjetoQuiz;

create table Cadastro(
codigo int not null auto_increment primary key,
nome varchar(120) not null,
pontuacao int not null,
tema varchar(30) not null
) engine = InnoDB;

select * from Cadastro;
drop table Cadastro;

        