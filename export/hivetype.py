#!/usr/bin/env python
# -*- coding:utf-8 -*-


class HiveType:
    @staticmethod
    def change_type(ctype):
        octype = ctype
        ctype = ctype.lower()
        if ctype in ("varchar", "char"):
            ctype = "string"
        if ctype in ("datetime",):
            ctype = "timestamp"
        if ctype == "timestamp":
            ctype = "string"
        if ctype in ("text", "longtext"):
            ctype = "string"
        if ctype == "time":
            ctype = "string"
        if ctype == "text":
            ctype = "string"
        if ctype in ("long", "int"):
            ctype = "bigint"
        if ctype in ("smallint", "mediumint", "tinyint"):
            ctype = "int"
        if ctype in ("decimal", "float"):
            ctype = "double"
        if ctype == "date":
            ctype = "string"
        if ctype == "array":
            ctype = "string"
        print "类型转换:", str(octype) + " -> " + str(ctype)
        return ctype

    @staticmethod
    def key_words(cname):
        cname = cname.upper()
        keys = "ADD, ADMIN, AFTER, ANALYZE, ARCHIVE, ASC, BEFORE, BUCKET, BUCKETS," \
                "CASCADE, CHANGE, CLUSTER, CLUSTERED, CLUSTERSTATUS, COLLECTION," \
                "COLUMNS, COMMENT, COMPACT, COMPACTIONS, COMPUTE, CONCATENATE," \
                "CONTINUE, DATA, DATABASES, DATETIME, DAY, DBPROPERTIES," \
                "DEFERRED, DEFINED, DELIMITED, DEPENDENCY, DESC, DIRECTORIES," \
                "DIRECTORY, DISABLE, DISTRIBUTE, ELEM_TYPE, ENABLE," \
                "ESCAPED, EXCLUSIVE, EXPLAIN, EXPORT, FIELDS, FILE," \
                "FILEFORMAT, FIRST, FORMAT, FORMATTED, FUNCTIONS," \
                "HOLD_DDLTIME, HOUR, IDXPROPERTIES, IGNORE, INDEX, INDEXES, INPATH," \
                "INPUTDRIVER, INPUTFORMAT, ITEMS, JAR, KEYS, KEY_TYPE, LIMIT, LINES," \
                "LOAD, LOCATION, LOCK, LOCKS, LOGICAL, LONG, MAPJOIN, MATERIALIZED," \
                "METADATA, MINUS, MINUTE, MONTH, MSCK, NOSCAN, NO_DROP, OFFLINE, OPTION," \
                "OUTPUTDRIVER, OUTPUTFORMAT, OVERWRITE, OWNER, PARTITIONED, PARTITIONS," \
                "PLUS, PRETTY, PRINCIPALS, PROTECTION, PURGE, READ, READONLY, REBUILD, RECORDREADER," \
                "RECORDWRITER, REGEXP, RELOAD, RENAME, REPAIR, REPLACE, REPLICATION, RESTRICT," \
                "REWRITE,RLIKE, ROLE, ROLES, SCHEMA, SCHEMAS, SECOND, SEMI, SERDE, SERDEPROPERTIES,SERVER," \
                "SETS, SHARED, SHOW, SHOW_DATABASE, SKEWED, SORT, SORTED, SSL, STATISTICS," \
                "STORED, STREAMTABLE, STRING, STRUCT, TABLES, TBLPROPERTIES, TEMPORARY, TERMINATED," \
                "TINYINT, TOUCH, TRANSACTIONS, UNARCHIVE, UNDO, UNIONTYPE, UNLOCK, UNSET, UNSIGNED," \
                "URI, USE, UTC, UTCTIMESTAMP, VALUE_TYPE, VIEW, WHILE, YEAR," \
                "ALL, ALTER, AND, ARRAY, AS, AUTHORIZATION, BETWEEN, BIGINT, BINARY," \
                "BOOLEAN, BOTH, BY, CASE, CAST, CHAR, COLUMN, CONF, CREATE, CROSS," \
                "CUBE, CURRENT, CURRENT_DATE, CURRENT_TIMESTAMP, CURSOR, DATABASE," \
                "DATE, DECIMAL, DELETE, DESCRIBE, DISTINCT, DOUBLE, DROP, ELSE, END," \
                "EXCHANGE, EXISTS, EXTENDED, EXTERNAL, FALSE, FETCH, FLOAT, FOLLOWING," \
                "FOR, FROM, FULL, FUNCTION, GRANT, GROUP, GROUPING, HAVING, IF, IMPORT," \
                "IN, INNER, INSERT, INT, INTERSECT, INTERVAL, INTO, IS, JOIN, LATERAL, LEFT," \
                "LESS, LIKE, LOCAL, MACRO, MAP, MORE, NONE, NOT, NULL, OF, ON, OR, ORDER,OUT," \
                "OUTER, OVER, PARTIALSCAN, PARTITION, PERCENT, PRECEDING, PRESERVE, PROCEDURE," \
                "RANGE,READS, REDUCE, REVOKE, RIGHT, ROLLUP, ROW, ROWS, SELECT, SET, SMALLINT, TABLE," \
                "TABLESAMPLE,THEN, TIMESTAMP, TO, TRANSFORM, TRIGGER, TRUE, TRUNCATE, UNBOUNDED, UNION," \
                "UNIQUEJOIN,UPDATE, USER, USING, UTC_TMESTAMP, VALUES, VARCHAR, WHEN, WHERE, WINDOW, WITH"
        keys_set = set()
        for key in keys.split(","):
            keys_set.add(key.strip())
        if cname in keys_set:
            return True
        else:
            return False