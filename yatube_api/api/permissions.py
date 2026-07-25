from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Изменять объект может только автор.
    Остальным разрешено только чтение.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
