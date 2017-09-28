-- 创建一个数据库
create table `users` (
    `id` int(11) not null auto_increment,
    `email` varchar(25) collate utf8_bin not null,
    `password` varchar(255) collate utf8_bin not null,
     primary key(`id`)
)