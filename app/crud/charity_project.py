from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select

from app.core.config import Constant
from app.crud.base import CRUDBaseAdvanced
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBaseAdvanced):
    """Класс для работы с операциями CRUD."""

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        """Поиск по имени с использованием общего метода."""
        return await self.get_by_kwargs(session, name=project_name)

    async def get_projects_by_completion_rate(
            self, session: AsyncSession
    ) -> list[list]:
        """Получение списка проектов."""
        project_objs = await session.execute(
            select(CharityProject).where(
                CharityProject.close_date.isnot(None)
            ).order_by(
                func.coalesce(
                    CharityProject.close_date - CharityProject.create_date,
                    Constant.RETURNED_NULL
                )
            )
        )
        project_objs = project_objs.scalars().all()
        return [
            [
                project.name,
                str(project.close_date - project.create_date),
                project.description
            ]
            for project in project_objs
        ]


charity_project_crud = CRUDCharityProject(CharityProject)
