from db.run_sql import run_sql
from models.human import Human
from models.zombie import Zombie
from models.zombie_type import ZombieType
import repositories.zombie_type_repository as zombie_type_repository

def save(zombie):
    sql = "INSERT INTO zombies (name, zombie_type_id) VALUES (%s, %s) RETURNING id"
    values = [zombie.name, zombie.zombie_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    zombie.id = id


def select_all():
    zombies = []
    sql = "SELECT * FROM zombies"
    results = run_sql(sql)
    for result in results:
        zombie_type = zombie_type_repository.select(result["zombie_type_id"])
        zombie = Zombie(result["name"], zombie_type, result["id"])
        zombies.append(zombie)
    return zombies


def select(id):
    sql = "SELECT * FROM zombies WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        zombie_type = zombie_type_repository.select(result["zombie_type_id"])
        zombie = Zombie(result["name"], zombie_type, result["id"])
    return zombie

def delete_all():
    sql = "DELETE FROM zombies"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM zombies WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(zombie):
    sql = "UPDATE zombies SET (name, zombie_type_id) = (%s, %s) WHERE id = %s"
    values = [zombie.name, zombie.zombie_type.id, zombie.id]
    run_sql(sql, values)
