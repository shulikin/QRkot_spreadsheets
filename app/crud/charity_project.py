from typing import Optional
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select

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
    ) -> List[List[str]]:
        """Получение списка проектов, отсортированных по времени выполнения."""
        project_objs = await session.execute(
            select(
                CharityProject.name,
                (func.julianday(CharityProject.close_date) - func.julianday(
                    CharityProject.create_date)).label('completion_days'),
                CharityProject.description,
            ).where(
                CharityProject.close_date.isnot(None)
            ).order_by('completion_days')
        )
        projects = project_objs.all()
        return [
            [project.name, project.completion_days, project.description]
            for project in projects
        ]


charity_project_crud = CRUDCharityProject(CharityProject)
