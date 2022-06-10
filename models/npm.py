from typing import Optional
from pydantic import BaseModel
from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, SQL

NpmDatesForGithub = Table('NpmDatesForGithub', meta,
    Column('id', Integer, primary_key=True),
    Column('dependencyName', String(150)),
    Column('repository', String(100)),
    Column('githubstar', String(7)),
    Column('githubfoks', String(5)),
    Column('githubwachers', String(5)),
    Column('abondoned', String(15)),
    Column('maintainers', String(5)),
    Column('contributors', String(10))
    )

NpmDatesForComplementary = Table('NpmDatesForComplementary', meta,
    Column('id', Integer, primary_key=True),
    Column('codeCoverage', String(15)),
    Column('linters', String(100)),
    Column('dependenats', String(10)),
    Column('npmStars', String(5)),
    Column('dependencies', String(5)),
    Column('license', String(15)),
    Column('totalissues', String(5)),
    Column('openissues', String(10)),
    Column('securityAdvisories', String(10)),
    Column('idNpmDatesForGithub', Integer, ForeignKey('NpmDatesForGithub.id'))
    )

meta.create_all(SQL)