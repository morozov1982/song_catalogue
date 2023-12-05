from django import forms
from django.contrib import admin
from django.db.models import Min
from django.utils.html import format_html

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Link, Song, Artist, Album, ArtistImage, Genre


class SongAdminForm(forms.ModelForm):
    lyrics = forms.CharField(label='Слова', widget=CKEditorUploadingWidget(), required=False)
    additional = forms.CharField(
        label='Дополнительная информация',
        widget=CKEditorUploadingWidget(),
        required=False,
        initial='<strong>Закольцованность припева:</strong> <br><strong>Диапазон:</strong> '
    )

    class Meta:
        model = Song
        fields = '__all__'


class ArtistAdminForm(forms.ModelForm):
    bio = forms.CharField(label='Биография', widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Artist
        fields = '__all__'


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class ArtistImageInline(admin.TabularInline):
    model = ArtistImage
    extra = 1


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    inlines = [LinkInline]
    list_display = ('title', 'display_performers', 'key', 'bpm', 'display_composers', 'display_authors',
                    'display_links', 'display_genres', 'slug')
    fields = (('title', 'slug', 'year'),
              ('key', 'chords', 'bpm'),
              'cover_image', 'genres',
              ('performers', 'performer_order'),
              ('composers', 'composer_order'),
              ('authors', 'author_order'),
              'lyrics', 'additional')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('performers', 'year', 'key', 'bpm', 'genres', 'composers', 'authors')
    search_fields = ('title', 'performers__nick_name', 'composers__nick_name', 'authors__nick_name')
    save_on_top = True
    save_as = True
    form = SongAdminForm
    filter_horizontal = ('performers', 'composers', 'authors', 'genres')

    def display_performers(self, obj):
        return ', '.join([str(p) for p in obj.performers.all()])

    def display_composers(self, obj):
        return ', '.join([str(c) for c in obj.composers.all()])

    def display_authors(self, obj):
        return ', '.join([str(a) for a in obj.authors.all()])

    def display_genres(self, obj):
        return ', '.join([str(a) for a in obj.genres.all()])

    def display_links(self, obj):
        links = obj.links.all()
        if links:
            return format_html(
                '<br>'.join([f'<a href="{link.url}" target="_blank">{link.description}</a>' for link in links]))
        return None

    display_performers.short_description = 'Исполнители'
    display_composers.short_description = 'Композиторы'
    display_authors.short_description = 'Авторы'
    display_genres.short_description = 'Стили'
    display_links.short_description = 'Ссылки'

    def get_queryset(self, request):
        queryset = Song.objects.annotate(first_performer_name=Min('performers__nick_name')).order_by(
            'first_performer_name', 'title')

        return queryset


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [ArtistImageInline]
    list_display = ('nick_name', 'slug')
    fields = (('nick_name', 'slug'),
              ('last_name', 'first_name', 'sur_name'),
              'bio')
    prepopulated_fields = {'slug': ('nick_name',)}
    search_fields = ('nick_name',)
    form = ArtistAdminForm


# admin.site.register(Song, SongAdmin)
# admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album)
admin.site.register(Genre)

admin.site.site_title = "Какталог песен"
admin.site.site_header = "Какталог песен"
