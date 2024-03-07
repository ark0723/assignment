from django.contrib import admin
from .models import Board

# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('writer', 'title','content','likes','created_at', "updated_at",)
    list_filter = ('date', 'writer')
    search_fields = ('title', 'content')
    ordering = ('date',) # 오름차순 정렬, ('-date') : 내림차순 정렬 dafault
    readonly_fields = ('writer', 'likes', 'reviews')
    list_per_page = 2 # default = 100
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('Advanced options', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
    )
    # 사용자 정의 대량 작업 추가
    actions = ('increment_likes',)
    def increment_likes(self, request, queryset):
        # 선택된 게시글에 대해 likes 1씩 증가
        for board in queryset:
            board.likes += 1
            board.save()
    
    increment_likes.short_description = "선택된 게시글의 좋아요 수 1씩 증가"
