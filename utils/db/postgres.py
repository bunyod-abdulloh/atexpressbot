from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    # ======================= TABLE | USERS =======================
    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NULL,
        username varchar(100) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,        
        phone VARCHAR(30) NULL,
        address VARCHAR(500) NULL,
        passport_a_side VARCHAR(300) NULL,
        passport_b_side VARCHAR(300) NULL,
        balance BIGINT DEFAULT 0                
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self, username, telegram_id):
        sql = "INSERT INTO users (username, telegram_id) VALUES($1, $2)"
        return await self.execute(sql, username, telegram_id, fetchrow=True)

    async def update_user_fullname(self, fullname, telegram_id):
        sql = "UPDATE users SET full_name=$1 WHERE telegram_id=$2"
        return await self.execute(sql, fullname, telegram_id, fetchrow=True)

    async def update_user_phone(self, phone, telegram_id):
        sql = "UPDATE users SET phone=$1 WHERE telegram_id=$2"
        return await self.execute(sql, phone, telegram_id, fetchrow=True)

    async def update_user_address(self, address, telegram_id):
        sql = "UPDATE users SET address=$1 WHERE telegram_id=$2"
        return await self.execute(sql, address, telegram_id, fetchrow=True)

    async def update_user_passport_a_side(self, passport_a_side, telegram_id):
        sql = "UPDATE users SET passport_a_side=$1 WHERE telegram_id=$2"
        return await self.execute(sql, passport_a_side, telegram_id, fetchrow=True)

    async def update_user_passport_b_side(self, passport_b_side, telegram_id):
        sql = "UPDATE users SET passport_b_side=$1 WHERE telegram_id=$2"
        return await self.execute(sql, passport_b_side, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, telegram_id):
        sql = f"SELECT * FROM users WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    async def delete_users(self):
        await self.execute("DELETE FROM users WHERE TRUE", execute=True)

    async def delete_user(self, telegram_id):
        await self.execute(f"DELETE FROM users WHERE telegram_id='{telegram_id}'", execute=True)

    async def drop_table_users(self):
        await self.execute("DROP TABLE users", execute=True)

    # ======================= TABLE | TABLES =======================
    async def create_table_tables(self):
        sql = """
        CREATE TABLE IF NOT EXISTS medialar_tables (
        table_number INTEGER PRIMARY KEY NOT NULL,
        channel_id VARCHAR(50) NULL,
        comment TEXT NULL,
        files BOOLEAN DEFAULT FALSE
        );
        """
        await self.execute(sql, execute=True)

    async def select_all_tables(self, table_type):
        sql = f"SELECT * FROM medialar_tables WHERE table_type='{table_type}' ORDER BY table_number ASC"
        return await self.execute(sql, fetch=True)

    async def select_table_tables(self):
        sql = "SELECT * FROM medialar_tables"
        return await self.execute(sql, fetch=True)

    async def get_channel_id(self, table_number):
        sql = f"SELECT channel_id FROM medialar_tables WHERE table_number='{table_number}'"
        return await self.execute(sql, fetchrow=True)

    async def select_media_by_id(self, table_number):
        sql = f"SELECT * FROM medialar_tables WHERE table_number='{table_number}'"
        return await self.execute(sql, fetchrow=True)

    async def delete_table_tables(self, table_number):
        await self.execute(f"DELETE FROM medialar_tables WHERE table_number='{table_number}'", execute=True)

    async def drop_table_tables(self):
        await self.execute(f"DROP TABLE medialar_tables", execute=True)
