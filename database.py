import aiosqlite
from datetime import datetime
import config

async def init_db():
    async with aiosqlite.connect(config.DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                nickname TEXT DEFAULT NULL,
                points INTEGER DEFAULT 0,
                coins INTEGER DEFAULT 0,
                last_bonus TIMESTAMP,
                last_komaru TIMESTAMP
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                user_id INTEGER,
                card_id TEXT,
                amount INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, card_id)
            )
        ''')
        await db.commit()

async def get_user(user_id: int):
    async with aiosqlite.connect(config.DB_NAME) as db:
        async with db.execute(
            "SELECT nickname, points, coins, last_bonus, last_komaru FROM users WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            user = await cursor.fetchone()
            if not user:
                await db.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
                await db.commit()
                return (None, 0, 0, None, None)
            return user

async def update_nickname(user_id: int, nickname: str):
    async with aiosqlite.connect(config.DB_NAME) as db:
        await db.execute(
            "UPDATE users SET nickname = ? WHERE user_id = ?",
            (nickname, user_id)
        )
        await db.commit()

async def add_reward(user_id: int, points: int, coins: int, card_id: str, timer_type: str = "last_bonus"):
    if timer_type not in ("last_bonus", "last_komaru"):
        timer_type = "last_bonus"

    async with aiosqlite.connect(config.DB_NAME) as db:
        query = f"UPDATE users SET points = points + ?, coins = coins + ?, {timer_type} = ? WHERE user_id = ?"
        await db.execute(query, (points, coins, datetime.now().isoformat(), user_id))
        await db.execute('''
            INSERT INTO inventory (user_id, card_id, amount) 
            VALUES (?, ?, 1) 
            ON CONFLICT(user_id, card_id) DO UPDATE SET amount = amount + 1
        ''', (user_id, card_id))
        
        await db.commit()

async def get_inventory(user_id: int):
    async with aiosqlite.connect(config.DB_NAME) as db:
        async with db.execute("SELECT card_id, amount FROM inventory WHERE user_id = ?", (user_id,)) as cursor:
            return await cursor.fetchall()

async def get_top(order_by: str = "points", limit: int = 10):
    if order_by not in ("points", "coins"):
        order_by = "points"

    async with aiosqlite.connect(config.DB_NAME) as db:
        query = f"SELECT nickname, user_id, {order_by} FROM users ORDER BY {order_by} DESC LIMIT ?"
        async with db.execute(query, (limit,)) as cursor:
            return await cursor.fetchall()

