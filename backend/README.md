# Tableのマイグレーション

マイグレーションの作成
poetry run alembic revision --autogenerate -m {ファイル名}

マイグレーションの反映
poetry run alembic upgrade head

マイグレーションの巻き戻し
poetry run alembic downgrade base
