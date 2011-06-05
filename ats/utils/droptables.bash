#!/bin/bash

psql -At ats -c "select 'drop table '||tablename||' cascade;' from pg_tables where tablename like 'main_%'" | psql ats 
