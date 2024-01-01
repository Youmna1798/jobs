# products/tables.py
import django_tables2 as tables
from myapp.models import Job

class JobTable(tables.Table):
    title = tables.LinkColumn('page_detail', args=[tables.A('pk')])

    class Meta:
        model = Job
        fields = ('title', 'description', 'published_date')