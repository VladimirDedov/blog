main_menu = [
    {'title': 'Домашняя', 'url_name': 'index'},
    {'title': 'Резюме', 'url_name': 'resume'},
    {'title': 'Блог', 'url_name': 'blog'},
    {'title': 'Словарь', 'url_name': 'distionary'},
    {'title': 'API', 'url_name': 'api'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'Слово', 'url_name': 'add_word'},
    {'title': 'Добавить пост', 'url_name': 'add_post'}
]
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = main_menu
        return context