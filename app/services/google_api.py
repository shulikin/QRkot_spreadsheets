from datetime import datetime

from aiogoogle import Aiogoogle
from app.core.config import settings, Constant


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    """Создание нового Google Sheets и установка прав на чтение и запись."""
    now_date_time = datetime.now().strftime(settings.format)
    service = await wrapper_services.discover(
        Constant.SHEETS_API_NAME,
        Constant.SHEETS_API_VERSION
    )

    spreadsheet_body = {
        'properties': {
            'title': Constant.SHEET_TITLE_TEMPLATE.format(date=now_date_time),
            'locale': Constant.SHEET_LOCALE
        },
        'sheets': [{
            'properties': {
                'sheetType': Constant.SHEETS_API_TYPE,
                'sheetId': Constant.SHEET_ID,
                'title': Constant.SHEET_NAME,
                'gridProperties': Constant.SHEET_GRID_PROPERTIES
            }
        }]
    }

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    """Добавление прав на чтение и запись для текущего пользователя."""
    permissions_body = {
        'type': Constant.PERMISSION_TYPE,
        'role': Constant.PERMISSION_ROLE,
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover(
        Constant.DRIVE_API_NAME,
        Constant.DRIVE_API_VERSION
    )
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields='id'
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        project_list: list,
        wrapper_services: Aiogoogle
) -> None:
    """Обновление значений в Google Sheets."""
    now_date_time = datetime.now().strftime(settings.format)
    service = await wrapper_services.discover(
        Constant.SHEETS_API_NAME,
        Constant.SHEETS_API_VERSION
    )

    table_values = [
        [cell.format(
            date=now_date_time) if '{date}' in cell else cell for cell in row]
        for row in Constant.TABLE_TEMPLATE
    ] + [
        [str(project[0]), str(project[1]), str(project[2])]
        for project in project_list
    ]

    update_body = {
        'majorDimension': Constant.MAJOR_DIMENSION_ROWS,
        'values': table_values
    }

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=Constant.SPREADSHEET_RANGE,
            valueInputOption=Constant.VALUE_INPUT_OPTION_USER_ENTERED,
            json=update_body,
        )
    )
