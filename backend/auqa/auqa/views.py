import sqlite3

from django.conf import settings
from django.shortcuts import render


def home(request):
    """Главная страница с актуальными рекордами непосредственно из БД игры."""
    leaderboard = []
    database_path = settings.GAME_DATABASE
    error = None

    try:
        with sqlite3.connect(f"file:{database_path.as_posix()}?mode=ro", uri=True, timeout=2) as connection:
            rows = connection.execute(
                """
                SELECT levels.name, records.best_progress, records.attempts
                FROM levels
                JOIN records ON records.level_id = levels.id
                ORDER BY records.best_progress DESC, levels.id ASC
                """
            ).fetchall()
        leaderboard = [
            {"rank": rank, "name": name, "progress": progress, "attempts": attempts}
            for rank, (name, progress, attempts) in enumerate(rows, start=1)
        ]
    except (sqlite3.Error, OSError):
        error = "Не удалось прочитать таблицу рекордов. Запустите игру хотя бы один раз."

    return render(request, "home.html", {"leaderboard": leaderboard, "leaderboard_error": error})
