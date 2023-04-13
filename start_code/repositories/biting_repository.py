from db.run_sql import run_sql
from models.biting import Biting
from models.human import Human
import repositories.human_repository as human_repository
from models.zombie import Zombie
import repositories.zombie_repository as zombie_repository

def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for result in results:
        biting = Biting(result["human"], result["zombie"])
        bitings.append(biting)
    return bitings

def select(id):
    biting = None
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        biting = Biting(result["human"], result["zombie"])
    return biting

def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(biting):
    sql = "UPDATE bitings SET (%s, %s) WHERE zombie = %s"
    values = [biting.human.id, biting.zombie.id, biting.id]
    run_sql(sql, values)