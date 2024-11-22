from marshmallow import Schema, fields, post_dump

from app.infrastructure.utils import DATETIME_FORMAT


class DefaultSchema(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(format=DATETIME_FORMAT, dump_only=True)
    updated_at = fields.DateTime(format=DATETIME_FORMAT, dump_only=True)

    @post_dump(pass_many=True)
    def transform_ids_to_urls(self, data, many, **kwargs):
        if not self.host and not self.base_path:
            return data

        def transform(item):
            if self.depends_on:
                item[self.depends_on] = [f"{self.host}/{self.depends_on}/{depends_id}" for depends_id in
                                         item[self.depends_on]]
            item['url'] = f"{self.host}/{self.base_path}/{item['id']}"
            item.pop('id')

        if many:
            for item in data:
                transform(item)
        else:
            transform(data)
        return data
