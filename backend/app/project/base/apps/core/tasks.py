from abc import ABC

from celery.utils.log import get_task_logger
from django.core.files.storage import default_storage

from project import celery_app


class BaseTask(ABC, celery_app.Task):
    name = __name__
    description = ''
    ignore_result = False
    max_retries = 5
    logger = get_task_logger(__name__)

    def run(self, *args, **kwargs):
        return self._run(*args, **kwargs)

    def _run(self, *args, **kwargs):
        raise NotImplementedError

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.logger.error('{0!r} failed: {1!r}'.format(task_id, exc))
        super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)


class DeleteFromStorageTask(BaseTask):
    name = 'project.base.apps.core.DeleteFromStorageTask'
    description = 'Delete file from storage'

    def _run(self, *args, **kwargs):
        default_storage.delete(kwargs.get('path'))


delete_from_storage_task = DeleteFromStorageTask()
