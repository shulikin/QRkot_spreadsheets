from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

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
            select(CharityProject).where(CharityProject
                                         .close_date.isnot(None))
        )
        project_objs = project_objs.scalars().all()
        project_list = [
            [
                project.name,
                str(project.close_date - project.create_date),
                project.description
            ]
            for project in project_objs
        ]
        return sorted(project_list, key=lambda x: x[1])


charity_project_crud = CRUDCharityProject(CharityProject)
