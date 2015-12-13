class FormMixin(object):
    def construct_widgets(self, fields, placeholders, must_delete=True):
        for field in fields.keys():
            if field in placeholders.keys():
                fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': placeholders[field]
                })
            else:
                if must_delete:
                    del fields[field]