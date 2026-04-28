# fastapistudies
INSTALLATIONS:
    pip install psycopg2-binary  -   conectar pgsql 
    pip install pymysql   -   conectar mysql

    SQLITE3: SQLACHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
             engine = create_engine(SQLACHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


    POSTGRESQL: SQLACHEMY_DATABASE_URL = "postgresql://postgres:Brunexx2207.@localhost/TodoApplicationDataBase"


    SQLACHEMY_DATABASE_URL = "mysql+pymysql://root:1234@127.0.0.1:3006/TodoApplicationDataBase"

o que é tags no apirouter()
