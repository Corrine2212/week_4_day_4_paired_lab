from db.run_sql import run_sql
from models.zombie_type import ZombieType

def save(zombie_type):
    sql = "INSERT INTO zombie_types (name) VALUES (%s) RETURNING id"
    values = [zombie_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    zombie_type.id = id


def select_all():
    zombie_types = []
    sql = "SELECT * FROM zombie_types"
    results = run_sql(sql)
    for result in results:
        zombie_type = ZombieType(result["name"], result["id"])
        zombie_types.append(zombie_type)
    return zombie_types


def select(id):
    zombie_type = None 
    sql = "SELECT * FROM zombie_types WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
    zombie_type = ZombieType(result["name"], result["id"])
    return zombie_type


def delete_all():
    sql = "DELETE FROM zombie_types"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM zombie_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(zombie_type):
    sql = "UPDATE zombie_types SET name = %s WHERE id = %s"
    values = [zombie_type.name, zombie_type.id]
    run_sql(sql, values)
