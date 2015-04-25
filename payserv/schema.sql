drop table if exists addr_table;
create table hash_table (
  id integer primary key autoincrement,
  addr text not null
);