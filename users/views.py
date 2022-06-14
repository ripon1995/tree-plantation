from djoser.views import UserViewSet as DjoserUserViewSet

#
# class UserViewSet(DjoserUserViewSet):
#     def perform_create(self, serializer):
#         if not serializer.is_valid():
#             data = {
#                 "message": 'fail'
#             }
#             return data
#
#         return serializer
