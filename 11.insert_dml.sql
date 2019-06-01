insert into programs values (1, 'математика и информационные технологии');
insert into programs values (2, 'теоретическая физика');

insert into courses values(1, 'Алгебра');
insert into courses values(2, 'Математический Анализ');
insert into courses values(3, 'Дискретная математика');
insert into courses values(4, 'Химия');

insert into programs_courses values(1, 1, 1);
insert into programs_courses values(1, 1, 2);
insert into programs_courses values(1, 2, 1);
insert into programs_courses values(1, 2, 2);
insert into programs_courses values(1, 3, 1);
insert into programs_courses values(1, 4, 2);
insert into programs_courses values(2, 1, 1);
insert into programs_courses values(2, 1, 2);
insert into programs_courses values(2, 2, 1);
insert into programs_courses values(2, 2, 2);
insert into programs_courses values(2, 3, 1);

insert into students(program_id, card, surname, name) values(1, '180101', 'Битов', 'Антон');
insert into students(program_id, card, surname, name) values(2, '180201', 'Аргонова', 'Виолетта');

insert into marks values(1, 1, 4);
insert into marks values(1, 3, 4);
insert into marks values(2, 2, 3);
insert into marks values(2, 1, 5);
insert into marks values(2, 4, 4);
